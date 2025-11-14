import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }  

    response = requests.post(url, json = input_json, headers=header)

    if response.status_code == 200:
        response_json = json.loads(response.text)

        # defaulting to score of 0 if not in the output but still a 200
        anger_score = emotion_dict.get('anger', 0)
        disgust_score = emotion_dict.get('disgust', 0)
        fear_score = emotion_dict.get('fear', 0)
        joy_score = emotion_dict.get('joy', 0)
        sadness_score = emotion_dict.get('sadness', 0)

        emotion_dict = response_json['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_dict, key=emotion_dict.get)

    elif response.status_code == 400:
        # All values set to None
        anger_score = disgust_score = fear_score = joy_score = sadness_score = None
        dominant_emotion = None

    else:
        # all other status values
        # TODO - handle better than throwing an error but for now... 
        raise Exception("API status code unhandled.")

    # returning a dict
    return { 'anger': anger_score, 
             'disgust': disgust_score, 
             'fear': fear_score, 
             'joy': joy_score, 
             'sadness': sadness_score, 
             'dominant_emotion': dominant_emotion }
