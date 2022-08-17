import pandas
import datetime as dt
import smtplib
import random
data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")
data_dict_bd = data.to_dict()
data_dict_name = data_dict_bd["name"]
NAME = None


def send_mail():
    global NAME
    my_email = "pythonegitim02@hotmail.com"
    password = "assd6462d"
    list_messages = [
        "bd_letter_1.txt",
        "bd_letter_2.txt",
        "bd_letter_3.txt"
    ]
    letter_txt = random.choice(list_messages)
    send_email_address = data_dict[name]["email"]
    with open(f"letter_templates/{letter_txt}", "r") as file:
        letter = file.read()
        new_letter = letter.replace("[NAME]", NAME)

    with smtplib.SMTP("smtp.office365.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=send_email_address,
            msg=f"Subject:Happy Birthday {NAME}\n\n{new_letter}"
        )


# gets the current date
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

# checks if anyone has a birthday today
for name in data_dict_name:
    if data_dict[name]["year"] == year and \
            data_dict[name]["month"] == month and \
            data_dict[name]["day"] == day:
        NAME = data_dict[name]["name"]
        send_mail()
