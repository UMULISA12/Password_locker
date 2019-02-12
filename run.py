#!/usr/bin/env python3.6

from credential import Credentials

def create_credential(site_name,site_username,site_userpassword):
    '''
    Function to create a new credential
    '''
    new_credential = Credentials(site_name,site_username,site_userpassword)
    return new_credential


def save_credentials(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()


def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()