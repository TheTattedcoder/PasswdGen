import string
import secrets
import os
import random

def main():
    welcome()
    length = passLength()
    listOfPasswords = generatePassword(length)



def welcome():
    '''Welcomes all users'''
    print('Welcome to PasswdGEN')
    user = input('What\'s your name? > ')
    print(f'Hey {user}! Let\'s get your ass a password')
    
    
    
def passLength():
    try:
        length = int(input('Please enter a password length: '))  
    except:
        print('Enter a valid number. Prefferably 10-15 ')
        length = int(input('Please enter a password length: ')) 
        
    return length
        
    

def generatePassword(length):
    passwords = []
    i = 0 
    alphanumeric = list(string.ascii_letters + string.digits + '!@#$%^&*()_')
    while i <= 5:
        password = [''.join(secrets.choice(alphanumeric) for i in range(length))]
        random.shuffle(password)
        passwords.append(password)
    
     
        
        


            
    

        
    