Initialize Database
Before starting the API server, initialize the database by running:

python
Copy
Edit
from main import init_db

init_db()
Or run a script that calls init_db().

Run API Server
bash
Copy
Edit
uvicorn main:app --reload
This will start the server on http://127.0.0.1:8000.

Run Simulator
In a separate terminal, run:

bash
Copy
Edit
python simulator.py
This script sends vehicle updates every 5 seconds to the API.

API Endpoints
GET /: Root endpoint, returns a welcome message.

GET /vehicles/: Returns a list of all vehicles.

POST /vehicles/: Adds or updates a vehicle entry.

Vehicle JSON Schema
json
Copy
Edit
{
  "vehicleId": "string",
  "model": "string",
  "latitude": 0.0,
  "longitude": 0.0,
  "speed": 0.0,
  "engineTemp": 0.0,
  "isFaulty": true
}
How It Works (Detailed Explanation)
1. FastAPI Application (main.py)
Defines a Vehicle Pydantic model to validate incoming JSON data.

Sets up CORS middleware to allow React app origins.

Maintains an in-memory list vehicles_db as sample data storage.

Implements GET /vehicles/ to return all vehicles.

Implements POST /vehicles/ to add or update vehicles in vehicles_db.

2. Database Setup (database.py)
Uses SQLAlchemy to define a VehicleDB model that maps to a SQLite database table vehicles.

Provides init_db() to create tables based on model definitions.

Provides get_db() generator to create and close database sessions for API dependency injection (not wired up in the current API code but ready for integration).

3. Simulator Script (simulator.py)
Continuously generates random vehicle telemetry data.

Sends the data as a POST request to the FastAPI /vehicles/ endpoint every 5 seconds.

Simulates latitude/longitude changes, speed, engine temperature, and fault status.

Prints status of each data transmission attempt.

Next Steps / Improvements
Integrate the SQLAlchemy database with FastAPI routes for persistent storage.

Add GET/POST routes that interact with the database instead of in-memory list.

Add authentication and authorization.

Add more vehicle attributes or history logging.

Create a React frontend to consume this API and visualize vehicle data in real-time.

Contact
For questions, reach out to hannahpriyanka2603@gmail.com.

yaml
Copy
Edit

---

# Explanation of the Code

### `main.py` — FastAPI Application

- **FastAPI app instance** is created.
- **CORS middleware** is configured to allow requests from your React frontend at `localhost:3000`.
- Defines a Pydantic model `Vehicle` to enforce request/response data schema.
- Maintains a sample list `vehicles_db` with example vehicles.
- Routes:
  - `/` — Simple root route returning a welcome message.
  - `/vehicles/` (GET) — Returns the list of vehicles.
  - `/vehicles/` (POST) — Updates an existing vehicle in the list or adds a new one.

Currently, this only works with the in-memory list `vehicles_db`, so data resets when the app restarts.

---

### `database.py` — Database Models and Session

- Defines SQLAlchemy engine for a local SQLite file named `vehicles.db`.
- `VehicleDB` is the SQLAlchemy ORM class representing the `vehicles` table.
- `init_db()` creates the SQLite tables if they don’t exist.
- `get_db()` is a generator function to get a session for database queries — intended for dependency injection with FastAPI routes, but not yet integrated in `main.py`.

---

### `simulator.py` — Data Simulator

- Runs an infinite loop generating random telemetry for one vehicle (`V001`).
- Sends this data as JSON to the FastAPI endpoint `/vehicles/` using the Python `requests` library.
- Waits 5 seconds before sending the next update.
- This simulates real-time vehicle tracking data being sent to your API.

---

If you want, I can help you next to **connect your FastAPI app to the database** so vehicles pe
