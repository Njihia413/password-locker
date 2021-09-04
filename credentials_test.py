import unittest #Importing the unittest module
from credentials import Credentials #Importing the credentials class

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours
    '''
    def setUp(self):
        '''
        setUp method to run before each test cases
        '''

        self.new_credentials = Credentials("Github","dev-njihia","dev2021","dev_njihia@gmail.com")

    '''
    Test to check if credentials have been created successfully
    '''
    def test_create_credentials(self):
        self.assertEqual(self.new_credentials.account,"Github")
        self.assertEqual(self.new_credentials.user_name,"dev-njihia")
        self.assertEqual(self.new_credentials.password,"dev2021")
        self.assertEqual(self.new_credentials.email,"dev_njihia@gmail.com")

if __name__ == '__main__':
    unittest.main()


