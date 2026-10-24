from sklearn.linear_model import LinearRegression

# Sample student data:
# [study hours, attendance percentage, previous marks]
X = [
    [1, 50, 40],
    [2, 60, 45],
    [3, 70, 55],
    [4, 80, 65],
    [5, 90, 75],
    [6, 95, 85],
    [2, 75, 50],
    [4, 90, 70],
    [3, 60, 48],
    [5, 85, 78]
]

# Sample marks obtained by students
y = [35, 42, 55, 65, 78, 90, 48, 73, 50, 80]

# Create and train the AI model
model = LinearRegression()
model.fit(X, y)

print("AI Student Performance Predictor")
print("--------------------------------")

hours = float(input("Daily study hours: "))
attendance = float(input("Attendance percentage: "))
previous_marks = float(input("Previous marks out of 100: "))

# Predict marks
prediction = model.predict([
    [hours, attendance, previous_marks]
])[0]

prediction = max(0, min(100, prediction))

print("\nEstimated marks:", round(prediction, 2), "/ 100")
print("This is an estimate, not a guaranteed result.")