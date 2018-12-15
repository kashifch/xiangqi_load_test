import uuid
import random
from locust import task, TaskSet
from signup import SignUpPage
from login import Login
from socket_gets import SocketGet
from socket_posts import SocketPost



class SignUpTasks(TaskSet):
    """
    User scripts that signsup the users
    """
    usernames = ['user1@grr.la',
                 'user2@grr.la',
                 'user3@grr.la',
                 'user4@grr.la',
                 'user5@grr.la',
                 'user6@grr.la',
                 'user7@grr.la',
                 'user8@grr.la',
                 'a@stage.com',
                 'd@stage.com'
                 ]

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(SignUpTasks, self).__init__(*args, **kwargs)
        self.user_signup = SignUpPage(self.locust.host, self.client)
        self.user_login = Login(self.locust.host, self.client)
        self.socket_get = SocketGet(self.locust.host, self.client)
        self.socket_post = SocketPost(self.locust.host, self.client)
        self.token = ''
        self.cookie = ''

    def on_start(self):
        """
        Login to Xiangqi
        """
        self.credentials = random.choice(self.usernames)
        # Login and return access token
        self.token = self.user_login.login(self.credentials, '123')
        # Get request after the login to get the cookie
        self.cookie = self.socket_get.socket_get_cookie(self.token)

    def signup_task(self):
        """
        View the pages repeatedly
        """
        # username = 'test_{}'.format(str(uuid.uuid4().node))
        username = 'awais.khan+{}'.format(random.randint(1, 10))
        email = "{}@arbisoft.com".format(username)
        self.user_signup.options()
        self.user_signup.u_signup(self.username, self.email, '123', 226)

    @task(20)
    def socket_post_request(self):
        """
        Post request after clicking 'Start New game' button
        """
        self.socket_post.socket_post(self.token, self.cookie)

    @task(20)
    def socket_get_polling(self):
        """
        Get request after the POST with transport parameter as 'polling'
        :return:
        """
        self.socket_get.socket_get_after_post_transport_polling(self.token)

    @task(20)
    def socket_get_websocket(self):
        """
        Get request after the POST with transport parameter as 'websocket'
        """
        self.socket_get.socket_get_after_post_transport_websocket(self.token)