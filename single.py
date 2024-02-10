# use this code if you want to check only one email

import asyncio
import nest_asyncio
from verify_email import verify_email

nest_asyncio.apply()

async def verify_email_address(email):
    result = await asyncio.to_thread(verify_email, email)
    if result == True:
        print(f"The email address '{email}' is valid.")
    elif result == False:
        print(f"The email address '{email}' is invalid.")
    else:
        print(f"Unable to verify the email address '{email}'. Error: {result}")

# change "example@example.com" by the email you want to check 

async def main():
    email_to_verify = "example@example.com"
    await verify_email_address(email_to_verify)

if __name__ == "__main__":
    asyncio.run(main())
