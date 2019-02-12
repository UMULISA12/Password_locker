class Credentials:
    """
    Class that generates credentials
    """

    credentials_list = [] # Empty credential list

    def __init__(self,site_name,site_username,site_password):

     
        self.site_name = site_name
        self.site_username = site_username
        self.site_password = site_password


    def save_credential(self):

        '''
        save_credentials method saves credential objects into credentials_list
        '''

        Credentials.credentials_list.append(self)  



    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credentials_list
        '''

        Credentials.credentials_list.remove(self)



    @classmethod
    def find_by_site_name(cls,site_name):
        '''
        Method that takes in a site and returns a username that matches that site_name.

        Args:
            site: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''
        for credential in cls.credentials_list:
            if credential.site_name == site_name:
                return credential




    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list