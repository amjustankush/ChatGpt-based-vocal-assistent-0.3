from openai_agent import OpenAIAgent
from speech_processing import SpeechProcessing
from command_processing import CommandProcessing

class todoManager:
    def __init__(self):
        self.openai_agent = OpenAIAgent()
        self.tasks = ["buy milk", "buy chocolate", "go play football"]
        self.speech_processor = SpeechProcessing()
        self.command_processor = CommandProcessing()
        
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
        
    def handle_command(self, command):
        label = self.openai_agent.get_todo_command_label(command)
        print(f"Label: {label}, Command: {command}")
        
        if label == "add":
            self.add_to_todo_list(command)
        elif label == "list":
            self.get_todo_list()
        elif label == "remove":
            self.remove_from_to_list(command)
        else:
            self.speech_processor.speak("i couden't understood can you say it again.")    
            
    #------------------------------------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
 
    
    def add_to_todo_list(self, item):
        
        todo = self.openai_agent.generated_todo(item)
        print(f"todo to be added: {todo}")
        
        if todo:
            self.tasks.append(todo)
            self.speech_processor.speak(f"succesfully added '{todo}' to your todo list..!")
            
        for todo in self.tasks:
            print(todo)
                        
    #------------------------------------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
 
    def get_todo_list(self):
        self.speech_processor.queue("here's what's in your todo list!")
        
        for index, task in enumerate(self.tasks):
            self.speech_processor.queue(f"{index+1}: {task}")
            
        self.speech_processor.runAndWait()
        
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    #------------------------------------------------------------------------------------------------------------------------------------------------ 

    def remove_from_to_list(self, command):
        task = self.openai_agent.recognize_todo(self.tasks, command)
        
        if task not in self.tasks:
            self.speech_processor.speak("i coudent find the specified task in your to-do list. please try again.")
        else:
            self.speech_processor.speak(f"do you want to remove '{task}' from your to do list  ?")
            decistion = self .speech_processor.listen()
            decistion = self.command_processor.get_approve_deny(decistion)
            
        if decistion == "approve":
            self.tasks.remove(task)
            self.speech_processor.speak(f"i have removed '{task}' from your todo list.")
        else:
            self.speech_processor.speak(f"ok, i won't remove the '{task} from your todo list'")
            