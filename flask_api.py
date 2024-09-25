from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample in-memory storage
sessions = {}
orders = {}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    # Simulate session creation
    session_id = f'session_{username}'
    sessions[session_id] = {"user": username}
    return jsonify({"session_id": session_id}), 200

@app.route('/order', methods=['POST'])
def order():
    data = request.get_json()
    session_id = data.get('session_id')
    if session_id not in sessions:
        return jsonify({"error": "Invalid session id"}), 400
    # Simulate order creation
    order_id = f'order_{session_id}'
    orders[order_id] = {"session_id": session_id}
    return jsonify({"order_id": order_id}), 200

@app.route('/payment', methods=['POST'])
def payment():
    data = request.get_json()
    session_id = data.get('session_id')
    order_id = data.get('order_id')
    if session_id not in sessions or orders.get(order_id) != {"session_id": session_id}:
        return jsonify({"error": "Invalid session id or order id mismatch"}), 400
    return jsonify({"status": "payment successful"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
