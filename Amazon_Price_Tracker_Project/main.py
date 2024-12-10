from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

example_url = " https://www.amazon.com/JBL-Eco-Bluetooth-Built-Waterproof/dp/B0BT38Q1BB?ref=dlx_deals_dg_dcl_B0BT38Q1BB_dt_sl14_3e"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(example_url, headers=header)

soup = BeautifulSoup(response.content, "html.parser")
print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()

price_without_currency = price.split("$")[1]

price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 30

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{example_url}".encode("utf-8")
        )