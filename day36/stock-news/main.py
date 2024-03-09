import requests
from datetime import date, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
AV_API_KEY = "AL76DPLI8DPYCRL6"
NEWS_API_KEY = "e3fcef4812b74205841775ca2f4a72da"
account_sid = "ACd378be490e791258d4c04917bcc7432b"
auth_token = "1bbdcb04c7c13a7bdef12987be82a86c"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": AV_API_KEY,
}

response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
data = response.json()
yesterday = date.today() - timedelta(days=1)
day_before = yesterday - timedelta(days=1)
yesterday_open = float(data["Time Series (Daily)"][str(yesterday)]["1. open"])
day_before_open = float(data["Time Series (Daily)"][str(day_before)]["1. open"])
if day_before_open < yesterday_open * 0.95 or day_before_open > yesterday_open * 1.05:
    print("Get News")
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

    parameters = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "pageSize" : 3
    }

    response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
    response.raise_for_status()
    data = response.json()

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

    percentage = ""
    if day_before_open / yesterday_open > 1:
        percentage = f"🔻{((day_before_open / yesterday_open) - 1) * 100}%"
    else: 
        percentage = f"🔺{(1 - (day_before_open / yesterday_open)) * 100}%"

    body = ""
    for article in data["articles"]:
        headline = article["title"]
        brief = article["description"]
        body += f"{STOCK}: {percentage}\nHeadline: {headline}\nBrief: {brief}\n\n"

    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body=body,
                        from_="+19497104345",
                        to="+59891017827"
                    )

    print(message.status)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

