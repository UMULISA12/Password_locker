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
        save_contact method saves credential objects into credentials_list
        '''

        Credentials.credentials_list.append(self)  



    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credentials_list
        '''

        Credentials.credentials_list.remove(self)


    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list