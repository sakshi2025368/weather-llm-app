# weather-llm-app
# 🌦️ Weather LLM App (React + Vite + FastAPI)

A simple **Weather Prediction Web Application** built using **React (Vite)** for the frontend and **FastAPI** for the backend. Users can enter a city name and get:

* ✅ **Current weather** (temperature & description)
* ✅ **Full-day weather overview** (extended info box)

This project was developed as part of a **technical assessment / internship task**.

---

## 📸 Application Output (Screenshots)

### 🔹 Home Screen

> User enters a city name and clicks **Get Weather**

📷 *(Insert screenshot here)*

---

### 🔹 Current Weather Result

> Shows live temperature and weather condition

📷 *(Insert screenshot here)*

---

### 🔹 Full Day Weather Overview

> Separate box showing detailed description for the day

📷 *(Insert screenshot here)*

---

## 🧱 Project Structure

```
weather-llm-app/
│
├── backend/
│   └── main.py        # FastAPI backend (Weather API)
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx    # Main React UI logic
│   │   ├── App.css    # Styling
│   │   └── main.jsx   # React entry point
│   │
│   ├── package.json   # Frontend dependencies & scripts
│   └── vite.config.js
│
└── README.md
```

---

## ⚙️ Technologies Used

### Frontend

* React (Vite)
* JavaScript (ES6)
* CSS

### Backend

* FastAPI
* Python
* OpenWeatherMap API

---

## 🚀 Step-by-Step Project Execution

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sakshi2025368/weather-llm-app.git
cd weather-llm-app
```

---

### 2️⃣ Backend Setup (FastAPI)

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn requests
uvicorn main:app --reload
```

✔ Backend runs at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

### 3️⃣ Frontend Setup (React + Vite)

```bash
cd frontend
npm install
npm run dev
```

✔ Frontend runs at: **[http://localhost:5173](http://localhost:5173)**

---

## 🔁 How the App Works (Flow)

1. User enters a **city name** in the UI
2. React sends a **POST request** to FastAPI backend
3. Backend calls **OpenWeatherMap API**
4. Weather data is processed
5. Response is sent back to frontend
6. UI displays:

   * Current temperature
   * Weather description
   * Full day weather info box

---

## 🌐 API Endpoint Used

```http
POST /weather
```

**Request Body:**

```json
{
  "city": "Pune"
}
```

**Response:**

```json
{
  "weather": {
    "city": "Pune",
    "temperature": 28,
    "description": "clear sky"
  }
}
```

---

## 🔐 CORS Configuration

CORS is enabled to allow frontend requests:

```python
allow_origins=["http://localhost:3000", "http://localhost:5173"]
```

---

## 📌 GitHub Submission Details

* **Repository URL:**
  [https://github.com/sakshi2025368/weather-llm-app](https://github.com/sakshi2025368/weather-llm-app)

* **GitHub View Access Provided To:**
  `pyaf`

---

## ✅ Conclusion

This project demonstrates:

* Frontend–Backend integration
* API handling
* Real-time weather data fetching
* Clean UI with React

✨ Thank you for reviewing this project!
