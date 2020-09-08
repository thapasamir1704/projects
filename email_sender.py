import smtplib
from email.message import EmailMessage

name=input("input your name :")
emailadd=input("input email address of recipient :")
subjectmatter=input("enter your email subject. :")
content=input ("enter your email content :")
own_email=input ("enter your email address :")
own_password=input("input your password :" )
email = EmailMessage()
email['from'] = name
email['to'] = emailadd
email['subject'] = subjectmatter

email.set_content(content)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login(own_email ,own_password)
  smtp.send_message(email)
  