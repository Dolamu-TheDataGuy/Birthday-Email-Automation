import smtplib


my_email = "dolamuoludare@gmail.com"

password = "bmvmxaaytwthyzsr"

my_email1 = "dolamuoludare@yahoo.com"


with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email1,
        msg="Subject: Hello\n\n This is the body of my email"
    )
