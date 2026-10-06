# 🤖 AI Investment Allocation Assistant

An AI-powered investment allocation assistant built using **FastAPI, LangGraph, Groq, and LLMs**.

The application collects a user's investment profile and uses a LangGraph workflow to generate educational asset-allocation guidance across stocks, bonds, and cash, followed by diversified ETF suggestions.

> ⚠️ **Disclaimer:** This project is for educational purposes only and does not provide personalized financial, investment, tax, or legal advice. Investment decisions should be made after consulting a qualified financial professional.

---

## 🚀 Features

* 👤 User investment profile collection
* 🤖 LLM-powered asset allocation
* 📊 Stock / Bond / Cash allocation
* 💼 ETF recommendations
* 🔗 LangGraph multi-step workflow
* ⚡ FastAPI backend
* 🎨 Interactive web UI
* 🔐 Environment-based API key management
* 📖 FastAPI Swagger documentation

---

## 🏗️ Architecture

```text
User
 │
 ▼
FastAPI Web Interface
 │
 ▼
LangGraph Workflow
 │
 ├── Collect User Profile
 │
 ▼
Suggest Asset Allocation
 │
 ▼
Groq LLM
 │
 ▼
Recommend ETFs
 │
 ▼
Final Investment Insights
```

---

## 🧠 LangGraph Workflow

The application contains three main nodes:

### 1. `collect_profile`

Collects the user's:

* Age
* Investment goal
* Investment horizon
* Risk tolerance

### 2. `suggest_allocation`

Uses the user's profile and an LLM to generate an educational allocation across:

* Stocks
* Bonds
* Cash

The allocation is required to total 100%.

### 3. `recommend_assets`

Maps the suggested asset allocation to suitable diversified ETF options.

The model considers:

* ETF ticker
* Fund name
* Expense ratio
* Diversification
* Long-term suitability

---

## 🛠️ Tech Stack

| Technology          | Purpose                   |
| ------------------- | ------------------------- |
| Python              | Core programming          |
| FastAPI             | Backend API               |
| LangGraph           | AI workflow orchestration |
| LangChain           | LLM integration           |
| Groq                | LLM inference             |
| HTML/CSS/JavaScript | Frontend                  |
| Jinja2              | HTML templates            |
| Pydantic            | Request validation        |
| python-dotenv       | Environment variables     |

---

## 📁 Project Structure

```text
AI-Investment-Allocation-Assistant/
│
├── app.py              # FastAPI application
├── config.py           # Groq/LLM configuration
├── collector.py        # User profile node
├── suggest.py          # Asset allocation node
├── rec.py              # ETF recommendation node
├── requirements.txt    # Python dependencies
├── .gitignore
├── README.md
│
└── templates/
    └── index.html      # Web interface
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Investment-Allocation-Assistant.git
```

```bash
cd AI-Investment-Allocation-Assistant
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv name
```

Activate it:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file:

```text
GROQ_API_KEY=your_groq_api_key
```

Do not commit the `.env` file.

---

## ▶️ Run the Application

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Open the application:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 📊 Example User Profile

```text
Age: 30
Goal: Retirement
Investment Horizon: 25 years
Risk Tolerance: Medium
```

The application processes this profile through the LangGraph workflow and produces:

```text
User Profile
     ↓
Asset Allocation
     ↓
ETF Recommendations
     ↓
Educational Explanation
```

---

## 🔐 Environment Variables

The following environment variable is required:

```text
GROQ_API_KEY
```

Example:

```text
GROQ_API_KEY=your_api_key_here
```

Never expose your API key in source code or commit it to GitHub.

---

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

* Generative AI application development
* LLM integration
* LangGraph workflows
* Prompt engineering
* FastAPI API development
* Frontend/backend integration
* Environment variable management
* AI-powered recommendation systems
* Multi-step AI agents

---

## 🔮 Future Improvements

Potential improvements include:

* Structured JSON output from the LLM
* Portfolio visualization
* Interactive allocation charts
* User authentication
* Persistent user profiles
* Database integration
* More sophisticated risk profiling
* Market-data integration
* ETF data validation
* Docker deployment
* Cloud deployment

---

## 👨‍💻 Author

**Anuj Tembhurne**

AI / Machine Learning / Generative AI Enthusiast

---

## ⚠️ Disclaimer

This application is an educational software project. The generated asset allocations and ETF examples should not be considered personalized financial advice or guaranteed investment recommendations.
