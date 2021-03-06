import random
import string

class Credentials:
    credential_list = [] #Empty credential list
    """
    Class that generates new instances of credentials
    """
    def __init__(self,account,user_name,password,email):
        """
        __init__ method helps us to define properties for our objects
        """
        self.account = account
        self.user_name = user_name
        self.password = password
        self.email = email

    def save_credentials(self):
        """
        save_credentials method saves credentials into the credential_list
        """
        Credentials.credential_list.append(self)

    def delete_credentials(self):
        """
        delete_credentials method to delete credentials from the credential_list
        """
        Credentials.credential_list.remove(self)

    @classmethod
    def find_by_account(cls,account):
        """
        find credentials by account
        """
        for credentials in cls.credential_list:
            if credentials.account == account:
                return credentials  

    @classmethod
    def credentials_exist(cls,account):
        """
        check if credentials exist
        """ 
        for credentials in cls.credential_list:
            if credentials.account == account:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        """
        method that returns the credential_list
        """
        return cls.credential_list

    @classmethod
    def generate_password(cls,password_length):
        """
        method to generate a random password for a user creating a new account
        """
        alpha = string.ascii_letters + string.digits
        password = ''.join(random.choice(alpha)
        for i in range(password_length))
        return password
        
