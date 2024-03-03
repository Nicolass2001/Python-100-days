##################### Birthday Wisher ######################
import random
import smtplib
import pandas
import datetime as dt

EMAIL_SENDER = "pythonmailtest50@gmail.com"
PASSWORD_SENDER = "zpge cgrd exyo xjxg"

# 2. Check if today matches a birthday in the birthdays.csv
df = pandas.read_csv("birthdays.csv")
reciver_list = df.to_dict("records")

now = dt.datetime.now()
today_month = now.month
today_day = now.day

for reciver in reciver_list:
    if reciver.get("month") == today_month and reciver.get("day") == today_day:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter_file_path = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(letter_file_path) as letter_file:
            letter_template = letter_file.read()
            reciver_name = reciver.get("name")
            letter = letter_template.replace("[NAME]", reciver_name)
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL_SENDER, password=PASSWORD_SENDER)
            reciver_email = reciver.get("email")
            connection.sendmail(
                from_addr=EMAIL_SENDER,
                to_addrs=reciver_email,
                msg=f"Subject:Happy Birthday!\n\n{letter}"
            )


