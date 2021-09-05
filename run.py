#!/usr/bin/env python3.8
from random import choice
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

def delete_a_user(locker_user_name):
    """
    Function to delete a user
    """
    User.delete_user(locker_user_name)

def find_user(user):
    """
    Function to find a user
    """    
    user.find_by_username()

def check_existing_users(locker_user_name):
    """
    Function to check for existing users
    """
    return User.user_exist(locker_user_name)

def check_user_password(locker_user_name,locker_password):
    """
    Function to check wheher the user entered the correct username and password
    """
    return User.check_user(locker_user_name,locker_password)


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

def delete_the_credentials(account):
    """
    Function to delete credentials
    """
    return Credentials.delete_credentials(account)

def find_credentials(account):
    """
    Function to find credentials
    """
    return Credentials.find_by_account(account)

def check_existing_credentials(account):
    """
    Function to check for existing credentials
    """
    return Credentials.credentials_exist(account)

def display_the_credentials():
    """
    Function that returns all the saved credentials
    """
    return Credentials.display_credentials()

def generate_user_password(password_length):
    """
    Function to generate user password
    """
    return Credentials.generate_password(password_length)

"""Main Function"""
def main():
    print("Hello, What is your name?")
    name = input()

    print(f"Welcome to Password Locker {name}. How can I help you?")
    while True:
        print("-"*50)
        print("Use these short codes to use password locker:\n cc - create a new user account\n lg - login to your account\n da - display account\n ex - exit the application")
        print("-"*50)
        short_code = input().lower()
        if short_code == 'cc':
            print("Create a New User Account")
            print("-"*50)
            print("Enter your first name....")
            first_name = input()
            print("Enter your last name....")
            last_name = input()
            print("Enter your preferred username....")
            locker_user_name = input()
            print("Enter your password....")
            locker_password = input()
            save_a_user(create_user(first_name,last_name,locker_user_name,locker_password))
            print("-"*50)

            print(f"Hello {first_name}. Account created successfully. Please login to access your account")
            print("*"*50)
        elif short_code == 'lg' or short_code == 'da':
            print("*"*50)
            print("Enter your username....")
            locker_user_name = input()
            print("Enter your password....")
            locker_password = input()
            if check_existing_users(locker_user_name): #Check if a user exists
                #Check if password is correct
                if check_user_password(locker_user_name,locker_password):
                    print("\n")
                    print(f"Welcome back {locker_user_name}")
                    print("*"*50)
                    while True:
                        print("Select an option below to continue")
                        print("1. Create new credentials\n2. View saved credentials\n3. Delete credentials\n4. Logout")
                        print("\n")
                        user_choice = int(input())
                        if user_choice == 1:
                            print("Enter the account name of your credential account eg twitter,intagram....")
                            account = input()
                            print(f"Enter your {account} username")
                            user_name = input()
                            print(f"Enter your registered email address for {account}")
                            email = input()
                            print("\n")
                            #Allow user to generate passowrd or input preferred password
                            print("*"*50)
                            print("Do you want to generate a random passowrd or enter your preferred password?\n \n Press 1 to generate a random password\n Press 2 to input preferred password")
                            print("*"*10)
                            print("\n")
                            choice = int(input())
                            if choice == 1: #Generate random password
                                print("How long do you want your password?")
                                password_length = int(input())
                                password = generate_user_password(password_length)
                                print(f"Your password is {password}")
                            elif choice == 2:
                                print(f"Enter your preferred password for {account}")
                                password = input()
                            else:
                                print("Please select a valid input")

                            #Create and save credentials
                            save_the_credentials(create_credentials(account,user_name,email,password))
                            print(f"New Credentials with account name '{account}' and password '{password}' has been successfully created \n")
                            print("*"*10)

                        elif user_choice == 2: #Display credentials
                            print("\n")
                            print("Here is a list of all your credentials in the application")
                            print("*"*50)
                            if display_the_credentials():
                                for platform in display_the_credentials():
                                    print(f"Account: {platform.account}, Username: {platform.user_name}, Password: {platform.password}")
                            else:
                                print("No saved accounts!")
                                print("*"*50)

                        elif user_choice == 3: #Delete the credentials
                            print("Enter the account name you want to delete credentials for:")
                            account_name_to_delete = input()
                            if find_credentials(account_name_to_delete):
                                print(f"Credentials for '{account_name_to_delete}' have successfully been deleted")
                                print("\n")
                            else:
                                print("*"*50)
                                print(f"Credentials with account name '{account_name_to_delete}' do not exist!")
                                print("*"*50)

                        elif user_choice == 4:
                            print("You have successfully logged out")
                            print("*"*50)
                            break

                        else: #No account
                            print("No such account!")

                else:
                    print("You entered wrong credentials")
        elif short_code == 'ex': #Exit
            print("Goodbye...")
            break


"""Call Main Function"""
if __name__ == '__main__':
    main()






