import requests
from speech_processing import SpeechProcessing
import os
from dotenv import load_dotenv

class JokesAgent:
    def __init__(self):
        self.base_url = "https://api.api-ninjas.com/v1/jokes?limit="
        self.api_key = os.getenv("APININJA_API_KEY")
        self.speech_processing = SpeechProcessing()
        
    def handle_command(self, command):
        self.speech_processing.speak("i always have jockes to tell ! let me search inside of my machine brain...")
        
    def get_joke(self, limit = 1):
        try:
            params={
                "limit":limit
            }
            
            headers = {
                'X-Api-Key': self.api_key
            }
            
            response = requests.get(self.base_url, params=params, headers=headers)
            if response.status_code ==200:
                joke =response.json()[0]["joke"]
                return joke
            else:
                self.speech_processing.speak("sorry... I wasent able to find good joke...")
        
        except Exception as e:
            print("there was an error accessing the jokes api :", e)
            self.speech_processing.speak("sorry... I wasent able to find good joke...")
        