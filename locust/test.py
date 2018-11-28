 import requets
 import uuid

 class SignuUpUsers(object):
    """
    Base class for page objects.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(SignuUpUsers, self).__init__()
        self.session = requests.Session()
 
  def u_signup(self, u_name, u_email, u_pwd, u_country):
          """
          Signup
          """
          url = u'/signup'
          default_headers = {
              'Host': 'api.xiangqi.arbisoft.com'
              'Accept': '*/*',
              'Accept-Language': 'en-US,en;q=0.5',
              'Accept-Encoding': 'gzip, deflate',
              'Content-Type': 'application/json',
              'Referer': 'http://xiangqi.arbisoft.com/signup'
              'origin': 'http://xiangqi.arbisoft.com'
          }
          params = {"username": u_name,"email":u_email,"password":u_pwd,"country_id":u_country,"locale":"en"}
          r = self.session.post(url=url, headers=default_headers, data=params)
          return r

signup_users = SignUpUsers()
username = 'test_{}'.format(str(uuid.uuid4().node))
email = "{}@example.com".format(username)
rs = signup_users.u_signup(username, email, 'temp', 226)
print rs.statuscode
print rs.content
