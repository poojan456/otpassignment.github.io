import smtplib
import random 

otp = (random.randrange(100000, 999999))
my_mail = "pooja1713953@gmail.com"
passcode = "kaxwlziuipezhgih"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_mail, password=passcode)


mail_content = f"Your OTP is {otp}"

try:
   connection.sendmail(from_addr=my_mail, to_addrs="pooja1713953@gmail.com",msg=mail_content)
except Exception as e:
   print("Something went wrong while sending the email", e)

connection.close()