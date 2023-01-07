from flask import Flask, request, render_template, redirect, session
app= Flask(__name__)

import random

app.secret_key= "I love gold"

@app.route('/')
def home():
    if 'gold' not in session:
        session['gold'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    if request.form['gold'] =="farm":
        chicken= random.randint(10, 20)
        session['gold'] += chicken 
        print("results", type(session['gold']))

    if request.form['gold'] =="cave":
        stones= random.randint(5, 10)
        session['gold'] += stones
        print("results", type(session['gold']))

    if request.form['gold'] =="house":
        chair= random.randint(2, 5)
        session['gold'] += chair
        print("results", type(session['gold']))

    if request.form['gold'] =="casino":
        money= random.randint(0, 50)
        session['gold'] += money
        print("results", type(session['gold']))

    return redirect('/')


if __name__=="__main__":     
    app.run(debug=True)