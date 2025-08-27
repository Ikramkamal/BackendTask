# Survey Backend

Simple backend structure using Flask for generating survey. It uses PostgreSQL for storage and provides RESTful endpoints for interacting with surveys.

# Getting Started

1. Create a virtual environment:

   ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate     # Windows
   ```

2. Install dependencies:

   ```bash
    pip3 install -r requirements.txt
   ```
3. Configure database:
   For this task, a local PostgreSQL database is used. It is important to make sure to update server.py with your PostgreSQL connection string. 
    
    ```bash
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://<username>@localhost:5432/<database>"
   ```
    Make sure your PostgreSQL server is running and database exists

4. Run server:

   ```bash
    python server.py
   ```

# Features:
* Generate survey from a description via a POST endpoint
* Save surveys description and generated questions in a PostgreSQL database
* Retrive generated questions from database for an existing description