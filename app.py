from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_card():
    data = request.json
    return jsonify({
        "status": "success",
        "card_number": data.get('cardNumber'),
        "card_holder": data.get('cardHolder'),
        "card_color": data.get('cardColor')
    })

if __name__ == '__main__':
    app.run(debug=True)