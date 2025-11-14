"""
Flask application providing endpoints for emotion detection and home page.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def text_to_detect():
    """
    Detect emotions in the text provided via the `textToAnalyze` query parameter.

    Returns a formatted string showing the emotion scores and the dominant
    emotion, or an error message if the input is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Using implicit string concatenation with parentheses thus the leading spaces
    # Note the BOLD for dominant emotion. TODO - Styling should done in the template or CSS.
    return ("For the given statement, the system response is"
            f" 'anger': {response['anger']}," 
            f" 'disgust': {response['disgust']},"
            f" 'fear': {response['fear']},"
            f" 'joy': {response['joy']} and"
            f" 'sadness': {response['sadness']}."
            f" The dominant emotion is <b>{dominant_emotion}</b>."
        )

@app.route("/")
def render_index_page():
    """
    Render and return the main index page. Simple.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
