import uuid
from locust import task, TaskSet
from signup import SignUpPage



class SignUpTasks(TaskSet):
    """
    User scripts that signsup the users
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(SignUpTasks, self).__init__(*args, **kwargs)
        self.user_signup = SignUpPage(self.locust.host, self.client)

    @task(1)
    def signup_task(self):
        """
        View the pages repeatedly
        """
        username = 'test_{}'.format(str(uuid.uuid4().node))
        email = "{}@example.com".format(username)
        self.user_signup.u_signup(username, email, 'temp', 226)
