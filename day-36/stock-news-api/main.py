import requests
import smtplib

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
ALPHAVANTAGE_API = "NFGD7ODFI8UW1R6P"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "ef873a8351004ebea3ca315f4a5b02e4"

MY_EMAIL = "mauriciolearningpython@gmail.com"
MY_PERSONAL_EMAIL = "mauriciomatos44@gmail.com"
MY_PASSWORD = "b483MM4nJD+#ZIT"



stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHAVANTAGE_API
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_data = stock_data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)

percent_difference = (difference / yesterday_closing_price) * 100

if percent_difference >= 5:

    news_parameters = {
        "apikey": NEWS_API,
        "qInTitle": COMPANY_NAME
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data["articles"]
    three_articles = articles[:3]


    for article in three_articles:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                msg=f"Subject:{article['title']}\n\n{article['description']}",
                from_addr=MY_EMAIL,
                to_addrs=MY_PERSONAL_EMAIL)
