# use this code if you want to check bulk emails

import asyncio
import nest_asyncio
from verify_email import verify_email

nest_asyncio.apply()

async def verify_email_address(email):
    result = await asyncio.to_thread(verify_email, email)
    return email if result == True else None

async def main():
    valid_emails = []
    with open('emails.txt', 'r') as file:
        emails = file.readlines()

    for email in emails:
        email = email.strip()  # Remove leading/trailing whitespace and newlines
        valid_email = await verify_email_address(email)
        if valid_email:
            valid_emails.append(valid_email)
            with open('valid_emails.txt', 'a') as output_file:
                output_file.write(valid_email + '\n')
            print(f"Valid email address '{valid_email}' has been written to 'valid_emails.txt'.")
        else:
            print(f"Invalid email address '{email}'.")

    print("All emails processed.")

if __name__ == "__main__":
    asyncio.run(main())
