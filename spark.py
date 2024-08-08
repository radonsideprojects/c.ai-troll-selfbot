from characterai import aiocai, sendCode, authUser
import asyncio
import json

async def main():
    email = input('Enter your email: ')

    code = sendCode(email)

    link = input('Enter the link you received: ')

    token = authUser(link, email)
    
    discord = input('Enter your discord token: ')

    credits = {"cai": token, "discord": discord}

    with open('config.json', 'w') as file:
        file.write(json.dumps(credits))

asyncio.run(main())