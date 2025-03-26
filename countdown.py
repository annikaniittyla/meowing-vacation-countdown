from flask import Flask, render_template, request
from datetime import datetime, timedelta
from playsound import playsound
import os

app = Flask("countdown")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/countdown', methods=['POST'])
def countdown():
    vacation_date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
    today = datetime.now().date()
    days_left = (vacation_date - today).days

    # Play sound
    for _ in range(days_left):
        playsound(os.path.abspath("meow.mp3")
)

    return render_template('countdown.html', days_left=days_left)

if __name__ == '__main__':
    app.run()

