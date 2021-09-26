# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 12:02:36 2021

@author: sankar
"""
from stdiomask import getpass
import hashlib
import os
import re
clear = lambda: os.system('cls')

def mainform():
    clear()
    print("---------")
    print("MAIN MENU")
    print("---------")
    print()
    print("Type 1 for Register")
    print("Type 2 for Login")
    print()
    while True:
        print()
        userChoice = input("Choose An Option: ")
        if userChoice in ['1', '2']:
            break
    if userChoice == '1':
        Register()
    else:
        Login()

def getInfo():
    usersDetail = {}
    if os.path.exists(datafile) and os.path.getsize(datafile) > 0:
        with open(datafile, 'r') as file:
            for line in file:
                line = line.split()
                usersDetail.update({line[0]: line[1]})
    
    return usersDetail

def userchoice(choice,mode):
    
    if choice == 'yes' or choice == 'YES' or choice == 'Yes':
        if mode=="Register":
            Login()
        elif mode=="Login":
            Register()
        elif mode=="Final":
            mainform()
    else: 
        if mode=="Register":
            mainform()
        elif mode=="Login":
            print("Please type correct email address")
            print()
        elif mode=="Final":
            print("Welcome")
            print()
    
def Register():
    clear()
    print("---------")
    print("REGISTER")
    print("--------")
    print()
    while True:
        userName = input("Enter Your Email address: ")
        if userName != '':
            if validateEmail(userName):
                break
        
    if userAlreadyExist(userName):
        displayUserAlreadyExistMessage()
    else:
        while True:
            userPassword = getpass("Enter Your Password: ")
            if userPassword != '':
                if validatePassword(userPassword):
                    break
            
        while True:
            confirmPassword = getpass("Confirm Your Password: ")
            if confirmPassword == userPassword:
                break
            else:
                print("Passwords Don't Match")
                print()
        
        addUserInfo([userName, hash_password(userPassword)])

        print()
        print("Registered Successfully!")
        print()
        loginchoice = input("Do you want to Login now ? (Type yes) : ")
        userchoice(loginchoice,"Register")
    
def Login():
    clear()
    print("---------")
    print("LOGIN")
    print("---------")
    print()
    usersInfo=getInfo()

    while True:
        userName = input("Enter Your Email: ")
        if validateEmail(userName):
            if userName not in usersInfo:
                print("This email address is Not Registered. Provide correct email address")
                
                print()
                registerchoice = input("Do you want to Register now ? (Type yes) : ")
                userchoice(registerchoice,"Login")

            else:
                break
            
    while True:
        userPassword = getpass("Enter Your Password: ")
        validpassword=check_password(userPassword, usersInfo[userName])
        if not validpassword:
            print("Incorrect Password")
            print()
        else:
            break
    print()
    print("Logged In Successfully!")
    print()
    finalchoice = input("Do you want to Logout and return to Main Screen now ? (Type yes) : ")
    userchoice(finalchoice,"Final")

def addUserInfo(userInfo: list):
    with open(datafile, 'a') as file:
        for info in userInfo:
            file.write(info)
            file.write(' ')
        file.write('\n')

def userAlreadyExist(userName, userPassword=None):
    usersInfo=getInfo()

    users=list(usersInfo.keys())
    if userName in users:
        return True
    return False

def displayUserAlreadyExistMessage():
    while True:
        print()
        error = input("You Are Already Registered.\n\nPress (T) To Try Again:\nPress (L) To Login: ").lower()
        if error == 't':
            Register()
            break
        elif error == 'l':
            Login()
            break

def validateEmail(email):
    pattern=r"\w+@\w+\.\w{2,}"
    if  re.match(pattern, email):
        email_result = True
    else:
        email_result = False
        print("Email address is not valid")
        print()
    return email_result   
    
def validatePassword(password):
    if len(password)>=5:
        sp_char= re.compile('[@_!#$%^&*()<>?/\|}{~:]')       
        numCheck=r"[0-9]+"
        cond1 = any(c.isalpha() for c in password)
        cond3 =any(c.isupper() for c in password) 
        cond4 =any(c.islower() for c in password) 
        valid=cond1 and cond3 and cond4
      
        if(sp_char.search(password)!= None):       
            if re.search(numCheck,password):
                if valid:
                    return  True
    print(("Password is not valid"))
    print()
    return False 

def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_password(password, hash):
    return hash_password(password) == hash

#Change the file path based on your file location
datafile=r"C:\Users\userInfo.txt"

mainform()
