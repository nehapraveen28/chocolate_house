Chocolate House Management Application

A Python-based web application to manage seasonal flavor offerings, ingredient inventory, and customer flavor suggestions with allergy concerns. This application uses Flask for the backend, SQLite as the database, and is containerized with Docker

 Features
1. Seasonal Flavor Offerings:
   - View, add, and manage seasonal chocolate flavors dynamically.
2. Ingredient Inventory:
   - Manage ingredients required for chocolate production.
3. Customer Feedback:
   - Add and view customer flavor suggestions and allergy concerns.

---

 Prerequisites
1. Install Python(Version 3.9+)
   - Verify installation:
     python --version
    

2. Install Docker
   - Verify installation:
     docker --version
    

3. Install Git


 Local Setup Instructions

 1. Clone the Repository
git clone <repository_url>
cd chocolate_house


Install dependencies 
pip install -r requirements.txt


2. Set Up the Virtual Environment

python -m venv venv
source venv/bin/activate 
On Windows, use venv\Scripts\activate


4. Initialize the SQLite Database
Run the database initialization script:
python db_manager.py


5. Run the Application
Start the Flask development server:
python app.py

Home Page: http://127.0.0.1:5000


Docker Deployment Instructions
1. Build the Docker Image
From the project root directory, build the Docker image:
docker build -t chocolate-house-app .

2. Run the Docker Container
Run the Docker container with the following command:
docker run -p 5000:5000 chocolate-house-app

3. Access the Application
Open your browser and navigate to:
Home Page: http://127.0.0.1:5000





Usage Instructions

Adding Seasonal Flavors
1. Navigate to the Seasonal Flavors page.
2. Fill in the flavor details (name, availability, start date, end date).
3. Submit the form to dynamically add the flavor to the database.



Managing Ingredient Inventory
1. Navigate to the Ingredient Inventory page.
2. Add or update ingredient quantities and other details.

Adding Customer Feedback
1. Navigate to the Feedback page.
2. Enter the customer's name, flavor suggestion, and allergy concerns.
3. Submit the form to save the feedback.




Developed by: Neha Praveen 
