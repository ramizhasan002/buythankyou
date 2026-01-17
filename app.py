from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')



@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)

