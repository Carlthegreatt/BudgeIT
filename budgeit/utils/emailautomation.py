import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailSender:
    def __init__(self, receiver_email, username):
        self.receiver_email = receiver_email
        self.username = username

    def send_email(self):
        try:
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
              <p>
                BudgeIT is a budget tracking app that helps you manage your finances effectively.
                  <br>
                  To get started, read our terms and conditions for more information
              </p>

              
              <br>
              
              <p>
                this is an automated message, please do not reply to this email.
              </p>
            </div>
            
<div style="background-color: #f9f4f7; border-radius: 8px; margin: 32px 24px 0 24px; padding: 24px 18px; font-size: 13px; color: #6c4464; box-shadow: 0 2px 8px rgba(167, 83, 115, 0.05);">
  <h2 style="color: #a75373; font-size: 18px; margin-top: 0; margin-bottom: 12px; text-align: center;">Terms and Conditions</h2>
  <b>Use of the App</b><br>
  Budget It is intended for personal finance management and budget tracking.<br>
  You must be at least 13 years old to use this app. You agree to use Budget It only for lawful purposes and in accordance with these Terms.<br><br>
  
  <b>User Data and Privacy</b><br>
  Budget It may collect non-personal data such as spending categories, dates, and amounts to help provide better insights.<br>
  We do not share or sell any data to third parties. For educational/demo purposes, data may be stored locally and not on external servers.<br>
  We are committed to keeping your information private. However, since this app is for educational purposes, it is not intended for storing sensitive financial information.<br><br>
  
  <b>Limitations of Liability</b><br>
  Budget It is provided "as is" without warranties of any kind. We are not liable for any financial decisions made based on app data. Always double-check your records; Budget It is a tool, not a financial advisor.<br><br>
  
  <b>Intellectual Property</b><br>
  All content, features, and designs of Budget It are the property of the creators/developers. You may not reproduce, copy, or reuse any part of the app without permission.<br><br>
  
  <b>Modifications to Terms</b><br>
  We may update these Terms from time to time. Continued use of the app after changes means you accept the revised Terms.<br><br>
  
  <b>Termination</b><br>
  We reserve the right to terminate or suspend access to the app at our discretion, without notice, for conduct that violates these Terms.<br><br>
  
  <b>Contact</b><br>
  For questions or feedback, contact us at: <a href="mailto:blancaflorcarlferros@gmail.com" style="color: #d46a92; text-decoration: underline;">blancaflorcarlferros@gmail.com</a>
</div>
              <div class="footer">
              &copy; 2025 BudgeIT. All rights reserved.
            </div>
          </div>
        </body>
      </html>
          
          """.format(
                username=self.username
            )

            # Attach both plain text and HTML versions
            part1 = MIMEText(text_content, "plain")
            part2 = MIMEText(html_content, "html")

            message.attach(part1)
            message.attach(part2)

            # Connect to Gmail SMTP server and send email
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login("santoschinkit@gmail.com", "kurh stbm drnd czut")
                server.sendmail(
                    "santoschinkit@gmail.com", self.receiver_email, message.as_string()
                )

            print("Email sent!")
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
          
test = EmailSender('santoschinkit@gmail.com','emman')
test.send_email()