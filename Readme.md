# Household Power Consumption Prediction 🔋⚡

This project predicts household power consumption using a **FastAPI backend** and a trained **Machine Learning model**.
The API accepts input features such as voltage, intensity, and sub-metering values, and returns a power consumption prediction.

---

## 🚀 Features

* FastAPI backend for serving predictions
* Trained ML model (e.g., regression or classification)
* REST API with `/predict` endpoint
* Interactive API docs via **Swagger UI** at `http://127.0.0.1:8000/docs`
* Easy deployment with Uvicorn

---

## 📂 Project Structure

```
project/
│── backend/
│   │── main.py
│
│── frontend/
│   │── index.html
│   │── style.css
│   │── script.js
│
│── myenv/
│── model.pkl              # Trained ML model
│── requirements.txt       # Python dependencies
│── README.md              # Documentation
```

---

## 🛠️ Installation & Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/household-power-prediction.git
   cd household-power-prediction
   ```

2. Create & activate virtual environment:

   ```bash
   python -m venv myenv
   myenv\Scripts\activate   # On Windows
   source myenv/bin/activate # On Mac/Linux
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

---

## 📡 API Endpoints

### Root

```http
GET /
```

* Returns: `"Welcome to Household Power Consumption Prediction API"`

### Predict

```http
POST /predict
```

* Request Body (JSON):

```json
{
  "global_reactive_power": 0.418,
  "voltage": 234.84,
  "global_intensity": 18.4,
  "sub_metering_1": 0.0,
  "sub_metering_2": 1.0,
  "sub_metering_3": 17.0,
  "avg_intensity_1h": 19.2,
  "avg_intensity_1d": 17.6
}
```

* Response:

```json
{
  "prediction": 4.62
}
```

---

## Example Input Values

| Feature               | Value  |
| --------------------- | ------ |
| Global Reactive Power | 0.418  |
| Voltage               | 234.84 |
| Global Intensity      | 18.4   |
| Sub Metering 1        | 0.0    |
| Sub Metering 2        | 1.0    |
| Sub Metering 3        | 17.0   |
| Avg Intensity 1h      | 19.2   |
| Avg Intensity 1d      | 17.6   |


---

## 👩‍💻 Author

**Iram Saba Khan**


