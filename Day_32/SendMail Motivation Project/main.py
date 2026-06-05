import smtplib
import datetime as dt
import random
import pathlib

MY_EMAIL = ""
MY_PASSWORD = ""

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open(pathlib.Path("quotes.txt")) as quote_files:
        all_quotes = quote_files.readlines()
        quote = random.choice(all_quotes)
        
    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Friday Motivation\n\n{quote}."
        )
        
    
