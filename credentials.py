class Credentials:
    credential_list = [] #Empty credential list
    """
    Class that generates new instances of credentials
    """
    def __init__(self,account,user_name,password,email):
        '''
        __init__ method helps us to define properties for our objects
        '''
        self.account = account
        self.user_name = user_name
        self.password = password
        self.email = email