class User :
    user_list = [] #Empty users list

    """
    Class that generates new instances of a user
    """
    def __init__(self,first_name,last_name,locker_user_name,locker_password):
        '''
        __init__ method helps us define properties for our objects
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.locker_user_name = locker_user_name
        self.locker_password = locker_password

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)    