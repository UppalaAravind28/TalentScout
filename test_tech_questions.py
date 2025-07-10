#!/usr/bin/env python3
"""
Test script to debug tech stack question generation issues.
Run this script to test the tech stack parsing and question generation.
"""

import os
import sys
from dotenv import load_dotenv

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import parse_tech_stack
from config import GEMINI_API_KEY, GEMINI_MODEL, TECH_QUESTION_PROMPT

def test_tech_stack_parsing():
    """Test the tech stack parsing function with various inputs."""
    print("=== Testing Tech Stack Parsing ===\n")
    
    test_cases = [
        "Python, SQL, AWS",
        "Python and SQL and AWS",
        "Python; SQL; AWS",
        "Python & SQL & AWS",
        "I know Python, SQL, and AWS",
        "I am proficient in Python and SQL",
        "Python\nSQL\nAWS",
        "Python, SQL",
        "Python",
        "",
        "   ",
        "Python, Python, SQL",  # Test duplicates
    ]
    
    for i, test_input in enumerate(test_cases, 1):
        result = parse_tech_stack(test_input)
        print(f"Test {i}: '{test_input}' -> {result}")

def test_gemini_connection():
    """Test if Gemini API is working."""
    print("\n=== Testing Gemini API Connection ===\n")
    
    try:
        import google.generativeai as genai
        
        # Configure Gemini
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(model_name=GEMINI_MODEL)
        
        # Test with a simple prompt
        test_prompt = "Generate 2 technical questions about Python programming."
        response = model.generate_content(test_prompt)
        
        print(f"✅ Gemini API is working!")
        print(f"Response: {response.text[:200]}...")
        return True
        
    except Exception as e:
        print(f"❌ Gemini API Error: {e}")
        print(f"API Key: {'Set' if GEMINI_API_KEY else 'Not Set'}")
        return False

def test_question_generation():
    """Test the full question generation process."""
    print("\n=== Testing Question Generation ===\n")
    
    if not test_gemini_connection():
        return
    
    try:
        from chatbot import ConversationManager
        
        # Create a conversation manager
        manager = ConversationManager()
        
        # Set up test candidate info
        manager.candidate_info = {
            "name": "Test User",
            "email": "test@example.com",
            "phone": "1234567890",
            "experience": "2",
            "position": "Software Engineer",
            "location": "New York",
            "tech_stack": ["Python", "SQL", "AWS"]
        }
        
        # Test question generation
        print("Generating questions for tech stack: Python, SQL, AWS")
        response = manager._generate_technical_questions()
        
        print(f"✅ Question generation successful!")
        print(f"Response: {response}")
        
    except Exception as e:
        print(f"❌ Question generation failed: {e}")

def main():
    """Run all tests."""
    print("🔍 TalentScout Tech Stack Question Generation Debug Tool\n")
    
    # Load environment variables
    load_dotenv()
    
    # Run tests
    test_tech_stack_parsing()
    test_gemini_connection()
    test_question_generation()
    
    print("\n=== Debug Complete ===")

if __name__ == "__main__":
    main() 