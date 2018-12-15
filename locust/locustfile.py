import os
from locust import HttpLocust, TaskSet
from XiangqiLocustTasks import SignUpTasks


class XiangqiTest(TaskSet):
    """
    Execute Load tests
    """
    tasks = {
        SignUpTasks: 1
    }


class ArbisoftLocust(HttpLocust):
    """
    Representation of an HTTP "user".
    Defines how long a simulated user should wait between executing tasks, as
    well as which TaskSet class should define the user's behavior.
    """
    task_set = globals()[os.getenv('LOCUST_TASK_SET', 'XiangqiTest')]
    min_wait = 1000
    max_wait = 3000