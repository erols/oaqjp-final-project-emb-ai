from flask import Flask, render_template, requests
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("\emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(textToAnalyze)
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    dominant = emotions['dominant_emotion']

    return f"For the given statement, the system response is 'anger': {anger}, \
        'disgust': {disgust}, \
        'fear': {fear}, \
        'joy': {joy} and \
        'sadness: {sadness}. \
        The dominant emotion is {dominant}."

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ = "__main__":
    app.run(host="0.0.0.0", port="5000")