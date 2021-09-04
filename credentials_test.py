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
    Teardown method does clean up after each test case has run
    '''
    def tearDown(self):
        Credentials.credential_list = []

    '''
    Test to check if credentials have been created successfully
    '''
    def test_create_credentials(self):
        self.assertEqual(self.new_credentials.account,"Github")
        self.assertEqual(self.new_credentials.user_name,"dev-njihia")
        self.assertEqual(self.new_credentials.password,"dev2021")
        self.assertEqual(self.new_credentials.email,"dev_njihia@gmail.com")

    '''
    Test to check if credentials object is saved into the credentials list
    '''
    def test_save_credentials(self):
        self.new_credentials.save_credentials() #Saving the credentials
        self.assertEqual(len(Credentials.credential_list),1)

    '''
    Test to check if multiple credentials objects are saved
    '''
    def test_save_multiple_credentials(self):
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Github","dev-njihia","dev2021","dev_njihia@gmail.com")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credential_list),2)

    '''
    Test to check if credentials can be deleted
    '''
    def test_delete_credentials(self):
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Github","dev-njihia","dev2021","dev_njihia@gmail.com")
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials() #Delete a credential object
        self.assertEqual(len(Credentials.credential_list),1)

    '''
    Test to find credentials by account
    '''
    def test_find_by_account(self):
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Github","dev-njihia","dev2021","dev_njihia@gmail.com")
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_account("Github")
        self.assertEqual(found_credentials.user_name,test_credentials.user_name)

    '''
    Test to check if credentials exist
    '''
    def test_credentials_exists(self):
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Github","dev-njihia","dev2021","dev_njihia@gmail.com")
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exist("Github")
        self.assertTrue(credentials_exists)



if __name__ == '__main__':
    unittest.main()


