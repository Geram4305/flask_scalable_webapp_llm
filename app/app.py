from flask import Flask, request, jsonify
import socket
from transformers import DistilBertTokenizer, TFDistilBertForSequenceClassification
import tensorflow as tf

app = Flask(__name__)

def analyze_sentiment(texts):
    try:
        texts = request.get_json()['texts']
        if not texts:
            raise ValueError('No inputs provided')
        
        # sentiment_pipeline = pipeline("sentiment-analysis",model='distilbert/distilbert-base-uncased-finetuned-sst-2-english')
        # results  = sentiment_pipeline(texts)

        # Load pre-trained DistilBERT tokenizer
        tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')

        # Load pre-trained DistilBERT model for sequence classification
        model = TFDistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')

        # Tokenize the input texts
        inputs = tokenizer(texts, return_tensors='tf', padding=True, truncation=True)

        # Perform inference on the batch
        outputs = model(inputs)

        # Get the predicted sentiment labels for each text in the batch
        predicted_labels = tf.argmax(outputs.logits, axis=1).numpy()

        # Map the predicted labels to sentiments
        sentiments = ["positive" if label == 1 else "negative" for label in predicted_labels]

        # Create a dictionary with text and its corresponding sentiment
        result = [{'text': text, 'sentiment': sentiment} for text, sentiment in zip(texts, sentiments)]
     
        return jsonify(result),200
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route("/", methods=['GET','POST'])
def home():
    if request.method == 'GET':
        text = f"Hello! Using container ID: {socket.gethostname()}. Application is up and running, send a post request to same route."
        return jsonify([{'text':text}])
    else:
        data = request.get_json()
        return analyze_sentiment(data.get('texts', []))


if __name__== "__main__":
    app.run()