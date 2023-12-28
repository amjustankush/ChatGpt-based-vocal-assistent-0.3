from speech_processing import SpeechProcessing
from command_processing import CommandProcessing
from openai_agent import OpenAIAgent
from todo_manager import todoManager
from weather_agent import WeatherAgent
import time
# from jokes_agent import JokesAgent
from Findlaw_agent import FindLawAgent

#------------------------------------------------------------------------------------------------------------------------------------------------ 
# this shows the path from where it is pulling lib.
#------------------------------------------------------------------------------------------------------------------------------------------------ 
# import sys
# print(sys.path)
#------------------------------------------------------------------------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------------------------------------------------------------------------ 

class MainApp:
    def __init__(self):
        self.speech_processor = SpeechProcessing()
        self.command_processor = CommandProcessing()
        self.openai_agent = OpenAIAgent()
        self.todo_manager = todoManager()
        self.weather_agent = WeatherAgent()
        # self.jokes_agent = JokesAgent()
        self.Findlaw_agent = FindLawAgent()
        
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
        
    def run(self):
        while True:
            # command = self.speech_processor.listen_for_wakeword()
            if self.speech_processor.listen_for_wakeword():
                self.speech_processor.speak("hi ! how can i assist you today")
                
                while True:
                    
                    command = self.speech_processor.listen(timeout=5)
                    
                    if command == "":
                        break
                    elif command is not None:
                        label= self.command_processor.handle_command(command)
                        if label == "to-do-list":
                            self.todo_manager.handle_command(command)
                        elif label == "weather":
                            self.weather_agent.handal_command(command)
                        elif label == "Legal-help":
                            self.Findlaw_agent.handal_command(command)    
                        else:
                            gpt_answer = self.openai_agent.get_response(command)
                            print(f"ChatGPT Answered: {gpt_answer}")
                            self.speech_processor.speak(gpt_answer)
                    time.sleep(0.1)
            time.sleep(0.1)
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    
if __name__ == "__main__":
    app = MainApp()
    app.run()
    
