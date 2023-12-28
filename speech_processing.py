import speech_recognition as sr
import pyttsx3 as tts
from openai_agent import OpenAIAgent
import time
from pygame import mixer

class SpeechProcessing:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.tts_engine = tts.init()
        self.openai_agent = OpenAIAgent()
        self.sound_file = "vocal Assistant\listen_sound.mp3"
        mixer.init()
        
        self.tts_engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
        self.tts_engine.setProperty("rate", 178)
        
    def play_sound(self):
        mixer.music.load(self.sound_file)
        mixer.music.play
        
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    # this syntax shows us the possible voice keys
    #------------------------------------------------------------------------------------------------------------------------------------------------    
        # voices = self.tts_engine.getProperty("voices")
        
        # for voice in voices:
        #     print(voice)
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    
    def listen_for_wakeword(self):
        wakeword = "wake up"
        
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration =1)
            # print("waiting for wake word...")
            try:
                # audio = self.recognizer.listen(source, timeout=5)
                # text = self.recognizer.recognize_google(audio)
                
                # if text.lower() == wakeword:
                #     print("wake word detected.") 
                return True
                
                
            except sr.WaitTimeoutError:
                print("listen timeout while waighting for phrase to start.") 
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                    print("coulden't request results from the Google Speech Recognizer Services")
            except Exception as e:
                print(f"There was an error: {e}")
            
            return False
                    

    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    
    def listen(self, timeout = 5):
        with sr.Microphone() as source:
            # print("calibrating...")
            self.recognizer.adjust_for_ambient_noise(source, timeout)
            # self.play_sound()
            print("Listening...")
            audio=None
            try:
                audio = self.recognizer.listen(source, timeout=10)
            except:
                print("Listening timeout while waiting for phrase to start")
                return ""
                
            text = ""
            try:
                print("Recognizing...")
                text = self.recognizer.recognize_google(audio)
                print(f" User said: {text}")
            except sr.UnknownValueError:
                print ("Google speech could not recognize audio")
            except sr.RequestError:
                print("coulden't request results from the Google Speech Recognizer Services")
            except Exception:
                print("There was an error")
            
            return text
        
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    
    def speak(self, text):
        self.queue(text)
        self.runAndWait()
        
    def queue(self, text):
        rephrased_text = self.openai_agent.rephrase(text)
        self.tts_engine.say(rephrased_text)
        
    def runAndWait(self):
        self.tts_engine.runAndWait()