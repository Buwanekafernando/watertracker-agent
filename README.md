# Water Tracker Agent

An AI-powered water intake tracker that helps you stay hydrated and manage weight with personalized feedback.

## What’s new (Updated)

* **Height Input**: Added height field to the dashboard for BMI calculations.
* **Health Metrics**: Dashboard now displays **BMI**, **BMI Category** (Underweight, Normal, Overweight, Obese), and **Ideal Weight Range** based on height.
* **Visuals for BMI**: A progress bar visualizes BMI status and indicates how close the user is to a healthy range.
* **Enhanced AI Feedback**: The agent provides tailored advice on weight management, hydration benefits, and a recommended drinking schedule (timed reminders / intake pacing).
* **Modern Layout**: Streamlit wide layout with a sidebar for user profile settings (name, age, height, weight, activity level, unit preferences).
* **Visual Metrics**: Large metric cards showing **Daily Goal**, **Today's Intake**, and **Streak** (consecutive days meeting goal).
* **Charts**: Interactive bar chart showing hydration history (daily intake for the last X days) and weekly trends.
* **Styling**: Custom fonts and color tokens for a more attractive UI and consistent branding.
* **AI Insights Section**: Dedicated area where the AI agent (Gemini) provides insights, summaries, and next steps.

---

## Features

* Interactive Streamlit dashboard to log water intake and view history.
* Health calculations (BMI and weight-range guidance) and visual indicators.
* AI-driven personalized feedback using Google Gemini.
* Backend FastAPI for logging and retrieving user data and hydration history.
* Local SQLite storage for lightweight usage; easily swap to Postgres/MySQL.

## Prerequisites

* Python 3.8+
* Google Gemini API Key

## Installation

1. **Clone the repository** (if you haven't already).
2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Set up Environment Variables**:

* Create a `.env` file in the root directory.
* Add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

* (Optional) Add UI customization variables if used by your app (e.g. `CUSTOM_FONT`, `THEME_COLOR`).

## Running the Application

### 1. Run the Dashboard (Frontend)

To use the interactive Streamlit UI (wide layout, sidebar, charts):

```bash
streamlit run dashboard.py --server.headless true
```

### 2. Run the API (Backend)

To start the FastAPI backend:

```bash
uvicorn src.api:app --reload
```

The API will be available at `http://127.0.0.1:8000`.
Docs: `http://127.0.0.1:8000/docs`

## Quick Usage

1. Open the dashboard in your browser after running Streamlit.
2. Use the sidebar to enter profile settings: **Name**, **Age**, **Height**, **Weight**, **Activity Level**, and **Unit** (metric/imperial).
3. The app automatically computes **BMI**, displays the **BMI Category**, and shows the **Ideal Weight Range**.
4. Log sips or bottles from the dashboard. Visual cards update: **Daily Goal**, **Today's Intake**, and **Streak**.
5. Check the **AI Insights** panel for personalized hydration and weight-management suggestions.

## Project Structure

* `dashboard.py` — Streamlit frontend application (sidebar, metrics cards, charts, BMI visuals, AI Insights).
* `src/agent.py` — AI agent logic and Gemini integration (prompts, summarization, actionable tips).
* `src/api.py` — FastAPI backend endpoints for logging/retrieving intake and user profile.
* `src/database.py` — SQLite database management and helper functions.
* `src/models.py` — Pydantic models / database schemas (if present).
* `requirements.txt` — Python dependencies (Streamlit, FastAPI, Uvicorn, requests, python-dotenv, sqlite-utils / sqlalchemy, etc.).

## Styling & Theming

The dashboard includes custom fonts and color variables. Edit the constants in `dashboard.py` (or a dedicated `theme.py`) to adjust brand colors and fonts.

## AI / Gemini Notes

* The agent uses your `GEMINI_API_KEY` to request personalized feedback. Ensure your key has the required permissions and is loaded from the `.env`.
* The AI provides hydration schedules (e.g., suggested amounts and timings), weight-management advice that is general and informational — not a substitute for professional medical guidance.

## Extensibility

* Swap SQLite for a production-grade database (Postgres, MySQL) by updating `src/database.py`.
* Add authentication (OAuth2) to protect API endpoints and link user profiles across devices.
* Add push notifications or scheduled background jobs (e.g., Celery / APScheduler) to send drinking reminders.

## License

Choose a license (e.g. MIT) and add a `LICENSE` file if you plan to open-source the project.


