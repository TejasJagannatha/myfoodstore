from app import app
from flask import Flask, render_template,request

@app.route('/join', methods=['GET', 'POST'])
def hire():
    # Sample data
    if request.method == 'POST':
        name = request.form['name']
        mob= request.form['mob']
        email= request.form['email']
        address= request.form['add']
        data_json= {'name' : name, 'mob' : mob, 'email' : email, 'address' :address}
        return render_template('hiring.html')
    else:
        return render_template('landing.html')