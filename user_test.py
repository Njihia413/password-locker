import unittest #Import unittest module
from user import User #Importing the User Class

class TestUser(unittest.TestCase):
    '''
    Test Class that defines test cases for the user class behaviours
    '''
    def setUp(self):
        self.new_user = User("Maureen","Njihia","Njihia413","Melissa@atara413")

    '''
    Teardown method does clean up after each test case has run
    '''
    def tearDown(self):
        User.user_list = []

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

    '''
    Test to check if multiple users can be saved
    '''
    def test_save_multiple_user(self):
        self.new_user.save_user()
        test_user = User("Maureen","Njihia","Njihia413","Melissa@atara413")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    '''
    Test to check if a user can be deleted
    '''
    def test_delete_user(self):
        self.new_user.save_user()
        test_user = User("Maureen","Njihia","Njihia413","Melissa@atara413")
        test_user.save_user()

        self.new_user.delete_user()  #Deleting a user
        self.assertEqual(len(User.user_list),1)

    '''
    Test to find a user by password_locker_username
    '''
    def test_find_user_by_username(self):
        self.new_user.save_user()
        test_user = User("Maureen","Njihia","Njihia413","Melissa@atara413")
        test_user.save_user()

        found_user = User.find_by_username("Njihia413")
        self.assertEqual(found_user.first_name,test_user.first_name) 

    '''
    Test to check if a user exists
    '''
    def test_user_exists(self):
        self.new_user.save_user()
        test_user = User("Maureen","Njihia","Njihia413","Melissa@atara413")
        test_user.save_user()  

        user_exists = User.user_exist("Njihia413")
        self.assertTrue(user_exists)          


if __name__ == '__main__':
    unittest.main()
