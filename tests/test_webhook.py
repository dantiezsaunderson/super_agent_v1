import unittest
import json
import asyncio
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

# Import the FastAPI app and application from your project
import sys
sys.path.append('/home/ubuntu')
from main import app
from src.interface.telegram_bot import application

class TestTelegramWebhook(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        # Create a mock for the update_queue
        self.mock_queue = MagicMock()
        self.mock_queue.put = MagicMock()
        # Replace the real queue with our mock
        application.update_queue = self.mock_queue

    def test_root_endpoint(self):
        """Test that the root endpoint returns the correct status message."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "Super Agent is webhook-ready"})

    def test_webhook_endpoint_valid_update(self):
        """Test that the webhook endpoint accepts valid Telegram updates."""
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
                "date": 1617123456,
                "text": "/start"
            }
        }
        
        # Send the update to the webhook endpoint
        with patch('main.application.update_queue.put', new=asyncio.coroutine(MagicMock())) as mock_put:
            response = self.client.post(
                "/webhook",
                json=update_data
            )
            
            # Check that the response is successful
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {"ok": True})
            
            # Check that the update was put into the queue
            mock_put.assert_called_once()

    def test_webhook_endpoint_invalid_json(self):
        """Test that the webhook endpoint handles invalid JSON gracefully."""
        # Send invalid JSON to the webhook endpoint
        response = self.client.post(
            "/webhook",
            data="This is not JSON",
            headers={"Content-Type": "application/json"}
        )
        
        # Check that the response indicates an error
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity

if __name__ == '__main__':
    unittest.main()
