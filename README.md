

---

# TalentScout Hiring Assistant

TalentScout is an AI-powered web application that automates the initial technical screening of job candidates. It collects candidate information, asks tailored technical questions based on the candidate’s tech stack, and stores responses for recruiters to review.

---

## Table of Contents

- [Features](#features)
- [Architecture Overview](#architecture-overview)
- [Setup & Installation](#setup--installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Extending the Project](#extending-the-project)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Features

- Conversational chatbot interface for candidate screening
- Collects essential candidate information (name, email, phone, experience, etc.)
- Parses and validates candidate tech stack
- Generates 3-5 technical questions tailored to the candidate’s skills using Google Gemini AI
- Stores candidate responses for later review (JSON and Supabase)
- User-friendly web UI built with Streamlit
- Easy to configure and extend

---

## Architecture Overview

- **Frontend/UI:** Streamlit web app (`app.py`)
- **Chatbot Logic:** Conversation management and AI integration (`chatbot.py`)
- **Configuration:** API keys, prompts, and settings (`config.py`)
- **Utilities:** Input validation, tech stack parsing, formatting (`utils.py`)
- **State Management:** Session state for multi-step conversations (`state_manager.py`)
- **Data Storage:** Candidate data saved as JSON and in Supabase
- **Testing/Debugging:** Scripts for environment and logic checks

---

## Setup & Installation

### 1. **Clone the Repository**

```bash
git clone <your-repo-url>
cd TalentScout
```

### 2. **Install Python Dependencies**

It is recommended to use Python 3.9+.

```bash
pip install -r requirements.txt
```

### 3. **Set Up Environment Variables**

- Create a `.env` file in the project root (if not using Streamlit secrets).
- Add your Google Gemini API key:

  ```
  GEMINI_API_KEY=your_gemini_api_key_here
  ```

- Alternatively, add your API key to `.streamlit/secrets.toml`:

  ```
  GEMINI_API_KEY = "your_gemini_api_key_here"
  ```

### 4. **Supabase Configuration (Optional)**

- The app is pre-configured to use a Supabase database for storing user data.
- Update the `url` and `key` in `config.py` with your own Supabase project credentials if needed.

### 5. **Run the Application**

```bash
streamlit run app.py
```

- The app will be available at [http://localhost:8501](http://localhost:8501) by default.

---

## Configuration

- **API Keys:** Store your Gemini API key in `.env` or `.streamlit/secrets.toml`.
- **Supabase:** Update credentials in `config.py` if you want to use your own database.
- **Prompts and Messages:** Customize system prompts, question templates, and closing messages in `config.py`.

---

## Usage

1. **Start the App:** Open the web interface in your browser.
2. **Begin Conversation:** Click "Start Conversation" in the sidebar.
3. **Follow Prompts:** The assistant will sequentially ask for your name, email, phone, experience, position, location, and tech stack.
4. **Answer Technical Questions:** After providing your tech stack, the assistant will generate and ask 3-5 relevant technical questions.
5. **End Conversation:** You can end the conversation at any time by typing "exit", "quit", "bye", or "end".
6. **Review & Export:** Candidate data and responses are saved for recruiter review.

---

## Project Structure

```
TalentScout/
│
├── app.py                  # Main Streamlit app (UI and flow)
├── chatbot.py              # Chatbot logic and conversation management
├── config.py               # Configuration, prompts, API keys, Supabase
├── utils.py                # Utility functions (validation, parsing, formatting)
├── state_manager.py        # Streamlit session state management
├── requirements.txt        # Python dependencies
├── .env                    # (Optional) Environment variables
├── .streamlit/
│   └── secrets.toml        # Streamlit secrets (API keys)
├── user_data/              # Saved candidate data (JSON)
├── test_tech_questions.py  # Test script for tech stack/question generation
├── check_config.py         # Environment and setup checker
└── README.md               # Project documentation
```

---

## Extending the Project

- **Add More Candidate Fields:** Update `REQUIRED_INFO` and `INFO_PROMPTS` in `config.py`.
- **Change/Expand Technical Questions:** Modify the `TECH_QUESTION_PROMPT` in `config.py`.
- **Integrate with Other Databases:** Replace or extend the `store_user_data` function in `config.py`.
- **Customize UI:** Edit `app.py` and the embedded CSS for a different look and feel.

---

## Troubleshooting

- **Missing Dependencies:**  
  Run `pip install -r requirements.txt` to install all required packages.

- **API Key Issues:**  
  Ensure your Gemini API key is set in `.env` or `.streamlit/secrets.toml`.

- **Supabase Errors:**  
  Check your Supabase credentials in `config.py`.

- **Check Setup:**  
  Run `python check_config.py` to verify your environment and configuration.

- **Debugging Tech Stack Parsing/Questions:**  
  Run `python test_tech_questions.py` to test parsing and question generation.

---

## License

[MIT License] (or your chosen license)

---

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Google Gemini](https://ai.google.dev/)
- [Supabase](https://supabase.com/)

---

**For further questions or support, contact the project maintainer or open an issue in the repository.**

---

