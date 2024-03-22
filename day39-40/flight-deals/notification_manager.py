import smtplib

EMAIL_SENDER = "pythonmailtest50@gmail.com"
PASSWORD_SENDER = "zpge cgrd exyo xjxg"
EMAIL_RECIVER = "python0891273654@hotmail.com"

class NotificationManager:
    
    def send_message(message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL_SENDER, password=PASSWORD_SENDER)
            connection.sendmail(
                from_addr=EMAIL_SENDER,
                to_addrs=EMAIL_RECIVER,
                msg=f"Subject:Flight Deals\n\n{message}"
            )
