# 🛡️ CyberGuard AI

### Cybersecurity Intelligence Assistant

CyberGuard AI is a specialized AI-powered cybersecurity assistant designed to help users understand cyber threats, improve digital safety, and learn cybersecurity best practices.

Unlike a general-purpose chatbot, CyberGuard AI focuses specifically on **Cybersecurity and Digital Safety**.

---

## 🌐 Overview

CyberGuard AI provides an intelligent conversational interface where users can ask cybersecurity-related questions and receive clear, structured, and defensive guidance.

The application combines:

- 🐍 Python
- 🎈 Streamlit
- 🦜 LangChain
- 🤖 OpenAI API

to create a modern AI-powered cybersecurity assistant.

---

## ✨ Features

### 🛡️ Cybersecurity-Focused AI

CyberGuard AI specializes in:

- Cybersecurity Fundamentals
- Threat Awareness
- Phishing Detection
- Social Engineering Awareness
- Password Security
- Multi-Factor Authentication
- Malware Awareness
- Ransomware Awareness
- Digital Privacy
- Secure Browsing
- Email Security
- Account Protection
- Network Security Fundamentals
- Web Security Concepts
- Security Best Practices

---

### 🚫 Domain Restriction

CyberGuard AI is designed specifically for cybersecurity.

If a user asks an unrelated question, the assistant responds with:

> 🛡️ Please ask a question related to Cybersecurity. CyberGuard AI specializes in Cybersecurity and Digital Safety.

This makes CyberGuard AI a specialized domain assistant rather than a general-purpose chatbot.

---

### 🔑 API Key Authentication

Users enter their OpenAI API key when launching the application.

The API key is stored temporarily in the Streamlit session and is used to connect the application with the language model.

---

### 💬 Conversational Memory

The application maintains conversation history during the active session.

Users can:

- Ask multiple questions
- Continue a cybersecurity discussion
- View previous messages
- Clear the conversation

---

### 🎨 Modern User Interface

CyberGuard AI includes:

- Dark cybersecurity-inspired interface
- Centered AI welcome screen
- Modern API key connection page
- Cybersecurity capability cards
- ChatGPT-style chat experience
- Responsive Streamlit layout

---

## 🏗️ System Architecture

```text
                ┌──────────────────┐
                │      User        │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │   CyberGuard AI  │
                │    Streamlit UI  │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │    LangChain     │
                │ Message Handling │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │   System Prompt  │
                │ Domain Guardrail │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │    OpenAI LLM    │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Cybersecurity AI │
                │     Response     │
                └──────────────────┘
```

---

## 🧠 How It Works

### Step 1 — Launch CyberGuard AI

The user opens the application.

### Step 2 — Connect OpenAI API

The user enters their OpenAI API key.

### Step 3 — Ask a Question

Example:

```text
What is phishing?
```

### Step 4 — Domain Validation

The system prompt ensures that CyberGuard AI focuses only on:

- Cybersecurity
- Digital Safety
- Privacy
- Online Threats
- Defensive Security

### Step 5 — AI Response

The LangChain application sends the conversation to the language model and displays the response.

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/cyberguard-ai.git
```

### 2. Navigate to the Project

```bash
cd cyberguard-ai
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
streamlit run app.py
```

---

## 🧪 Example Questions

### 🔍 Threat Awareness

```text
What is ransomware?
```

### 📧 Phishing Detection

```text
How can I identify a phishing email?
```

### 🔐 Password Security

```text
How can I create a strong password?
```

### 🌐 Digital Privacy

```text
How can I protect my privacy online?
```

### 🛡️ Account Security

```text
What is multi-factor authentication?
```

---

## ⚠️ Safety & Ethics

CyberGuard AI is designed for:

- Cybersecurity education
- Digital safety awareness
- Defensive security practices
- Threat awareness

The application promotes ethical and authorized cybersecurity practices.

It should not be used for unauthorized access or malicious activities.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core Programming Language |
| Streamlit | User Interface |
| LangChain | LLM Integration |
| OpenAI API | AI Model |
| Session State | Conversation Memory |

---

## 🔮 Future Improvements

- 🔍 Advanced Threat Analyzer
- 📧 Suspicious Email Analysis
- 📊 Cyber Risk Score
- 📁 Security Report Generation
- 🧠 Persistent Conversation Memory
- 📄 Cybersecurity Knowledge Base
- 🔎 RAG-Based Security Assistant
- 🌐 Security News Integration

---

## 📸 Application Flow

```text
User
  ↓
Enter OpenAI API Key
  ↓
Launch CyberGuard AI
  ↓
Ask Cybersecurity Question
  ↓
LangChain Processes Conversation
  ↓
OpenAI Model Generates Response
  ↓
CyberGuard AI Displays Answer
```

---

## 👨‍💻 Author

**Asad Ashraf**

Software Engineering Student | AI & Machine Learning Enthusiast

---

## ⭐ Support

If you like this project, consider giving the repository a ⭐ on GitHub.

---

## 📜 License

This project is created for educational and learning purposes.
