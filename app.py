from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

base_url = "https://api.aimlapi.com/v1"
api_key = "0d0db946de674eceb283396486977868"
system_prompt = "A user will give you symptoms and you role is to respond back with a ecofriendly solution to help there health problem"
user_prompt = "Tell me about San Francisco"

api = OpenAI(api_key=api_key, base_url=base_url)
@app.route('/')
def home():
    return "Hello"

@app.route('/analyze', methods=['POST'])
def analyze():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    symptoms = data.get('symptoms', '')  

    try:
        response = api.chat.completions.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "system", "content":system_prompt},
                {"role": "user", "content": f"The user has the following symptoms: {symptoms}. What could this mean, and what should they do?"},
            ],
            max_tokens=100,  
            temperature=0.7,  
        )
        health_insights = response.choices[0].message.content.strip()
    except Exception as e:
        health_insights = f"An error occurred: {str(e)}"

    return jsonify({
        'symptoms': symptoms,
        'health_insights': health_insights,
    })

if __name__ == '__main__':
    app.run(debug=True)