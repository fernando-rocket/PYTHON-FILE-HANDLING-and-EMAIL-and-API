import smtplib

my_email = "colocar o email aq"
password = "colocar a senha aq"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="email destinatário", 
msg="Subject:Hello\n\nThis is the body of my email")
connection.close()

# Outro mode de fazer
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="email destinatário", 
#     msg="Subject:Hello\n\nThis is the body of my email")

