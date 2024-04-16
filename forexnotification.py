# pip install requests twilio
import requests
from twilio.rest import Client

# Alpha Vantage API credentials
alpha_vantage_api_key = "YOUR_ALPHA_VANTAGE_API_KEY"

# Twilio credentials
twilio_account_sid = "YOUR_TWILIO_ACCOUNT_SID"
twilio_auth_token = "YOUR_TWILIO_AUTH_TOKEN"
twilio_phone_number = "YOUR_TWILIO_PHONE_NUMBER"
your_phone_number = "YOUR_PHONE_NUMBER"

# Function to get forex price
def get_forex_price():
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=EUR&to_currency=USD&apikey={alpha_vantage_api_key}"
    response = requests.get(url)
    data = response.json()
    return float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])

# Function to send SMS using Twilio
def send_sms(message):
    client = Client(twilio_account_sid, twilio_auth_token)
    client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=your_phone_number
    )

# Main function
def main():
    threshold_price = 1.15  # Example threshold price
    current_price = get_forex_price()
    if current_price > threshold_price:
        message = f"EURUSD price has passed {threshold_price}. Current price: {current_price}"
        send_sms(message)

if __name__ == "__main__":
    main()
