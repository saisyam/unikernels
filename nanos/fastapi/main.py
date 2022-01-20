from fastapi import FastAPI

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = FastAPI()
sid_obj = SentimentIntensityAnalyzer()


def get_sentiment(sentence):
    sentiment_dict = sid_obj.polarity_scores(sentence)
    sentiment = ""
 
    if sentiment_dict['compound'] >= 0.05 :
        sentiment = "positive"
    elif sentiment_dict['compound'] <= - 0.05 :
        sentiment = "negative"
    else :
        sentiment = "neutral"
    return {
        "sentiment": sentiment
    }

@app.get("/")
async def index():
    return {
        "message":"Sentiment Analysis using Vader and FastAPI"
    }

@app.post("/sentiment")
async def sentiment(sentence: str):
    return get_sentiment(sentence)