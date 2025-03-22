from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/hello')
def hello():
	return "<p>Hello, World!</p>"

@app.route('/chatgpt', methods=['POST'])
def chatgpt():
	data = request.get_json()
 # AskResponseGpt= {
 #   conversation_id: string;
 #   answer: string;
 #   current_state: string;
 #   thoughts: string | Thought[] | null;
 #   data_points: string[];
 #   transaction_data?: TransactionData;
 #   error?: string;
 #};
	response = {
		"conversation_id": data["conversation_id"],
		"answer": "Hello, World!",
		"current_state": "active",
		"thoughts": "I'm a bot",
		"data_points": ["hello", "world", data.get("query", "")]
	}

	return jsonify(response)

@app.route('/api', methods=['GET','POST'])
def api():
	data = request.get_json()
	return jsonify(data)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)
