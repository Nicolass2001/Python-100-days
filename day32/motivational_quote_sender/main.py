import smtplib
import datetime as dt
import random

with open(file="quotes.txt") as quotes_file:
    quotes_list = quotes_file.readlines()
    quote = random.choice(quotes_list)

my_email = "pythonmailtest50@gmail.com"
password = "zpge cgrd exyo xjxg"

if dt.datetime.now().weekday() == 3:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="python0891273654@hotmail.com",
            msg=f"Subject:Feliz Jueves\n\n{quote}"
        )



