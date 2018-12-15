import json


class SocketPost(object):

    """
    Course page Class
    """

    def __init__(self, hostname, client):
        """
        Initialize the client.
        :param hostname: The hostname of the test server
        :param client: The test client used by locust.
        """
        self.hostname = hostname
        self.client = client

    def _check_response(self, response):
        """
        Check whether a response was successful.
        """
        if response.status_code not in (200, 201):
            raise Exception(
                'API request failed with following error code: ' +
                str(response.status_code)
            )

    def socket_post(self, access_token, cookie):
        url = 'http://api.xiangqi.arbisoft.com/socket.io/?xiangqi.jwt_token={}&param=GROygq=3&transport=polling&t=MUjmfzG&sid={}'.format(
            access_token, cookie)

        default_headers = {
            'Host': 'api.xiangqi.arbisoft.com',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/json',
            'Referer': 'http://xiangqi.arbisoft.com/lobby',
            'origin': 'http://xiangqi.arbisoft.com',
            'Cookie': 'io='.format(cookie)
        }

        r = self.client.post(url=url, headers=default_headers, verify=False, name='socket_post')

        return r