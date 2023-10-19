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

try:
   connection.sendmail(from_addr=my_mail, to_addrs="pooja1713953@gmail.com",msg=mail_content)
except Exception as e:
   print("Something went wrong while sending the email", e)

connection.close()
