# 🗄️ Text-to-SQL AI

Convert natural-language questions into SQL queries and get easy-to-understand answers using **Google Gemini, LangChain, SQLite, and Streamlit**.

## 📌 Overview

Text-to-SQL AI allows users to interact with an e-commerce database using plain English instead of writing SQL manually.

The application uses an LLM to generate SQL queries from user questions, executes them against an SQLite database, and converts the results into natural-language responses.

## ✨ Features

- **Natural Language to SQL:** Generate SQL queries from everyday questions.
- **AI-Powered Responses:** Convert query results into clear, natural-language answers.
- **Interactive Chat Interface:** Ask questions through Streamlit's chat interface.
- **Conversation History:** View previous questions and answers during the current session.
- **Clear Chat:** Reset the conversation history.
- **SQLite Database:** Query structured e-commerce data.
- **Docker Support:** Package the application for consistent deployment.
- **AWS Deployment Ready:** Deploy the containerized application on AWS EC2.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Interactive web interface |
| LangChain | LLM integration and output parsing |
| Google Gemini | SQL generation and natural-language responses |
| SQLite | Database storage and query execution |
| Docker | Application containerization |
| AWS EC2 | Cloud deployment |

## 🏗️ Architecture

```text
User Question
     ↓
Streamlit Chat Interface
     ↓
Google Gemini + LangChain
     ↓
SQL Query Generation
     ↓
SQLite Database Execution
     ↓
Query Result
     ↓
Google Gemini + LangChain
     ↓
Natural-Language Answer
     ↓
Display Answer in Chat
```

## 🗃️ Database Schema

The application uses four related tables:

- **customers:** Customer details, city, state, and signup date.
- **products:** Product names, categories, and unit prices.
- **orders:** Order dates, statuses, and payment methods.
- **order_items:** Products purchased, quantities, and selling prices.

### Table Relationships

```text
customers ──< orders ──< order_items >── products
```

Revenue can be calculated using:

```sql
SUM(quantity * selling_price)
```

## 📂 Project Structure

```text
TexttoSQl/
├── app.py
├── database.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

The `.env` file contains your Gemini API key and should remain local. The SQLite database is generated locally and is excluded from Git.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Badala2306/TexttoSQl.git
cd TexttoSQl
```

### 2. Create a Virtual Environment

```bash
python -m venv env
```

Activate it on Windows:

```powershell
.\env\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API Key

Create a `.env` file in the project root:

```text
GOOGLE_API_KEY=your_gemini_api_key
```

Obtain an API key through [Google AI Studio](https://aistudio.google.com/).

### 5. Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, usually `http://localhost:8501`.

## 🐳 Run with Docker

Build the Docker image:

```bash
docker build -t text-to-sql-ai .
```

Run the container:

```bash
docker run --name text-to-sql-app --env-file .env -p 8501:8501 -v "${PWD}/ecommerce.db:/app/ecommerce.db" text-to-sql-ai
```

Open `http://localhost:8501` in your browser.

The database volume helps preserve the SQLite database outside the container. Ensure your `database.py` uses the expected database path.

## 💡 Example Questions

Try asking:

- What are the top 3 products by revenue?
- Which city has the most customers?
- How many orders are completed?
- What is the total revenue from completed orders?
- Which product category generates the highest revenue?
- Which customers have placed the most orders?

## ☁️ Deployment

The application can be containerized using Docker and deployed on AWS EC2.

For deployment, configure the server, install Docker, supply the Gemini API key securely, and expose the Streamlit port through the EC2 security group.

## 🔒 Security Notes

- Never commit API keys or `.env` files to GitHub.
- The current implementation is a learning project; generated SQL is executed against the database.
- Before public deployment, add robust SQL validation, restrict database permissions, and protect the application against unintended queries.

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Large Language Model (LLM) integration
- Prompt engineering for SQL generation
- Natural-language data querying
- Relational databases and SQL joins
- LangChain output parsing
- Streamlit session-state management
- Docker containerization and cloud deployment

## 👨‍💻 Author

**Manan Badala**

GitHub: [Badala2306](https://github.com/Badala2306)

---

*Built to make database querying more accessible through natural language and generative AI.*
