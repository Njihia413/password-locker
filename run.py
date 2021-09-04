#!usr/bin/env python3.8
from user import User
from credentials import Credentials

"""
Implementing user functions
"""
def create_user(first_name,last_name,locker_user_name,locker_password):
    """
    Function to create a new user
    """
    new_user = User(first_name,last_name,locker_user_name,locker_password)
    return new_user

def save_a_user(user):
    """
    Function to save user
    """
    user.save_user()

def delete_a_user(user):
    """
    Function to delete a user
    """
    user.delete_user()

def find_user(user):
    """
    Function to find a user
    """    
    user.find_by_username()

def check_existing_users(user):
    """
    Function to check for existing users
    """
    user.user_exist

"""
Implementing credentials functions
"""
def create_credentials(account,user_name,password,email):
    """
    Function to create new credentials
    """
    new_credentials = Credentials(account,user_name,password,email)
    return new_credentials

def save_the_credentials(credentials):
    """
    Function to save credentials
    """
    credentials.save_credentials()

def delete_the_credentials(credentials):
    """
    Function to delete credentials
    """
    credentials.delete_credentials()

def find_credentials(credentials):
    """
    Function to find credentials
    """
    credentials.find_by_account()

def check_existing_credentials(credentials):
    """
    Function to check for existing credentials
    """
    credentials.credentials_exist()

def display_the_credentials(credentials):
    """
    Function that returns all the saved credentials
    """
    credentials.display_credentials()
    