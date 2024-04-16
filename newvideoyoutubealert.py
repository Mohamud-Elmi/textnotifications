# required libraries: pip install google-api-python-client twilio


import os
from googleapiclient.discovery import build
from twilio.rest import Client

# YouTube Data API credentials
api_key = "YOUR_YOUTUBE_API_KEY"
channel_id = "CHANNEL_ID_OF_THE_YOUTUBE_CHANNEL"

# Twilio credentials
twilio_account_sid = "YOUR_TWILIO_ACCOUNT_SID"
twilio_auth_token = "YOUR_TWILIO_AUTH_TOKEN"
twilio_phone_number = "YOUR_TWILIO_PHONE_NUMBER"
your_phone_number = "YOUR_PHONE_NUMBER"

# Initialize YouTube Data API
youtube = build("youtube", "v3", developerKey=api_key)

# Get the latest video from the channel
def get_latest_video():
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        order="date",
        maxResults=1
    )
    response = request.execute()
    latest_video = response["items"][0]
    return latest_video

# Send SMS using Twilio
def send_sms(message):
    client = Client(twilio_account_sid, twilio_auth_token)
    client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=your_phone_number
    )

# Main function
def main():
    latest_video = get_latest_video()
    video_title = latest_video["snippet"]["title"]
    video_url = f"https://www.youtube.com/watch?v={latest_video['id']['videoId']}"
    message = f"New video released: {video_title}\nWatch it here: {video_url}"
    send_sms(message)

if __name__ == "__main__":
    main()
