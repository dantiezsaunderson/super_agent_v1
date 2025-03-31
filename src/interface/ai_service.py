"""
AI Service module for Superagent101
Handles integration with OpenAI API for various AI functions
"""

import os
import openai
from typing import Optional, List

class AIService:
    """Service class for AI-related functionality"""
    
    def __init__(self):
        """Initialize the AI service with API key from environment"""
        self.api_key = os.getenv("OPENAI_API_KEY")
        if self.api_key:
            openai.api_key = self.api_key
            self.is_configured = True
        else:
            self.is_configured = False
    
    def configure(self, api_key: str) -> bool:
        """Configure the AI service with the provided API key"""
        if not api_key:
            return False
        
        self.api_key = api_key
        openai.api_key = api_key
        self.is_configured = True
        return True
    
    def generate_code(self, prompt: str) -> str:
        """Generate code using OpenAI API"""
        if not self.is_configured:
            return "Error: OpenAI API key not configured. Please set your API key in the control panel."
        
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that generates code. Provide only the code without explanations unless specifically asked."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
                max_tokens=1500
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating code: {str(e)}"
    
    def generate_image(self, prompt: str) -> Optional[str]:
        """Generate an image using OpenAI DALL-E API"""
        if not self.is_configured:
            return "Error: OpenAI API key not configured. Please set your API key in the control panel."
        
        try:
            response = openai.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1
            )
            return response.data[0].url
        except Exception as e:
            return f"Error generating image: {str(e)}"
    
    def research(self, query: str) -> str:
        """Perform research on a topic using OpenAI API"""
        if not self.is_configured:
            return "Error: OpenAI API key not configured. Please set your API key in the control panel."
        
        try:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a research assistant. Provide comprehensive, well-structured information on the topic. Include relevant facts, context, and if appropriate, different perspectives."},
                    {"role": "user", "content": f"Research the following topic and provide detailed information: {query}"}
                ],
                temperature=0.3,
                max_tokens=2000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error performing research: {str(e)}"

# Create a singleton instance
ai_service = AIService()
