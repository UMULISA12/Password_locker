
class Credentials:
    """
    Class that generates new instances of credential
    """

    credential_list = [] # empty credential list
 # Init method here
    def save_credentials(self):
        '''
        save_credential method saves credential objects into credential_list
        '''

        Credentials.credential_list.append(self)

    def __init__(self,user_name,phone_number,email,password):


        self.user_name = user_name
        self.phone_number = phone_number
        self.email = email
        self.password = password

    def delete_credential(self):
        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credentials.credential_list.remove(self)

    @classmethod
    def find_by_user_name(cls, name):
        '''
        This is a method that in which user can find credential by name search
        '''
        for credential in cls.credential_list:
            if credential.user_name == name:
                return credential

    @classmethod
    def credential_exist(cls,name):
        '''
        method that checks if the credential ade are already on the credential_list and return true (if exists) and false(if does not)
        '''
        for credential in cls.credential_list:
            if credential.user_name == name:
                return True

        return false 
    
    @classmethod
    def credential_display(cls):
        '''
        method that checks if the credential  already display on the  credential_list and return true (if exists) and false(if does not)
        '''
        return cls.credential_list
