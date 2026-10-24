from flask import Flask, request, render_template_string
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

X = [
    [1, 50, 40], [2, 60, 45], [3, 70, 55],
    [4, 80, 65], [5, 90, 75], [6, 95, 85],
    [2, 75, 50], [4, 90, 70], [3, 60, 48],
    [5, 85, 78]
]
y = [35, 42, 55, 65, 78, 90, 48, 73, 50, 80]

model = LinearRegression()
model.fit(X, y)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Student Predictor</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #eef2ff;
            display: flex;
            justify-content: center;
            padding: 30px 12px;
        }
        .card {
            background: white;
            padding: 28px;
            border-radius: 18px;
            width: 100%;
            max-width: 390px;
            box-shadow: 0 8px 28px #0001;
        }
        h1 { color: #3730a3; font-size: 25px; }
        p { color: #555; }
        label { display: block; margin-top: 18px; }
        input {
            box-sizing: border-box;
            width: 100%;
            padding: 12px;
            margin-top: 7px;
            border: 1px solid #ccc;
            border-radius: 8px;
        }
        button {
            width: 100%;
            padding: 14px;
            margin-top: 24px;
            background: #4f46e5;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
        }
        .result {
            margin-top: 22px;
            padding: 15px;
            background: #ecfdf5;
            border-radius: 10px;
            color: #065f46;
        }
    </style>
</head>
<body>
<div class="card">
    <h1>🎓 AI Student Predictor</h1>
    <p>Enter your details to estimate your marks.</p>

    <form method="POST">
        <label>Daily study hours</label>
        <input type="number" name="hours"
               min="0" max="24" step="0.5" required>

        <label>Attendance (%)</label>
        <input type="number" name="attendance"
               min="0" max="100" required>

        <label>Previous marks (out of 100)</label>
        <input type="number" name="marks"
               min="0" max="100" step="0.5" required>

        <button type="submit">Predict Marks</button>
    </form>

    {% if prediction is not none %}
    <div class="result">
        <h2>Estimated Marks: {{ prediction }}/100</h2>
        <p>This is an estimate, not a guaranteed result.</p>
    </div>
    {% endif %}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        hours = float(request.form["hours"])
        attendance = float(request.form["attendance"])
        marks = float(request.form["marks"])

        result = model.predict([[hours, attendance, marks]])[0]
        prediction = round(max(0, min(100, result)), 2)

    return render_template_string(HTML, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)