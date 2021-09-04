#!usr/bin/env python3.8
from user import User
from credentials import Credentials

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

