import unittest # Importing the unittest module
from user import Users # Importing the contact class
from credential import Credentials


class TestUsers(unittest.TestCase):

    '''
    Test class that defines test cases for the users class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
   
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = Users("Alice","UMULISA","Alicia","abana") # create user object
        # self.new_credential = Credentials("Github","UMULISA12","abana") # creating credential object


    def test_init(self):
        '''
        test_init test case to test if the user object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Alice")
        self.assertEqual(self.new_user.last_name,"UMULISA")
        self.assertEqual(self.new_user.user_name,"Alicia")
        self.assertEqual(self.new_user.password,"abana")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(Users.username_and_password_list),1)


    # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Users.username_and_password_list = []
    
    
    
    def test_save_multiple_user(self):
        '''
        test_save_multiple_users to check if we can save multiple user
         objects to our user_list
        '''
        self.new_user.save_user()
        test_user = Users("Alice","UMULISA","Alicia","abana") # new contact
        test_user.save_user()
        self.assertEqual(len(Users.username_and_password_list),2)


# if __name__ == '__main__':
#     unittest.main()



class TestCredentials(unittest.TestCase):
    '''
    Set up method to run before each test cases.
    '''

    def setUp(self):
        # '''
        # Set up method to run before each test cases.
        # '''
        # self.new_user = Users("Alice","UMULISA","Alicia","abana")
     self.new_credential = Credentials("Github","UMULISA12","abana") # creating credential object
    

    def test_init(self):
        '''
        test_init test case to test if the credential object is initialized properly
        '''

        self.assertEqual(self.new_credential.site_name,"Github")
        self.assertEqual(self.new_credential.site_username,"UMULISA12")
        self.assertEqual(self.new_credential.site_password,"abana")


    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credentials.credentials_list),1)



    # setup and class creation up here
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []



    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credential
         objects to our credentials_list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Github","UMULISA12","abana") # new credential
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list),2)



  
    def test_delete_credential(self):
            '''
            test_delete_credential to test if we can remove a credential from our credentials list
            '''
            self.new_credential.save_credential()
            test_credential = Credentials("Github","UMULISA12","abana") # new credential
            test_credential.save_credential()

            self.new_credential.delete_credential()# Deleting a contact object
            self.assertEqual(len(Credentials.credentials_list),1)



    def test_find_credential_by_site_name(self):
            '''
            test to check if we can find credential by site_name and display username and password
            '''

            self.new_credential.save_credential()
            test_credential = Credentials("Github","UMULISA12","abana") # new credential
            test_credential.save_credential()

            found_credential = Credentials.find_by_site_name("Github")

            self.assertEqual(found_credential.site_username,test_credential.site_username)















if __name__ == '__main__':
    unittest.main()


