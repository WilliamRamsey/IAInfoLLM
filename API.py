from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/Client/Chat.html', methods=['GET'])
def chat_page():
    with open("Client/Chat.html") as html_file:
        return html_file.read()

@app.route("/API/get_response", methods=['POST', 'GET'])
def get_agent_response():
    user_message = request.form.get("user_message")
    return jsonify({"response": user_message})

@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({"status": "API is working"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)