from __builtin__ import basestring

import re
import requests


__all__ = [
    'NumberException', 'ElksException', 'ElksRestClient',
    'format_swedish_number'
]


class NumberException(Exception):
    pass


class NotASwedishNumberException(NumberException):
    pass


class ElksException(Exception):
    def __init__(self, status_code, message):
        super(ElksException, self).__init__("%s - %s" % (status_code, message))


class ElksRestClient(object):
    """
    Basic client for accessing the 46elks REST API
    """

    def __init__(self, account, token, base="https://api.46elks.com/a1/"):
        self.base = base
        self.auth = (account, token)

    def request(self, path, method='GET', vars=None):
        """
        sends a request and gets a response from the 46elks REST API
        """
        if method and method not in ['GET', 'POST']:
            raise NotImplementedError(
                'HTTP method %s not implemented' % method)

        uri = '%s%s' % (self.base, path)

        if method == 'GET':
            response = requests.get(uri, auth=self.auth, params=vars)
        elif method == 'POST':
            response = requests.post(uri, auth=self.auth, data=vars)

        if response.status_code == 200:
            return response.json()
        else:
            raise ElksException(response.status_code, response.text)

    def SMS(self, to, sender, message, flashsms=False, whendelivered=None):
        """
        send a SMS through the 46elks REST API
        """
        vars = {
            'from': sender,
            'message': message,
        }

        if isinstance(to, basestring):
            to = [to]
        vars['to'] = ','.join(format_swedish_number(n) for n in to)

        if flashsms:
            vars['flashsms'] = 'yes'
        if whendelivered:
            vars['whendelivered'] = whendelivered
        return self.request('SMS', 'POST', vars)


def format_swedish_number(number):
    """
    formats numbers so they can be accepted by 46elks

    e.g. these are all turned into "+46701234567":
    0701234567
    701234567
    +46701234567
    +460701234567 (!)
    46701234567
    070 123 45 67
    070 - 123 45 67
    070-12 34 567
    """
    n = str(number).strip()

    if n.startswith('+') and not n.startswith('+46'):
        raise NotASwedishNumberException("This number isn't a Swedish number")

    # remove all non-numeric characters
    n = re.sub(r'[^0-9]', '', n)
    if n.startswith('46'):  # remove country code
        n = n[2:]
    n = n.lstrip('0')  # remove leading 0

    # is this a valid Swedish cell phone number?
    if len(n) != 9:
        raise NumberException(
            "%s is not a valid Swedish cell phone number - "
            "number is %d characters (should be 9)" % (n, len(n)))
    if n[:2] not in {'70', '72', '73', '76', '10'}:
        raise NumberException(
            "%s is not a valid Swedish cell phone number - "
            "0%s is not a valid region code" % (n, n[:2]))

    return '+46%s' % n
