import smtplib
import credential


with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=credential.MY_EMAIL, password=credential.MY_PASSWORD)
    connection.sendmail(
        from_addr=credential.MY_EMAIL,
        to_addrs=credential.MY_EMAIL,
        msg="Subject: Hello\n\n This is the body of my email"
    )
