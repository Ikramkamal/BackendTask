# Survey Backend

Simple backend structure using Flask for generating survey. It uses PostgreSQL for storage and provides RESTful endpoints for interacting with surveys. For this project, Flask was chosen for its simplicity, flexibility and extensivity which is perfect for this small size project. 

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

# Backend Architecture:
For this task, a Strategy Pattern is applied for survey generation. surveyGenerator represent a strategy context where generate_survey_from_description() strategy is defined. Using this design patterns improves the system's maintainability, extensibility (e.g: adding generate survey from template) and flexibility. This pattern ensures a clean separation of concerns and prepares the project for future growth while keeping the codebase easy to manage. The diagram bellow represent illustrate the system's backend architecture.  

<img width="1003" height="824" alt="Blank diagram" src="https://github.com/user-attachments/assets/2daaf4e3-4e04-4661-a3c7-bb69669f6637" />


# Future Improvements
* Dockerization: Due to time limitations, the Dockerization of this application has not been completed. The goal of Dockerization is to make the application easier to build and run across different environments. As a future improvement, the application will be containerized to ensure consistency, isolation, portability, and scalability.
  
* Testing: To ensure high code quality, it is important to introduce unit tests and automate the testing process using GitHub Actions or another CI/CD platform. This will help catch issues early and maintain reliability as the project evolves.
  
* Authentification: An authentication system could be added to allow users to securely log in, save their surveys within their sessions, and track their progress over time. This would enhance personalization and data security.
  
* UI/UX improvement: For the purpose of this task, the focus was primarily on the backend. As a future improvement, the user interface and user experience can be enhanced to provide a more intuitive, accessible, and visually appealing design. This would make the application easier to use and more engaging for end users.

