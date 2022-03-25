import smtplib

def send_email():
    sender = "albertorodrigues7248@gmail.com"
    receiver = "albertorodrigues7248@gmail.com"
    password = 'cool&pass*225'

    connection = smtplib.SMTP("smtp.gmail.com",port=587)
    connection.starttls()
    connection.login(user=sender, password=password)
    connection.sendmail(sender,receiver,msg="Subject:ISS nearby!\n\nThe ISS is in your area. Look up!")
    connection.close()

send_email()