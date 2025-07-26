# FleetAI Vehicle Tracking API

This project is a simple vehicle tracking API built using **FastAPI** and **SQLAlchemy**, with a simulator script that sends vehicle data periodically to the API.

---

## Project Overview

- **FastAPI app** serves as a backend API to store and update vehicle data.
- Uses **SQLAlchemy** ORM with **SQLite** for database persistence.
- Provides REST endpoints to get and update vehicle info.
- **Simulator** script mimics real-time vehicle telemetry by sending periodic updates to the API.
- CORS middleware is configured to allow access from a React frontend (running on localhost).

---

## Project Structure

- `main.py`: FastAPI application and API routes.
- `database.py`: SQLAlchemy models, DB initialization, and session management.
- `simulator.py`: Script simulating vehicle telemetry, sends data via HTTP POST to the API.

---

## Setup Instructions

### Prerequisites

- Python 3.8+
- `pip` package manager

### Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy pydantic requests
