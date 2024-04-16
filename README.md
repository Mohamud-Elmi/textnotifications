# text notifications
Required Libraries: 
pip install google-api-python-client twilio
pip install requests twilio


Forex Notification:
This script fetches the real-time exchange rate for EURUSD from the Alpha Vantage API and compares it with a predefined threshold price. If the current price exceeds the threshold, it sends an SMS notification using Twilio with the current price information. You can adjust the threshold_price variable to set your desired price point for the notification.

Youtube Alert:
This script will fetch the latest video from the specified YouTube channel using the YouTube Data API and then send a text message to your phone using Twilio with the title and URL of the latest video. 
