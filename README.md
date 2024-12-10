# Amazon Price Tracker  

This Python project tracks the price of an Amazon product and sends an email alert when the price drops below a specified threshold. Using `BeautifulSoup` for web scraping and `smtplib` for email notifications, this tool allows users to monitor price changes effortlessly.  

To set up the project, start by installing Python 3.x and the required libraries (`requests`, `beautifulsoup4`, and `python-dotenv`).
Clone the repository, install the dependencies, and create a `.env` file to store sensitive information like SMTP credentials securely. The `.env` file should have the following format:  

```
SMTP_ADDRESS="your_smtp_server"  
EMAIL_ADDRESS="your_email"  
EMAIL_PASSWORD="your_email_password"  
```  

Replace the placeholder Amazon product URL in the script with your desired product link and set your target `BUY_PRICE`. Run the script, and it will scrape the product page, retrieve the current price, and notify you via email if the price is below your threshold.  

This project demonstrates the integration of web scraping and email automation while prioritizing secure handling of credentials. Use responsibly, as web scraping can violate website terms of service.
