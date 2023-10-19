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

def sendOTPOverEmail(Checked_email, OTP):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls() 
    server.login('pooja1713953@gmail.com', 'kaxwlziuipezhgih')
    message = 'Your 4 digit OTP is '+str(OTP)
    server.sendmail('pooja1713953@gmail.com',
                    Checked_email, message)
    server.quit()

def sendOTPOverMessage(Checked_MobileNo, OTP):
    account_sid = 'ACb5baf5f93fe0d1ec919cae3a2d66bf41'
    auth_token = 'a5206483ad0d5cfaf854a97372f9c63e'
    client= Client(account_sid, auth_token)
    msg = client.messages.create(
        body= 'your OTP is' +OTP,
        from_= '+17027238962',
        to = '+91'+str(Checked_MobileNo),
)
    
MobileNo = input("Enter the Mobile number:")
Checked_MobileNo = ValidateMobileNo(MobileNo)

Email = input("Enter the Email:")
Checked_email = ValidateEmailID(Email)

# will Generate OTP
OTP = generateOTP(4)

# send OTP to Number
sendOTPOverMessage(Checked_MobileNo, OTP)

# send to email
sendOTPOverEmail(Checked_email, OTP)

