#!/usr/bin/env python3
"""
Configuration checker for TalentScout.
This script helps identify common setup issues.
"""

import os
import sys
from dotenv import load_dotenv

def check_environment():
    """Check environment setup."""
    print("=== Environment Check ===\n")
    
    # Check Python version
    print(f"Python version: {sys.version}")
    
    # Check if .env file exists
    env_file = ".env"
    if os.path.exists(env_file):
        print(f"✅ .env file found: {env_file}")
    else:
        print(f"❌ .env file not found: {env_file}")
        print("   Create a .env file with your GEMINI_API_KEY")
    
    # Load environment variables
    load_dotenv()
    
    # Check API key
    api_key = os.getenv('GEMINI_API_KEY')
    if api_key:
        print(f"✅ GEMINI_API_KEY found (length: {len(api_key)})")
    else:
        print("❌ GEMINI_API_KEY not found in environment")
        print("   Add GEMINI_API_KEY=your_key_here to .env file")

def check_dependencies():
    """Check if required packages are installed."""
    print("\n=== Dependencies Check ===\n")
    
    required_packages = [
        "streamlit",
        "google-generativeai", 
        "python-dotenv",
        "langchain",
        "langchain-google-genai"
    ]
    
    for package in required_packages:
        try:
            __import__(package.replace("-", "_"))
            print(f"✅ {package} is installed")
        except ImportError:
            print(f"❌ {package} is NOT installed")
            print(f"   Run: pip install {package}")

def check_files():
    """Check if required files exist."""
    print("\n=== Files Check ===\n")
    
    required_files = [
        "app.py",
        "chatbot.py", 
        "config.py",
        "utils.py",
        "requirements.txt"
    ]
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} missing")

def check_streamlit_secrets():
    """Check Streamlit secrets configuration."""
    print("\n=== Streamlit Secrets Check ===\n")
    
    try:
        import streamlit as st
        
        # Try to access secrets
        try:
            api_key = st.secrets.get("GEMINI_API_KEY")
            if api_key:
                print("✅ GEMINI_API_KEY found in Streamlit secrets")
            else:
                print("❌ GEMINI_API_KEY not found in Streamlit secrets")
                print("   Add it to your .streamlit/secrets.toml file")
        except Exception as e:
            print(f"❌ Error accessing Streamlit secrets: {e}")
            
    except ImportError:
        print("❌ Streamlit not installed")

def main():
    """Run all checks."""
    print("🔍 TalentScout Configuration Checker\n")
    
    check_environment()
    check_dependencies()
    check_files()
    check_streamlit_secrets()
    
    print("\n=== Check Complete ===")
    print("\nIf you see any ❌ errors, fix them before running the app.")

if __name__ == "__main__":
    main() 