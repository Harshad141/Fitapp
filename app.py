from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

workouts = []

@app.route('/')

def indexhome():

    return render_template('index.html', workouts=workouts)

@app.route('/add', methods=['POST'])

def add_workout():

    workout = request.form.get('workout')

    duration = request.form.get('duration')

    if not workout or not duration:

        return "Please enter both workout and duration.", 400

    try:

        duration = int(duration)

        workouts.append({'workout': workout, 'duration': duration})

        return redirect(url_for('home'))

    except ValueError:

        return "Duration must be a number.", 400

if __name__ == '__main__':

    app.run(debug=True)

