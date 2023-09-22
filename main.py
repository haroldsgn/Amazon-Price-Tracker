import requests
from bs4 import BeautifulSoup
import os
import lxml
import smtplib
from email.mime.text import MIMEText

MY_EMAIL = "teinsteim@gmail.com"
MY_PASSWORD = os.environ.get('PASSWORD')

URL = os.environ.get("AMAZON_URL")
USER_AGENT = os.environ.get("AMAZON_USER_AGENT")
ACCEPT_LANGUAGE = "en-US,en;q=0.9"

headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE
}

response = requests.get(url=URL, headers=headers)
web_page = response.text
soup = BeautifulSoup(web_page, 'lxml')
price = float(soup.select("span .a-offscreen")[0].getText().split("$")[1])
product_name = soup.title.getText().split(":")[1].strip()

message_body = f"Hey! {product_name} is below $420! Current price: ${price} buy it now here: {URL}"
message = MIMEText(message_body, _charset="utf-8")
message["Subject"] = "Product Alert - Price Drop"
message["From"] = MY_EMAIL
message["To"] = "samuelrm@outlook.es"

if price < 420:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.send_message(
            message
        )

