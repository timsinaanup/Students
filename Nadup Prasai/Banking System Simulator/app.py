from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Global variable to store account data
account = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/create_account', methods=['POST'])
def create_account():
    global account
    name = request.form.get('name')
    try:
        balance = float(request.form.get('balance'))
        if balance < 0:
            return jsonify({"error": "Starting balance cannot be negative."}), 400
    except ValueError:
        return jsonify({"error": "Invalid balance input."}), 400
    
    account = {"name": name, "balance": balance}
    return jsonify({"message": f"Account created for {name} with balance {balance:.2f}"})

@app.route('/deposit', methods=['POST'])
def deposit():
    global account
    try:
        amount = float(request.form.get('amount'))
        if amount <= 0:
            return jsonify({"error": "Deposit amount must be greater than 0."}), 400
        account['balance'] += amount
        return jsonify({"message": f"{amount:.2f} deposited successfully!", "balance": account['balance']})
    except ValueError:
        return jsonify({"error": "Invalid amount input."}), 400

@app.route('/withdraw', methods=['POST'])
def withdraw():
    global account
    try:
        amount = float(request.form.get('amount'))
        if amount <= 0:
            return jsonify({"error": "Withdrawal amount must be greater than 0."}), 400
        if amount > account['balance']:
            return jsonify({"error": "Insufficient balance!"}), 400
        account['balance'] -= amount
        return jsonify({"message": f"{amount:.2f} withdrawn successfully!", "balance": account['balance']})
    except ValueError:
        return jsonify({"error": "Invalid amount input."}), 400

@app.route('/check_balance', methods=['GET'])
def check_balance():
    global account
    if not account:
        return jsonify({"error": "No account found."}), 400
    return jsonify({"name": account['name'], "balance": account['balance']})

if __name__ == '__main__':
    app.run(debug=True)
