import smtplib
from email.mime.text import MIMEText

gmail_user = 'andreas.ded2@gmail.com'
gmail_password = 'punksk8er12345%'

from_=gmail_user
to =['iwsifa@gmail.com','krnikos@gmail.com']
subject = 'OMG Super Important Message'
body = 1234
email_text = "niko ti kaneis re mouni "+str(body)
message='Subject: %s\n\n %s'%(subject,email_text)



try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(from_,to,message)
    server.close()
    print("ok")
except:
    print 'Something went wrong...'
