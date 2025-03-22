from flask import Flask, request, jsonify, send_from_directory

from semantickernelcompletion import completion

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/hello')
def hello():
	return "<p>Hello, World!</p>"

@app.route('/chatgpt', methods=['POST'])
async def chatgpt():
	data = request.get_json()
	query = data.get("query", "")
	print(f"Query: {query}")
	answer = await completion(query)
	print(f"Answer: {answer}")
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
		"answer": answer,
		"current_state": "active",
		"thoughts": "I'm a bot",
		"data_points": [query]
	}
	print(f"Response: {response}")
	return jsonify(response)

@app.route('/api', methods=['GET','POST'])
def api():
	data = request.get_json()
	return jsonify(data)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)
