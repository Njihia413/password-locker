import unittest #Import unittest module
from user import User #Importing the User Class

class TestUser(unittest.TestCase):
    '''
    Test Class that defines test cases for the user class behaviours
    '''
    def setUp(self):
        self.new_user = User("Maureen","Njihia","Njihia413","Melissa@atara413")

    def test_create_user(self):
        self.assertEqual(self.new_user.first_name,"Maureen")
        self.assertEqual(self.new_user.last_name,"Njihia")
        self.assertEqual(self.new_user.locker_user_name,"Njihia413")
        self.assertEqual(self.new_user.locker_password,"Melissa@atara413")

if __name__ == '__main__':
    unittest.main()
    