import requests
from dotenv import load_dotenv
import os
from speech_processing import SpeechProcessing
from openai_agent import OpenAIAgent

load_dotenv()



class FindLawAgent:
    
    def __init__(self):
        # self.api_key = os.getenv("WEATHER_API_KEY")
        # self.base_url = "http://api.weatherapi.com/v1/current.json"
        self.openai_agent = OpenAIAgent()
        self.speech_processing = SpeechProcessing()
        self.location = "none"
        self.Practices = "none"
        
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
        
    def handal_command(self, command):
        location = self.openai_agent.extract_information("location", command)
        Practices = self.openai_agent.extract_Legal_information(command)
        
        if location == "none" or Practices == "none":
            if location == "none":
                self.get_location(command)
            elif Practices=="none":
                self.get_Practices(command)
        else:
            # weather_data = self.get_weather(location)
            # self.process_weather(weather_data)
            print(location, Practices)
            quit()

    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    
    def command_condition(self, command):
        if self.location == "none" or self.Practices == "none":
            if self.location == "none":
                self.get_location(command)
            elif self.Practices=="none":
                self.get_Practices(command)
        else:
            # weather_data = self.get_weather(location)
            # self.process_weather(weather_data)
            print(self.location, self.Practices)
            quit()

    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
        
    def get_location(self, command):
        self.speech_processing.speak("please specify the location for me to give you relavent firm result.")
        location = self.speech_processing.listen()
        location = self.openai_agent.extract_information("location", location)
        self.location = location
        print(self.location, self.Practices)
        
        if location and location != "none":
            # weather_data=self.get_weather(location)
            self.command_condition(command)
        else:
            self.speech_processing.speak("i can't find the specified location. please try again.")
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    #------------------------------------------------------------------------------------------------------------------------------------------------
     
    def get_Practices(self, command):
        self.speech_processing.speak("please specify the Practice Area for me to give you relavent firms.")
        Practices = self.speech_processing.listen()
        Practices = self.openai_agent.extract_Legal_information(command)
        self.Practices = Practices
        print(self.location, self.Practices)
        
        
        if Practices and Practices != "none":
            # weather_data=self.get_weather(Practices)
            self.command_condition(command)
        else:
            self.speech_processing.speak("i can't find the specified Practice areas. please try again.")
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    #------------------------------------------------------------------------------------------------------------------------------------------------  
    
    # def process_legal(self, data):
    #     if data:
    #         weather_message = f"Currently in {data['location']}, the weather condition is : {data['condition']}, and the temperature is : {data['temperature']} degrees."
    #         self.speech_processing.speak(weather_message)
            
    #     else:
    #         self.speech_processing.speak("I couden't retreave the weather information please try again.")
        
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
        
    # def get_legal(self, location):
    #     params = {
    #         'key': self.api_key,
    #         'q' : location,
    #         'aqi' : 'no'
    #     }
        
    #     response = requests.get(self.base_url, params=params)
        
    #     if response.status_code != 200:
    #         return None
        
    #     data = response.json()
        
    #     weather_data= {
    #         'location': data['location']['name'],
    #         'condition': data['current']['condition']['text'],
    #         'temperature': data['current']['temp_c']
    #     }
        
    #     return weather_data