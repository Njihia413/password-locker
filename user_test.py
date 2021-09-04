import unittest #Import unittest module
from user import User #Importing the User Class

class TestUser(unittest.TestCase):
    '''
    Test Class that defines test cases for the user class behaviours
    '''
    def setUp(self):
        self.new_user = User("Maureen","Njihia","Njihia413","Melissa@atara413")

    '''
    Test to check if user is successfully created
    '''    
    def test_create_user(self):
        self.assertEqual(self.new_user.first_name,"Maureen")
        self.assertEqual(self.new_user.last_name,"Njihia")
        self.assertEqual(self.new_user.locker_user_name,"Njihia413")
        self.assertEqual(self.new_user.locker_password,"Melissa@atara413")

    '''
    Test to check if the user is saved
    '''    
    def test_save_user(self):
        self.new_user.save_user() #Saving the new user
        self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
    unittest.main()
