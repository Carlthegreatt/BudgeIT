import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailSender:
    def __init__(self, receiver_email, username):
        self.receiver_email = receiver_email
        self.username = username

    def send_email(self):
        # Create the email
        message = MIMEMultipart("alternative")
        message["Subject"] = f"Welcome to BudgeIT, {self.receiver_email}!"
        message["From"] = "santoschinkit@gmail.com"
        message["To"] = self.receiver_email

        text_content = """\
      Hi,
      This is an automated email sent from Python!
      """
        html_content = """\
        <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <title>Email Template</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <style>
          body {{
            margin: 0;
            padding: 0;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            background-color: #f4f4f4;
          }}

          .container {{
            max-width: 600px;
            margin: 40px auto;
            background-color: #ffffff;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
          }}

          .header {{
            background-color: #ff7369;
            color: #ffffff;
            padding: 24px;
            text-align: center;
          }}

          .content {{
            padding: 24px;
            color: #333333;
            line-height: 1.6;
          }}

          .button {{
            display: inline-block;
            padding: 12px 24px;
            margin-top: 20px;
            background-color: #4a90e2;
            color: #ffffff;
            text-decoration: none;
            border-radius: 4px;
            font-weight: bold;
          }}

          .footer {{
            background-color: #f0f0f0;
            padding: 16px;
            text-align: center;
            font-size: 12px;
            color: #888888;
          }}

          .feature-btn {{
            display: inline-block;
            padding: 12px 24px;
            margin-top: 20px;
            background-color: #ff7369;
            color: #ffffff;
            text-decoration: none;
            border-radius: 4px;
            font-weight: bold;
          }}

          @media (max-width: 600px) {{
            .container {{
              margin: 20px;
            }}

            .content,
            .header,
            .footer {{
              padding: 16px;
            }}
          }}
        </style>
      </head>

      <body>
        <div class="container" style="text-align: center;">
          <div class="header">
            <h1>Welcome, <br> <b "font-size: 16px;"> {username} </b></h1>
          </div>
          <div class="content">
            <p style="font-size: 20px; margin: 0px;"><b>Let the BudgeIT-ing begin!!</b></p>
            <p >
              BudgeIT is a budgeting app that helps you manage your finances effectively.
                <br>
                To get started, read our features for more information. on how you can BudgeIT effectively! ^^
            </p>

            <a href="#" class="feature-btn">Features</a>
            
            <br>
            
            <p>
              this is an automated message, please do not reply to this email.
            </p>
          </div>
          <div class="footer">
            &copy; 2025 BudgeIT. All rights reserved.
          </div>
        </div>
      </body>
    </html>
        
        """.format(username=self.username)
        
        # Attach both plain text and HTML versions
        part1 = MIMEText(text_content, "plain")
        part2 = MIMEText(html_content, "html")

        message.attach(part1)
        message.attach(part2)

        # Connect to Gmail SMTP server and send email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login("santoschinkit@gmail.com", "kurh stbm drnd czut")
            server.sendmail('santoschinkit@gmail.com', self.receiver_email, message.as_string())

        print("Email sent!")
