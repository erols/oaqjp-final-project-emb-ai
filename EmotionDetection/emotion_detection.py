''' Module that sends user text to Emotion Detection for analysis
'''

import json
import requests

def emotion_detector(text_to_analyze):
    ''' Send user text to AI at url for analysis.
    dict returned. 
    If user sends empty string, error message is returned.
    '''
    url = 'https://sn-watson-emotion.labs.skills.network' + \
    '/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=input_json, headers=headers, timeout=10)

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        result = formatted_response['emotionPredictions'][0]['emotion']
        emotions = list(result.keys())
        scores = list(result.values())
        dominant_emotion = emotions[scores.index(max(scores))]
        result['dominant_emotion'] = dominant_emotion
        return result

    if response.status_code == 400:
        error_dict = {"anger": None, \
                    "disgust": None, 
                    "fear": None, 
                    "joy": None, 
                    "sadness": None, 
                    "dominant_emotion": None}
        return error_dict
    return "Unknown Error"
