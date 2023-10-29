from flask import Flask, render_template, request, jsonify
import openai

# Initialize the Flask application
app = Flask(__name__)

# Configure OpenAI API key
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']

    openai_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a tax assistant.Only answer questions related to tax.Give an error message if the user asks something else."},
            {"role": "user", "content": user_message}
        ]
    )
    response = openai_response.choices[0].message['content']

    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True)
