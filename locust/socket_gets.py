import json


class SocketGet(object):

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

    def socket_get_cookie(self, access_token):
        url = u'http://api.xiangqi.arbisoft.com/socket.io/?xiangqi.jwt_token={}'.format(access_token)

        default_headers = {
            'Host': 'api.xiangqi.arbisoft.com',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/json',
            'Referer': 'http://xiangqi.arbisoft.com/lobby',
            'origin': 'http://xiangqi.arbisoft.com'
        }

        params = {"xiangqi.jwt_token": access_token, "param": "GROygq", "EIO": "3", "transport": "polling",
                  "t": "MUjmfzG", "sid": "f9df73dfbe7540258cc31624d2527485"}

        # r = self.session.post(url=url, headers=default_headers, data=json.dumps(params), verify=False)
        r = self.client.get(url=url, headers=default_headers, name="socket_get_cookie")
        self._check_response(r)
        return r.cookies.values()[0]

    def socket_get_after_post_transport_polling(self, access_token):
        url = u'http://api.xiangqi.arbisoft.com/socket.io/?xiangqi.jwt_token={}'.format(access_token)

        default_headers = {
            'Host': 'api.xiangqi.arbisoft.com',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/json',
            'Referer': 'http://xiangqi.arbisoft.com/lobby',
            'origin': 'http://xiangqi.arbisoft.com'
        }

        params = {"xiangqi.jwt_token": access_token, "param": "GROygq", "EIO": "3", "transport": "polling",
                  "t": "MUjmfzG", "sid": "f9df73dfbe7540258cc31624d2527485"}

        # r = self.session.post(url=url, headers=default_headers, data=json.dumps(params), verify=False)
        r = self.client.get(url=url, headers=default_headers, name='socket_get_after_post_transport_polling')
        self._check_response(r)
        return r.cookies.values()[0]

    def socket_get_after_post_transport_websocket(self, access_token):
        url = u'http://api.xiangqi.arbisoft.com/socket.io/?xiangqi.jwt_token={}'.format(access_token)

        default_headers = {
            'Host': 'api.xiangqi.arbisoft.com',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/json',
            'Referer': 'http://xiangqi.arbisoft.com/lobby',
            'origin': 'http://xiangqi.arbisoft.com'
        }

        params = {"xiangqi.jwt_token": access_token, "param": "GROygq", "EIO": "3", "transport": "websocket",
                  "t": "MUjmfzG", "sid": "f9df73dfbe7540258cc31624d2527485"}

        # r = self.session.post(url=url, headers=default_headers, data=json.dumps(params), verify=False)
        r = self.client.get(url=url, headers=default_headers, name='socket_get_after_post_transport_websocket')
        self._check_response(r)
        return r.cookies.values()[0]