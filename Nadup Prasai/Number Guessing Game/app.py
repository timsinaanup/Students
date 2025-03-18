from flask import Flask, request, render_template, redirect, url_for
import random

app = Flask(__name__)
random_value = None
no_of_guess = 0
guessed_times = 0
lower_number = 0
higher_number = 0

@app.route('/', methods=['GET', 'POST'])
def home():
    global random_value, no_of_guess, guessed_times, lower_number, higher_number
    if request.method == 'POST':
        lower_number = int(request.form['lower_number'])
        higher_number = int(request.form['higher_number'])
        no_of_guess = int(request.form['no_of_guess'])
        random_value = random.randint(lower_number, higher_number)
        guessed_times = 0
        return redirect(url_for('game'))
    return render_template('home.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    global guessed_times, no_of_guess, random_value
    message = ""
    if request.method == 'POST':
        user_guess = int(request.form['guess'])
        guessed_times += 1

        if user_guess == random_value:
            message = f'Hurray! You guessed it right: {user_guess} in {guessed_times} tries!'
        elif guessed_times >= no_of_guess:
            message = f'Game Over! The right number was: {random_value}'
        elif user_guess < random_value:
            message = 'Your guess is too low! Try a higher number.'
        else:
            message = 'Your guess is too high! Try a lower number.'

    return render_template('game.html', message=message, guesses_left=no_of_guess - guessed_times, lower=lower_number, higher=higher_number)

if __name__ == '__main__':
    app.run(debug=True)
