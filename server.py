''' Initiate the Emotion Detector Flask app. The app detects the emotion of user text. 
The app will be served on localhost:5000 
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    '''gets user text, forwards for emotion detection and 
    returns emotions and dominant emotion in a dict
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    dominant = emotions['dominant_emotion']

    if dominant is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is 'anger': {anger}, \
        'disgust': {disgust}, \
        'fear': {fear}, \
        'joy': {joy} and \
        'sadness: {sadness}. \
        The dominant emotion is <b>{dominant}</b>."

@app.route("/")
def render_index_page():
    '''renders the homepage
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
