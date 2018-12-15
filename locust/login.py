import json


class Login(object):

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

    def login(self, u_email, u_password):
        """
        Login to Xiangqi
        :param u_email: User Email
        :param u_password:   User Password
        """
        url = u'http://api.xiangqi.arbisoft.com/api/users/signin'
        default_headers = {
            'Host': 'api.xiangqi.arbisoft.com',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/json',
            'Referer': 'http://xiangqi.arbisoft.com/signup',
            'origin': 'http://xiangqi.arbisoft.com'
        }
        params = {"email": u_email, "password": u_password, "locale": "en"}
        r = self.client.post(url=url, headers=default_headers, data=json.dumps(params), verify=False)
        self._check_response(r)
        return json.loads(r.content)['access_token']