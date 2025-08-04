# Hi, This a an Email Sending Application that sends an Email Reminding me of my tasks.

import smtplib
import schedule
import time
from email.message import EmailMessage




def email_sender():
    try:
        # This port number is very important
        port = 587
        smtp_server = "smtp.gmail.com"
        sender_email = "sender@gmail.com"
        receiver_email = "receiver@gmail.com"
        # Use Google app password
        password = "" 
        subject = "Your Reminder"
        message ="""

            Hi there,

            You must finish Crash Course, 
            Fluent Python and Dsa the fun way.

            Take good care,
            Bye ;) me 
        """
        # Formats the Email in the correct order
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg.set_content(message)
        # The right and Secure way to send emails using smtplib
        with smtplib.SMTP(smtp_server,port) as server: 
            server.starttls()
            server.login(sender_email,password)
            server.send_message(msg)

        print("Successfully Done")
    
    except Exception as e:
        print(f"Exception: {e} ")




schedule.every().day.at("19:10").do(email_sender)

while True:
    schedule.run_pending()
    time.sleep(1)
    
