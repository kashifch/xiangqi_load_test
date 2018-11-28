import json
from base import Base
from config import SEARCH_FLIGHT_URL


class SignUpPage(object):

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
        if response.status_code != 200:
            raise Exception(
                'API request failed with following error code: ' +
                str(response.status_code)
            )
        if "Operation successful" not in response.content:
            raise Exception(
                'API request failed to fetch data'
            )

    def u_signup(self, u_name, u_email, u_pwd, u_country):
        """
        Signup
        """
        url = u'/signup'
        default_headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/json',
            'Referer': 'http://xiangqi.arbisoft.com/signup'
        }
        params = {"username": u_name,"email":u_email,"password":u_pwd,"country_id":u_country,"locale":"en"}
        r = self.client.post(url=url, headers=default_headers, data=params, verify=False)
        self._check_response(r)
        return r


