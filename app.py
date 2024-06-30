import openai
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

openai.api_key = ' '

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    
    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=user_input,
        max_tokens=150  
    )
    
    bot_response = response.choices[0].text.strip()
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
