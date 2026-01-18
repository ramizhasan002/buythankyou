from flask import Flask, render_template, request, redirect, url_for, jsonify
import razorpay

app = Flask(__name__)



RAZOR_KEY_ID = "rzp_test_S59LriCOpEr9fW"
RAZOR_KEY_SECRET = "glUCJRauGXUONjdJx312euAM"

client = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create_order', methods=['POST'])
def create_order():
    data = request.get_json()
    amount = float(data.get('amount', 0))
    order_amount = int(amount * 100)  # in paise
    order = client.order.create({
        "amount": order_amount,
        "currency": "INR",
        "payment_capture": 1
    })
    return jsonify({
        "order_id": order['id'],
        "key": RAZOR_KEY_ID,
        "amount": order_amount
    })

@app.route('/verify_payment', methods=['POST'])
def verify_payment():
    data = request.get_json()
    params_dict = {
        'razorpay_payment_id': data['razorpay_payment_id'],
        'razorpay_order_id': data['razorpay_order_id'],
        'razorpay_signature': data['razorpay_signature']
    }
    try:
        client.utility.verify_payment_signature(params_dict)
        return jsonify({"status": "success"})
    except:
        return jsonify({"status": "failed"})


@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/refund')
def refund():
    return render_template('refund.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
