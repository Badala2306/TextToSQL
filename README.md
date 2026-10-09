# Text-to-SQL AI

An AI-powered application that converts natural-language questions into SQL queries using Google Gemini, LangChain, and SQLite.

## 🚀 Live Demo

**[Try Text-to-SQL AI](https://texttosql-93z5.onrender.com)**

## ✨ Features

- Convert natural-language questions into SQL queries.
- Generate SQL using Google Gemini.
- Execute queries against a SQLite database.
- Display query results in a Streamlit interface.
- Maintain chat history during a session.
- Run the application using Docker.

## 🛠️ Tech Stack

- **Language:** Python
- **Frontend:** Streamlit
- **LLM:** Google Gemini
- **LLM Framework:** LangChain
- **Database:** SQLite
- **Containerization:** Docker
- **Deployment:** Render

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Badala2306/TexttoSQl.git
cd TexttoSQl
```

### 2. Create a virtual environment

```bash
python -m venv env
```

Activate it on Windows:

```powershell
.\env\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r Requirements.txt
```

### 4. Configure the Gemini API key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Replace the placeholder with your own API key. Never upload `.env` to GitHub.

### 5. Initialize the database

Ensure `ecommerce.db` and its required tables are initialized with your sample data before running the application.

### 6. Start the application

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

## 🐳 Run with Docker

Ensure Docker Desktop is running and your `.env` file is configured.

### Build the Docker image

```bash
docker build -t text-to-sql-ai .
```

### Run the container

```bash
docker run -d --name text-to-sql-app --env-file .env -p 8501:8501 -v "${PWD}/ecommerce.db:/app/ecommerce.db" text-to-sql-ai
```

Open `http://localhost:8501`.

> Ensure the database file exists and contains the required tables before starting the container.

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `GOOGLE_API_KEY` | API key for Google Gemini |

Store API keys in your local `.env` file or your deployment provider's environment settings. Never commit secrets to source control.

## 🌐 Deployment

The application is deployed on Render using Docker.

**Live URL:** https://texttosql-93z5.onrender.com

## 🔮 Future Improvements

- Add robust SQL validation and read-only query execution.
- Improve database schema discovery and error handling.
- Support additional databases.
- Add query explanations and downloadable results.
- Improve the interface and user experience.

## 👨‍💻 Author

**Manan Badala**

- [GitHub](https://github.com/Badala2306)
- [Portfolio](https://manan-badala.vercel.app/)
