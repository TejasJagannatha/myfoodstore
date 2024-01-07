from flask import Flask, render_template

app = Flask(__name__)

@app.route('/indian_bhojana')
def index():
    # Sample data
    title = "Flask Template Example"
    message = "Welcome to Flask Templates!"

    # Render the template and pass variables
    return render_template('landing.html', title=title, message=message)

if __name__ == '__main__':
    app.run(debug=True)
