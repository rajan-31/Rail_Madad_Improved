from flask import Flask, request, jsonify
import joblib
from utils.image_processing import process_image
from utils.nlp_processing import process_description

app = Flask(__name__)

# Load the pre-trained models
category_model = joblib.load('models/category_prediction_model.pkl')
priority_model = joblib.load('models/priority_prediction_model.pkl')

@app.route('/process_complaint', methods=['POST'])
def process_complaint():
    data = request.json
    description = data.get('description')
    image = data.get('image')

    # Process description with NLP model
    keywords = process_description(description)

    # Process image with OCR and object detection
    text, metadata = process_image(image)

    # Prediction based on keywords and metadata
    category = category_model.predict([keywords])
    priority = priority_model.predict([metadata])

    # Create response
    response = {
        'category': category[0],
        'priority': priority[0],
        'keywords': keywords,
        'metadata': metadata
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
