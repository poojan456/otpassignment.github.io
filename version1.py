import math
import random
import smtplib
from twilio.rest import Client

def generateOTP(length):
    digits = "0123456789"
    otp = ""

    for i in range(length):
        otp += digits[math.floor(random.random()*10)]
    return otp

def ValidateMobileNo(MobileNo):
    if len(MobileNo) != 10:
        print("Please enter valid Mobile number!!")
        MobileNo = input("Enter the Mobile number:")
        ValidateMobileNo(MobileNo)
    return MobileNo


def ValidateEmailID(Email):
    if "@gmail.com" not in Email:
        print("Please Enter Valid Email address!!")
        Email = input("Enter the Email:")
        ValidateEmailID(Email)
    return Email
