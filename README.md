**Support My Work**

Hey there! 👋

I'm an independent creator working on various projects, from open-source software to content creation. If you find my work useful or enjoy what I do, consider supporting me with a virtual coffee!
Your support helps keep me fueled and motivated to continue creating and sharing. It's a small gesture that goes a long way in making a difference.

Thank you for being a part of my journey! ☕


--> [**Buy Me a Coffee ☕**](https://www.buymeacoffee.com/apophis04)


# email_bomber
Python script for sending multiple emails through Outlook and Gmail with user choice, 2FA support, and adjustable delays.

**Title:** Multi-Email Sender (Outlook and Gmail)

**Description:**

This Python script allows you to send multiple emails through both Outlook and Gmail using functions. It provides a choice between the two email services, and you can select the service you want to use before sending emails.

**Instructions:**

1. When you run the script, it will prompt you to choose an email service:
   - Enter '1' to send emails through Outlook.
   - Enter '2' to send emails through Gmail.

2. Based on your choice, the script will guide you through the email configuration process and email sending for the selected service.

**Features:**

- **Outlook Email Function:**
  - You will be asked to enter your Outlook email address and password (or App Password if 2FA is enabled).
  - Specify the recipient's email address.
  - Choose the number of times to send the email.
  - Compose the email with a subject and message.
  - Emails are sent with a 5-second delay between each email to avoid triggering security measures.

- **Gmail Email Function:**
  - You will be asked to enter your Gmail email address and password.
  - Specify the recipient's email address.
  - Choose the number of times to send the email.
  - Compose the email with a subject and message.
  - Emails are sent with a 5-second delay between each email to avoid triggering security measures.

**Usage Tips:**

- Ensure that you have enabled "Less secure app access" for Gmail if you're using Gmail as the email service.
- Use App Passwords if 2FA is enabled for Outlook or Gmail.
- Adjust the delay between emails by changing the sleep duration (e.g., `time.sleep(5)`) as needed.
- Use this script responsibly and consider the potential impact on the recipient's inbox when sending multiple emails.

**Note:**

This script provides a convenient way to send multiple emails through Outlook and Gmail. Make sure to follow the instructions and enter the required information accurately for a successful email sending experience.
