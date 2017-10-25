import textblob
import json
from textblob import TextBlob

def analyze(event, context):
    #use when testing function
    # text = event
    #use for deployment
    text = event['body']
    blob = TextBlob(text)
    sentiment_polarity = blob.sentiment.polarity

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": text,
        "sentiment": sentiment_polarity
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
