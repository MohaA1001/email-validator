# Email-validator
check if email address is valid or not

# Bulk Email validator / Bulk Email Verification Tool

This tool allows you to verify bulk email addresses efficiently. You can use it to check a list of email addresses stored in a file named emails.txt. The tool will verify each email address and output the valid ones to a file named valid_emails.txt.

# Prerequisites
Before using this tool, ensure you have the following:

Python 3 installed on your system.
The **verify_email** package installed. 
**You can install it using** 
`pip install verify_email`

# How To Use It
1) install **verify_email** package using `pip install verify_email`
2) in **emails.txt** Add all email addresses you want to verify, each on a new line.
3) to start: `python bulk.py`
> If you want to verify just one email ignore 2, 3 and only run `python single.py` after editing the email in it

# Notes

This script utilizes asyncio for concurrent execution, which enhances performance for bulk verification. However, please be aware of rate limits imposed by email verification services.

Always respect the privacy and policies of email verification services and the privacy of individuals whose email addresses you are verifying.

# Credits

This tool uses the **verify_email** package for email verification.

This code I made using [ChatGPT 3.5](https://chat.openai.com)

> This code is For educational purposes only
