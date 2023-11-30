# Import Flask and SQLAlchemy
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Create an app instance
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'

# Create a database object
db = SQLAlchemy(app)

# Define a Task model
class Task(db.Model):
    # Define the columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    done = db.Column(db.Boolean, default=False)

    # Define the representation
    def __repr__(self):
        return f'<Task {self.title}>'

# Define a route for the home page
@app.route('/')
def index():
    # Query all tasks from the database
    tasks = Task.query.all()

    # Render the index.html template with the tasks
    return render_template('index.html', tasks=tasks)

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
