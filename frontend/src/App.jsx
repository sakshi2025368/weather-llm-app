import React, { useState } from "react";
import "./App.css";

export default function App() {
  const [city, setCity] = useState("");
  const [current, setCurrent] = useState(null);
  const [forecast, setForecast] = useState([]);
  const [dark, setDark] = useState(true);

  const fetchWeather = async () => {
    try {
      const res = await fetch("http://127.0.0.1:8000/weather", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ city }),
      });
      const data = await res.json();
      console.log(data); // Check the structure of the response

      // Only keep necessary fields
      setCurrent({
        city: data.current.city,
        temperature: data.current.temperature,
        description: data.current.description,
      });
      setForecast(data.forecast);
    } catch (error) {
      console.error("Error fetching weather:", error);
    }
  };

  return (
    <div className={`app ${dark ? "dark" : ""}`}>
      {/* HEADER */}
      <header className="top-bar">
        <h1>Weather Dashboard</h1>
        <div className="search-box">
          <input
            placeholder="Search City"
            value={city}
            onChange={(e) => setCity(e.target.value)}
          />
          <button onClick={fetchWeather}>Get Wheather</button>
          <button className="mode" onClick={() => setDark(!dark)}>
            🌙
          </button>
        </div>
      </header>

      {current && (
        <>
          {/* MAIN GRID */}
          <section className="grid">
            {/* LEFT */}
            <div className="card main-card">
              <h2>{current.city}</h2>
              <div className="temp">{current.temperature}°</div>
              <p>{current.description}</p>
            </div>

            {/* RIGHT */}
            <div className="card side-card">
              <h3>Highlights</h3>
              <p>Feels like {current.temperature}°C</p>
              <p>Air quality: Good</p>
              <p>Visibility: Normal</p>
            </div>
          </section>

          {/* CHART */}
          <section className="card chart">
            <h3>Temperature Trend</h3>
            <div className="bars">
              {forecast.map((f, i) => (
                <div key={i} className="bar-wrap">
                  <div
                    className="bar"
                    style={{ height: `${f.temperature * 3}px` }}
                  />
                  <span>{f.time}</span>
                </div>
              ))}
            </div>
          </section>

          {/* FORECAST */}
          <section className="forecast">
            {forecast.map((f, i) => (
              <div key={i} className="forecast-card">
                <p>{f.time}</p>
                <h4>{f.temperature}°</h4>
                <span>{f.description}</span>
              </div>
            ))}
          </section>
        </>
      )}
    </div>
  );
}
