from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
	return "<p>Hello, World!</p>"

@app.route('/api', methods=['GET','POST'])
def api():
	data = request.get_json()
	return jsonify(data)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)
