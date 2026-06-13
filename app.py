from flask import Flask, render_template, request, redirect
import sqlite3
import joblib

app = Flask(__name__)

model = joblib.load(
    "models/purchase_prediction.pkl"
)

# Home Page
@app.route('/')
def home():
    return render_template('login.html')


# Register Page
@app.route('/register')
def register_page():
    return render_template('register.html')


# Register User
@app.route('/register', methods=['POST'])
def register():

    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect(
        "database/customers.db"
    )

    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users(username,password) VALUES(?,?)",
        (username, password)
    )

    conn.commit()
    conn.close()

    return redirect('/')


# Login User
@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect(
        "database/customers.db"
    )

    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cur.fetchone()

    conn.close()

    if user:
        return redirect('/dashboard')

    return "Invalid Login"


# Dashboard
@app.route('/dashboard')
def dashboard():
    return render_template(
        'dashboard.html'
    )


# Prediction Page
@app.route('/prediction')
def prediction():
    return render_template(
        'prediction.html'
    )


# Predict Purchase
@app.route('/predict', methods=['POST'])
def predict():

    customer_id = request.form['customer_id']
    age = int(request.form['age'])
    income = int(request.form['income'])
    score = int(request.form['score'])

    result = model.predict([[age, income, score]])

    prediction = (
        "Likely To Purchase"
        if result[0] == 1
        else "Not Likely To Purchase"
    )

    conn = sqlite3.connect("database/customers.db")
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO prediction_history
    (customer_id, age, income, score, prediction)
    VALUES (?, ?, ?, ?, ?)
    """,
    (customer_id, age, income, score, prediction))

    conn.commit()
    conn.close()

    return render_template(
        'result.html',
        prediction=prediction
    )


# Recommendation Page
@app.route('/recommendation', methods=['GET', 'POST'])
def recommendation():

    recommendation = ""

    if request.method == 'POST':

        income = int(request.form['income'])

        if income >= 80000:
            recommendation = "Premium Product Offer"
        elif income >= 50000:
            recommendation = "Combo Offers & Membership Plans"
        else:
            recommendation = "Discount Coupons & Cashback Offers"

    return render_template(
        'recommendation.html',
        recommendation=recommendation
    )
@app.route('/segmentation')
def segmentation():
    return render_template(
        'segmentation.html'
    )
@app.route('/reports')
def reports():
    return render_template(
        'reports.html'
    )
@app.route('/history')
def history():

    conn = sqlite3.connect("database/customers.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM prediction_history"
    )

    records = cur.fetchall()

    conn.close()

    return render_template(
        'history.html',
        records=records
    )
    
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)