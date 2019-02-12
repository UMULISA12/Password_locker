class Users:
    """
    Class that generates new instances of contacts

    """
    username_and_password_list = [] # Empty credential list
  
    def __init__(self,userName,password):

      # docstring removed for simplicity

        # self.first_name = first_name
        # self.last_name = last_name
        self.userName = userName
        self.password = password

    def save_user(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        Users.username_and_password_list.append(self)   



       
