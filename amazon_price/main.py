import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
ACCOUNT_SID = "AC4e57c1679a260ad344484a8ae3c19d77"
AUTH_TOKEN = "0959946ffd2e94366ed6725f5470aff2"

URL = "https://www.amazon.in/Fur-Jaden-Black-Waterproof-Backpack/dp/B078GLXMDY/ref=sr_1_5?crid=L4HD7IR65HL2&keywords=charging%2Bbackpack&qid=1686417127&sprefix=charging%2Bbaagpac%2Caps%2C342&sr=8-5&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8,id;q=0.7",
    "Accept-Encoding": "gzip, deflate, br"

}
response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.content, 'lxml')

price_of_the_bag = soup.find(name='span', class_='a-price-whole').text
price_of_the_bag = float(price_of_the_bag[0:len(price_of_the_bag)-1])
message = ''
if price_of_the_bag < 5001:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body=f"PRICE OF CHARGING BAG DROPPED BELOW 500!!\nCURRENT PRICE = {price_of_the_bag}\nLINK: {URL}\nKINE NE BAL",
        from_='+13613146342',
        to='+91----------'
    )
print(message)
