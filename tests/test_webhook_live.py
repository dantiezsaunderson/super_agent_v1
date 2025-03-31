import requests
import json
import os
import time

def test_webhook_with_real_request():
    """
    Send a real HTTP request to test the webhook endpoint.
    This simulates Telegram sending an update to your webhook.
    
    Note: This requires your FastAPI service to be deployed and accessible.
    """
    # Replace with your actual deployed webhook URL
    webhook_url = "https://super-agent-api.onrender.com/webhook"
    
    # Sample Telegram update data
    update_data = {
        "update_id": 123456789,
        "message": {
            "message_id": 123,
            "from": {
                "id": 987654321,
                "first_name": "Test",
                "username": "testuser"
            },
            "chat": {
                "id": 987654321,
                "first_name": "Test",
                "username": "testuser",
                "type": "private"
            },
            "date": int(time.time()),
            "text": "/help"
        }
    }
    
    # Send the update to the webhook endpoint
    try:
        response = requests.post(
            webhook_url,
            json=update_data,
            headers={"Content-Type": "application/json"}
        )
        
        # Print the response details
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 200:
            print("✅ Webhook test successful!")
            return True
        else:
            print("❌ Webhook test failed!")
            return False
    except Exception as e:
        print(f"❌ Error testing webhook: {str(e)}")
        return False

def test_telegram_api_getme():
    """
    Test the Telegram Bot API directly using the getMe method.
    This verifies that your bot token is valid and the bot is operational.
    """
    token = os.getenv("TELEGRAM_BOT_TOKEN", "8046986752:AAHWFX9PCJlZjUJoHIevV5a45SeaoqVajAw")
    url = f"https://api.telegram.org/bot{token}/getMe"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(data, indent=2)}")
        
        if response.status_code == 200 and data.get("ok"):
            print("✅ Bot API test successful!")
            print(f"Bot username: @{data['result']['username']}")
            return True
        else:
            print("❌ Bot API test failed!")
            return False
    except Exception as e:
        print(f"❌ Error testing Telegram API: {str(e)}")
        return False

def test_webhook_info():
    """
    Check the current webhook settings for your bot.
    This verifies that the webhook is properly configured.
    """
    token = os.getenv("TELEGRAM_BOT_TOKEN", "8046986752:AAHWFX9PCJlZjUJoHIevV5a45SeaoqVajAw")
    url = f"https://api.telegram.org/bot{token}/getWebhookInfo"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(data, indent=2)}")
        
        if response.status_code == 200 and data.get("ok"):
            if data["result"].get("url"):
                print(f"✅ Webhook is set to: {data['result']['url']}")
                return True
            else:
                print("❌ No webhook URL is set!")
                return False
        else:
            print("❌ Failed to get webhook info!")
            return False
    except Exception as e:
        print(f"❌ Error checking webhook info: {str(e)}")
        return False

if __name__ == "__main__":
    print("=== Testing Telegram Bot API ===")
    test_telegram_api_getme()
    
    print("\n=== Checking Webhook Configuration ===")
    test_webhook_info()
    
    print("\n=== Testing Webhook with Simulated Update ===")
    test_webhook_with_real_request()
