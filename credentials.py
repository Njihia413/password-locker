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

    def save_credentials(self):
        '''
        save_credentials method saves credentials into the credential_list
        '''
        Credentials.credential_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method to delete credentials from the credential_list
        '''
        Credentials.credential_list.remove(self)