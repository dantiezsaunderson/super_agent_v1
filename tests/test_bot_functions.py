import unittest
from unittest.mock import patch, MagicMock
import json
import os

class TestTelegramBotFunctions(unittest.TestCase):
    """Test the core functionality of the Telegram bot."""
    
    def setUp(self):
        """Set up test environment before each test."""
        # Import here to avoid import errors when module is loaded
        import sys
        sys.path.append('/home/ubuntu')
        from src.interface.telegram_bot import TelegramInterface
        
        self.interface = TelegramInterface()
        
        # Create mock update and context objects
        self.update = MagicMock()
        self.context = MagicMock()
        
        # Set up message mock
        self.message_mock = MagicMock()
        self.update.message = self.message_mock
        self.message_mock.reply_text = MagicMock()
    
    async def test_start_command(self):
        """Test the /start command response."""
        await self.interface.start(self.update, self.context)
        self.message_mock.reply_text.assert_called_once()
        args, _ = self.message_mock.reply_text.call_args
        self.assertIn("Hello", args[0])
    
    async def test_help_command(self):
        """Test the /help command response."""
        await self.interface.help_command(self.update, self.context)
        self.message_mock.reply_text.assert_called_once()
        args, _ = self.message_mock.reply_text.call_args
        self.assertIn("/start", args[0])
        self.assertIn("/help", args[0])
        self.assertIn("/code", args[0])
    
    async def test_code_command_with_args(self):
        """Test the /code command with arguments."""
        # Set up context with arguments
        self.context.args = ["print('Hello World')"]
        
        await self.interface.code_command(self.update, self.context)
        self.message_mock.reply_text.assert_called_once()
        args, _ = self.message_mock.reply_text.call_args
        self.assertIn("Here's your generated code", args[0])
        self.assertIn("print('Hello", args[0])
    
    async def test_code_command_without_args(self):
        """Test the /code command without arguments."""
        # Set up context with no arguments
        self.context.args = []
        
        await self.interface.code_command(self.update, self.context)
        self.message_mock.reply_text.assert_called_once()
        args, _ = self.message_mock.reply_text.call_args
        self.assertIn("Here's your generated code", args[0])
        self.assertIn("print('Hello", args[0])
    
    async def test_handle_message_with_code_keyword(self):
        """Test handling a message containing the 'code' keyword."""
        # Set up message text
        self.message_mock.text = "Can you write some code for me?"
        
        await self.interface.handle_message(self.update, self.context)
        self.message_mock.reply_text.assert_called_once()
        args, _ = self.message_mock.reply_text.call_args
        self.assertIn("Here's your generated code", args[0])
    
    async def test_handle_message_without_keywords(self):
        """Test handling a message without recognized keywords."""
        # Set up message text
        self.message_mock.text = "Hello there!"
        
        await self.interface.handle_message(self.update, self.context)
        self.message_mock.reply_text.assert_called_once()
        args, _ = self.message_mock.reply_text.call_args
        self.assertIn("Sorry, I didn't understand", args[0])

if __name__ == '__main__':
    unittest.main()
