from flask import Flask, render_template, request, redirect, jsonify
import sqlite3

# Path to the SQLite database file
DB_PATH = "db/chocolate.db"

app = Flask(__name__)

# Function to query the database
def query_db(query, args=(), one=False):
    try:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute(query, args)
        rv = cursor.fetchall()
        connection.commit()
        connection.close()
        return (rv[0] if rv else None) if one else rv
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"General error: {e}")
        return []

# Home route redirects to the flavors page
@app.route('/')
def home():
    return redirect('/flavors')

# Route for displaying and adding new seasonal flavors
@app.route('/flavors', methods=['GET', 'POST'])
def flavors():
    if request.method == 'POST':
        flavor_name = request.form['flavor_name']
        availability = request.form['availability']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        
        try:
            query_db("INSERT INTO seasonal_flavors (flavor_name, availability, start_date, end_date) VALUES (?, ?, ?, ?)",
                     (flavor_name, availability, start_date, end_date))
            return redirect('/flavors')
        except Exception as e:
            return jsonify({"message": f"Error: {e}"}), 500
    
    flavors = query_db("SELECT * FROM seasonal_flavors")
    return render_template('flavors.html', flavors=flavors)

# Route for displaying and adding new ingredients to the inventory
@app.route('/ingredients', methods=['GET', 'POST'])
def ingredients():
    if request.method == 'POST':
        ingredient_name = request.form['ingredient_name']
        quantity = request.form['quantity']
        unit = request.form['unit']
        
        try:
            query_db("INSERT INTO ingredient_inventory (ingredient_name, quantity, unit) VALUES (?, ?, ?)",
                     (ingredient_name, quantity, unit))
            return redirect('/ingredients')
        except Exception as e:
            return jsonify({"message": f"Error: {e}"}), 500
    
    ingredients = query_db("SELECT * FROM ingredient_inventory")
    return render_template('ingredients.html', ingredients=ingredients)

# Route for handling customer feedback (suggestions and allergy concerns)
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        flavor_suggestion = request.form['flavor_suggestion']
        allergy_concern = request.form['allergy_concern']
        
        try:
            query_db("INSERT INTO customer_feedback (customer_name, flavor_suggestion, allergy_concern) VALUES (?, ?, ?)",
                     (customer_name, flavor_suggestion, allergy_concern))
            return redirect('/feedback')
        except Exception as e:
            return jsonify({"message": f"Error: {e}"}), 500
    
    feedbacks = query_db("SELECT * FROM customer_feedback")
    return render_template('feedback.html', feedbacks=feedbacks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
