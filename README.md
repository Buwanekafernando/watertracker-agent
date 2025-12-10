# Water Tracker Agent

An AI-powered water intake tracker that helps you stay hydrated with personalized feedback.

## Features
- **Interactive Dashboard**: Log your water intake and view history.
- **AI Feedback**: Get personalized hydration advice powered by Google Gemini.
- **API Support**: Backend API for logging and retrieving data.

## Prerequisites
- Python 3.8+
- Google Gemini API Key

## Installation

1.  **Clone the repository** (if you haven't already).
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Set up Environment Variables**:
    - Create a `.env` file in the root directory.
    - Add your Gemini API key:
        ```env
        GEMINI_API_KEY=your_api_key_here
        ```

## Running the Application

### 1. Run the Dashboard (Frontend)
To use the interactive web interface:
```bash
streamlit run dashboard.py
```

### 2. Run the API (Backend)
To start the FastAPI backend:
```bash
uvicorn src.api:app --reload
```
The API will be available at `http://127.0.0.1:8000`.
Docs: `http://127.0.0.1:8000/docs`

## Project Structure
- `dashboard.py`: Streamlit frontend application.
- `src/agent.py`: AI agent logic (Gemini integration).
- `src/api.py`: FastAPI backend endpoints.
- `src/database.py`: SQLite database management.
