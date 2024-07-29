from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import logging

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def mock_openai_response():
    return {
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": "This is a mock response due to quota limits."
                }
            }
        ]
    }

@app.route('/api/validate-experiment', methods=['POST'])
def validate_experiment():
    try:
        data = request.get_json()
        logging.debug(f"Received data: {data}")
        params = data.get('params')
        api_key = data.get('apiKey')

        if not params or not api_key:
            logging.error("Missing parameters or API key.")
            return jsonify({"error": "Experimental parameters or API key not provided"}), 400

        openai.api_key = api_key
        logging.debug(f"Using OpenAI API key: {api_key}")

        prompt = f"Validate the following experimental design:\n{params}"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an AI that validates experimental designs."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=100
            )
            result = response.choices[0].message['content'].strip()
        except Exception as e:
            logging.warning(f"API call failed, using mock response. Error: {e}")
            response = mock_openai_response()
            result = response['choices'][0]['message']['content']

        logging.debug(f"Generated result: {result}")
        return jsonify({"result": result})
    except Exception as e:
        logging.error(f"Error generating result: {e}")
        return jsonify({"error": "Failed to generate result"}), 500

if __name__ == '__main__':
    app.run(debug=True)