import asyncio
import aiohttp

async def send_request(session, address):
    url = f"https://geteligibleuserrequest-xqbg2swtrq-uc.a.run.app/?address={address}"
    headers = {
        'User-Agent': 'Mozilla/5.0 ...',
        'Referer': 'https://lessfeesandgas.org/'
    }
    async with session.get(url, headers=headers) as response:
        return await response.json()

async def process_addresses(addresses):
    async with aiohttp.ClientSession() as session:
        total_addresses = len(addresses)
        for address in addresses:
            response = await send_request(session, address)
            if 'error' not in str(response).lower():
                with open('logisDYM.txt', 'a') as log_file:
                    log_message = f"Address: {address}, Response: {response}\n"
                    log_file.write(log_message)
            
            total_addresses -= 1
            print(f"Addresses remaining: {total_addresses}")  # Вывод в консоль оставшихся адресов
            await asyncio.sleep(0.001)
            
with open('wallets.txt', 'r') as file:
    addresses = [address.strip().lower() for address in file.readlines()]
    print(f"Total addresses to process: {len(addresses)}")
    

asyncio.run(process_addresses(addresses))

print("Script completed.")
