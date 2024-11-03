from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

if __name__ == '__main__':
    app.run(debug=True)
