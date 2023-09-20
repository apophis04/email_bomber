import smtplib
import time

def send_outlook_email():
    # Outlook email configuration
    sender_email = input("Enter your Outlook email: ")
    password = input("Enter your Outlook password: ")  # App Password if 2FA is enabled

    # Recipient's email address
    recipient_email = input("Enter the recipient email: ")

    # Number of times to send the message
    num_emails = int(input("Enter the number of times to send the Outlook email: "))

    # Create a connection to the Outlook SMTP server
    smtp_server = "smtp.office365.com"
    port = 587
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)

        # Compose your email
        subject = input("Enter the Outlook Subject: ")
        body = input("Enter the message here to send via Outlook: ")

        for _ in range(num_emails):
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(sender_email, recipient_email, message)
            print(f"Outlook Email {(_ + 1)}/{num_emails} sent successfully!")

            time.sleep(5)  # Pause for 5 seconds before sending the next email, dont touch this otherwise your account gets locked by the security system

        print(f"All {num_emails} Outlook emails sent successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        server.quit()

def send_gmail_email():
    # Gmail email configuration
    sender_email = input("Enter your Gmail email: ")
    password = input("Enter your Gmail password: ")

    # Recipient's email address
    recipient_email = input("Enter the recipient email: ")

    # Number of times to send the message
    num_emails = int(input("Enter the number of times to send the Gmail email: "))

    # Create a connection to the Gmail SMTP server
    smtp_server = "smtp.gmail.com"
    port = 587
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)

        # Compose your email
        subject = input("Enter the Gmail Subject: ")
        body = input("Enter the message here to send via Gmail: ")

        for _ in range(num_emails):
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(sender_email, recipient_email, message)
            print(f"Gmail Email {(_ + 1)}/{num_emails} sent successfully!")

            time.sleep(5)  # Pause for 5 seconds before sending the next email, dont touch this otherwise your account gets locked by the security system

        print(f"All {num_emails} Gmail emails sent successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        server.quit()

# Prompt the user to select the email service
print("Choose the email service:")
print("1. Outlook")
print("2. Gmail")
choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    send_outlook_email()
elif choice == "2":
    send_gmail_email()
else:
    print("Invalid choice. Please enter '1' for Outlook or '2' for Gmail.")
