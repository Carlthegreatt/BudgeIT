import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",  # or your host, e.g., '127.0.0.1'
    user="root",  # your MySQL username
    password="09082005",  # your MySQL password
    database="airbnb",  # your database name
)

cursor = conn.cursor()


def send_email():
    sender_email = "blancaflorcarlferros@gmail.com"
    cursor.execute("SELECT email, id FROM users")
    for i in cursor.fetchall():
        receiver_email = i[0]
        id = i[1]
        password = "irbx vimg qyke uopr"

    # Create the email
    message = MIMEMultipart("alternative")
    message["Subject"] = "Automated Email"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = """\
    Hi,
    This is an automated email sent from Python!
    """
    html = """\
    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Email Template</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <style>
      body {
        margin: 0;
        padding: 0;
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        background-color: #f4f4f4;
      }

      .container {
        max-width: 600px;
        margin: 40px auto;
        background-color: #ffffff;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
      }

      .header {
        background-color: #4a90e2;
        color: #ffffff;
        padding: 24px;
        text-align: center;
      }

      .content {
        padding: 24px;
        color: #333333;
        line-height: 1.6;
      }

      .button {
        display: inline-block;
        padding: 12px 24px;
        margin-top: 20px;
        background-color: #4a90e2;
        color: #ffffff;
        text-decoration: none;
        border-radius: 4px;
        font-weight: bold;
      }

      .footer {
        background-color: #f0f0f0;
        padding: 16px;
        text-align: center;
        font-size: 12px;
        color: #888888;
      }

      @media (max-width: 600px) {
        .container {
          margin: 20px;
        }

        .content,
        .header,
        .footer {
          padding: 16px;
        }
      }
    </style>
  </head>

  <body>
    <div class="container">
      <div class="header">
        <h1>Hello from Python!</h1>
      </div>
      <div class="content">
        <p>Hi there,</p>
        <p>
          This is an <strong>automated email</strong> sent using Python.
          You can customize this template to suit your needs.
        </p>
        <p>
          Click below to visit our site:
        </p>
        <a href="https://example.com" class="button">Visit Website</a>
        <p>
          Best regards,<br />
          Your Python Automation Script
        </p>
      </div>
      <div class="footer">
        &copy; 2025 Your Company. All rights reserved.
      </div>
    </div>
  </body>
</html>

    """

    # Attach both plain text and HTML versions
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    # Connect to Gmail SMTP server and send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email sent!")


send_email()
