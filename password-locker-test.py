import unittest # Importing the unittest module
from credential import Credentials # Importing the credential class       
import user

class TestCredential(unittest.TestCase):

    '''
    Test class that defines test cases for the credential class behaviours.
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''    

    def setUp(self):
        '''
        set up method to run before each test cases.
        '''
        self.new_credential = Credentials("github","alice","123") # create credential object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.acc_name,"github")
        self.assertEqual(self.new_credential.acc_username,"alice")
        self.assertEqual(self.new_credential.password,"123")

    def test_save_credential(self): 
        '''
        test_save_credential test case to test if the credential object is saved into the credential list
        ''' 
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credentials.credential_list),1) 

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Test","umulisaa0@gmail.com","password") # new credential
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credential_list),2)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credential_list = []

 # other test cases here
    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Test","umulisaa0@gmil.com","123") # new credential
        self.assertEqual(len(Credentials.credential_list),1)

    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from our credential list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Test","umulisaa0@gmil.com","123") # new credential
        test_credential.save_credential()

        self.new_credential.delete_credential() # Deleting a credential object
        self.assertEqual(len(Credentials.credential_list),1)

    def test_find_credential_by_user_name(self):
        '''
        this will check if we can find a credential by user name and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credentials("Alia", "0785256555", "umulisaa0@gmai.com", "password")
        test_credential.save_credential()

        found_credential = Credentials.find_by_user_name("Alia")
        self.assertEqual(found_credential.acc_name, test_credential.acc_name) 

    def test_credential_exist(self):
        '''
        check if credential exist and return a boolean
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Alia", "0785256555", "umulisaa0@gmai.com", "password") 

        credentials_exist = Credentials.credential_exist    
        self.assertTrue(credentials_exist) 

    def test_display_all_credentials(self):
        '''
        test method that returns a list of all the credential saved.
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("alice", "0785256555", "umulisaa0@gmai.com", "123") 
        test_credential.save_credential()
 



if __name__ == '__main__':
    unittest.main()      