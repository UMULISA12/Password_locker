import unittest # Importing the unittest module
from user import User # import user class

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours
    '''

    def tearDown(self):
            '''
            tearDown method that does cleanup after each test case has run
            '''
            User.user_list = []

    def setUp(self):
        '''
        Set up method to run before each test cases .
        '''
        self.new_user = User("Alice","12")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Alice)
        self.assertEqual(self.new_user.user_password,"12")
        self.assertEqual(self.new_credentials.site_name,"Github")
        self.assertEqual(self.new_credentials.site_username,"Alicia")
        self.assertEqual(self.new_credentials.site_password,"123")

    def test_save_user(self):
        '''
        test case to test if the user object is saved
        '''
        self.new_user.save_user() # save a user
        self.assertEqual(len(User.user_list),1)

    def test_multiple_user(self):
        '''
        test case to check if we can save multiple user objects
        '''
        self.new_user.save_user()
        test_user = User("Test","user")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    @classmethod
    def test_display_credentials(cls,name,password):
        '''
        test case to test if we can display credentials by name and password
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)



if __name__ == '__main__':
    unittest.main()