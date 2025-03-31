"""
Test script for Superagent101 AI functions
"""

import os
import sys
import asyncio
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.interface.ai_service import ai_service

async def test_ai_functions():
    """Test all AI functions to verify they're working correctly"""
    
    print("=== Testing Superagent101 AI Functions ===\n")
    
    # Check if OpenAI API key is set
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY environment variable is not set.")
        print("Please set your OpenAI API key in the .env file or environment variables.")
        return False
    
    # Configure AI service with API key
    ai_service.configure(api_key)
    
    # Test code generation
    print("Testing /code command...")
    code_prompt = "Write a Python function to calculate the factorial of a number"
    code_result = ai_service.generate_code(code_prompt)
    
    if "def factorial" in code_result.lower() and "return" in code_result.lower():
        print("✅ Code generation test PASSED")
        print(f"Sample output: {code_result[:100]}...\n")
    else:
        print("❌ Code generation test FAILED")
        print(f"Output: {code_result}\n")
        return False
    
    # Test image generation
    print("Testing /image command...")
    image_prompt = "A simple cartoon robot with a friendly face"
    image_result = ai_service.generate_image(image_prompt)
    
    if image_result and not image_result.startswith("Error"):
        print("✅ Image generation test PASSED")
        print(f"Image URL: {image_result}\n")
    else:
        print("❌ Image generation test FAILED")
        print(f"Output: {image_result}\n")
        return False
    
    # Test research function
    print("Testing /research command...")
    research_prompt = "Brief overview of quantum computing"
    research_result = ai_service.research(research_prompt)
    
    if len(research_result) > 200 and "quantum" in research_result.lower():
        print("✅ Research function test PASSED")
        print(f"Sample output: {research_result[:100]}...\n")
    else:
        print("❌ Research function test FAILED")
        print(f"Output: {research_result}\n")
        return False
    
    print("All AI function tests PASSED! ✅")
    return True

if __name__ == "__main__":
    # Run the test function
    success = asyncio.run(test_ai_functions())
    
    # Exit with appropriate status code
    sys.exit(0 if success else 1)
