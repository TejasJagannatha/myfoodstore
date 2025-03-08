from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/indian_bhojana' , methods= ['GET', 'POST'])
def index():
    # Sample data
    # Render the template and pass variables
    return render_template('landing.html')

if __name__ == '__main__':
    app.run()
