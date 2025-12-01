# Store Operations Microservice

This microservice is designed to manage store-level data for a retail company. It allows for managing store profiles, inventory, and sales data via RESTful API endpoints.

## Key Features
- **Store Profile Management**: View and manage information about each store.
- **Inventory Management**: Fetch store-level inventory details.
- **Sales Reporting**: Push daily sales data from the point-of-sale system.
- **Microservice Architecture**: Designed to work in a distributed system with other services.

## Tech Stack
- **Backend**: FastAPI (Python)
- **Database**: Azure SQL Database
- **Web Server**: Uvicorn (for development), Gunicorn (for production)
- **ORM**: SQLAlchemy (Optional, for complex queries)
- **Authentication**: OAuth2 with JWT Tokens
- **Testing**: pytest
- **Containerization**: Docker (Optional for deployment)

## Endpoints
### `/stores/`
- **Method**: GET
- **Description**: Fetch all store profiles.
- **Response Example**:
```json
[
  {
    "store_id": 101,
    "store_name": "Amsterdam Central Store",
    "region": "EU-West",
    "status": "Active"
  }
]
```
## Getting Started
### Prerequisites

Ensure you have the following installed:
Python 3.8 or higher
Azure SQL Database (for database)
Docker (optional, for containerized setup)

### Installation

Clone the repository:
git clone https://github.com/your-username/store-operations-service.git
cd store-operations-service

### Create a virtual environment and activate it:

python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


## Install dependencies:
pip install -r requirements.txt
Create a .env file in the root directory and add your database credentials:
DB_SERVER=yourserver.database.windows.net
DB_NAME=StoreDB
DB_USER=dbadmin
DB_PASSWORD=YourPassword123

## Running the Application
To run the application in development mode:
uvicorn app.main:app --reload
To run the application in production (using Gunicorn):
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app

## Running Tests
You can run the unit tests using pytest: 
pytest

## Docker Setup (Optional)
To run the app in a Docker container, use the following commands:
Build the Docker image:
docker build -t store-operations-service .

## Run the container:
docker run -p 8000:8000 store-operations-service
Environment Variables
Add your environment variables (for database connection) to the .env file:
DB_SERVER=yourserver.database.windows.net
DB_NAME=StoreDB
DB_USER=dbadmin
DB_PASSWORD=YourPassword123

## Troubleshooting
Error 500 (Internal Server Error): Check the database connection string and ensure that your database is accessible.
Error 404: Make sure the endpoint exists, and that you're using the correct URL.

## License
This project is licensed under the MIT License - see the LICENSE
file for details.




