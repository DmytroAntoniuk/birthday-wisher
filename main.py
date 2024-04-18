import smtplib

sender_email = "8antoniuk8@gmail.com"
password = "uxpb zxsq oipf zzwu"
recipient_email = "oksana.bondarchuk03@gmail.com"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=sender_email, password=password)
    connection.sendmail(
        from_addr=sender_email, 
        to_addrs=recipient_email, 
        msg="Subject:Hello\n\noverLAP"
        )
    connection.close()
