import smtplib
import random
import datetime as dt

MY_EMAIL = "mauriciolearningpython@gmail.com"
MY_PERSONAL_EMAIL = "mauriciomatos44@gmail.com"
MY_PASSWORD = "b483MM4nJD+#ZIT"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:

    with open("quotes.txt") as data:
        quote_list = data.readlines()
        quote_of_the_day = random.choice(quote_list).strip("\n")


    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            msg=f"Subject:Motivational Quotes\n\n{quote_of_the_day}",
            from_addr=MY_EMAIL,
            to_addrs=MY_PERSONAL_EMAIL)

