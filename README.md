# Amazon-Price-Tracker
A Python Project that keeps an eye on the price of your favorite Amazon product.

# Features
- Retrieves the current price of a product on Amazon.
- Monitors the product's price and sends an email notification when it drops below a specified threshold.
- Uses BeautifulSoup for web scraping and smtplib for sending email notifications.

# Usage
Set up your environment variables:
- AMAZON_URL: The URL of the Amazon product you want to track.
- AMAZON_USER_AGENT: Your user agent string.
- PASSWORD: Your email account password.
- Run the script to start tracking the product's price. If the price drops below the specified threshold (e.g., $420), you will receive an email notification.
