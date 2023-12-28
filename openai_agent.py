import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAIAgent:
    
    def __init__(self, model= "gpt-3.5-turbo"):
        self.model = model
        self.memory = []
        self.memory_limit = 10
    
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
        
    def chat_Completion_method(self, messages):
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=messages
        )
        return completion["choices"][0]["message"]["content"]
    
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    #------------------------------------------------------------------------------------------------------------------------------------------------ 

    
    def get_response(self, command):
        
        messages=[
            {"role":"system", "content":"you are a vocal assistant. you have to answer in a simple, efficient and concise way. your answer should not take more than 30 seconds to say out loud"}
        ]
        messages.extend(self.memory)
        messages.append(
            {"role":"user", "content":command}
        )
        
        
        assistant_reply = self.chat_Completion_method(messages)
        
        if assistant_reply:
            self.memory.extend([
                {"role":"user", "content":command},
                {"role": "assistant", "content": assistant_reply}
            ])
            self.memory = self.memory[-self.memory_limit:]
            
        return assistant_reply
    
    #------------------------------------------------------------------------------------------------------------------------------------------------    
    #------------------------------------------------------------------------------------------------------------------------------------------------ 

    def get_command_label(self, command):
        
        messages=[
                {"role":"system", "content":"you are a vocal assistant."},
                {"role":"system", "content":"your role is to classify the user's command and return only the corresponding label."},
                {"role":"system", "content":"the labels are : to-do-list, weather, normal question, legal-help."},
                {"role":"system", "content":"if you recognize the user's command as a to-do list request (for example), then return to-do-list"},
                {"role":"system", "content":"if you recognize the user's command as a legal help request (for example), then return Legal-help nothing more."},
                {"role":"system", "content":"if you recognize the user's had an incident that can be helped with the legal process(for example), then return Legal-help nothing more."},
                {"role":"user", "content":command}
            ]
        
        label =self.chat_Completion_method(messages)
        return label
    
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    
    def get_todo_command_label(self,command):
        
        messages =[
            {"role":"system", "content":"you are a vocal assistant."},
            {"role":"system", "content":"you must classify the following command for a todo list functionality, choose between one of these labels"},
            {"role":"system", "content":"the possible labels are : add, remove, list, none"},
            {"role":"system", "content":"for example if the user says 'i want to go running tomorrow at 10 am', return add"},
            {"role":"user", "content":command}
        ]
        label =self.chat_Completion_method(messages)
        return label
    
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    
    def generated_todo(self, command):
        messages =[
            {"role":"system", "content":"you are a vocal assistant."},
            {"role":"system", "content":"user is trying to add the task to there todo list, and your job is to format there task into a concise task."},
            {"role":"system", "content":"for example if the user says 'i need to buy milk at 5 pm', you should refrase it as 'buy milk at 5 pm'."},
            {"role":"system", "content":"ignore any word that are not part of the task itself."},
            {"role":"user", "content":command}
        ]
        
        todo = self.chat_Completion_method(messages)
        return todo
    
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    def get_approve_deny(self, command):
        messages =[
            {"role":"system", "content":"you are an assistant tasked with classifying user responses."},
            {"role":"system", "content":"the user will approve and deny the proposal."},
            {"role":"system", "content":"determine whether the user approves or deny a praposal."},
            {"role":"system", "content":"return 'approve' or 'deny'."},
            {"role":"user", "content":command}
        ]
        
        decision = self.chat_Completion_method(messages)
        return decision
    
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    #------------------------------------------------------------------------------------------------------------------------------------------------ 

    def recognize_todo(self, tasks, command):
        messages =[
            {"role":"system", "content":"your task is to match the user's command to one of the element of a todo list."},
            {"role":"system", "content":"the user wants to remove the specific task from his to do list."},
            {"role":"system", "content":"identify the task from user and return it."},
            {"role":"system", "content":"if you find the task that matches his request them should return the exact task text, nothing more. else return 'none'"},
            {"role":"user", "content":command}
        ]
        
        for index, task in enumerate(tasks):
            messages.append(
                {"role":"system", "content":f"{index+1}: {task}"}
            )
            
        messages.append(
            {"role":"user", "content":command}
        )
        
        todo = self.chat_Completion_method(messages)
        return todo
    
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    
    def extract_information(self, info, command):
        messages =[
            {"role":"system", "content":"you are an AI assistent tasked with extracting specific information from users command."},
            {"role":"system", "content":f"extraxt the following detail: {info}"},
            {"role":"system", "content":f"if the user's message contain any '{info}', return only the detail."},
            {"role":"system", "content":f"if the user's message doesn't contain any '{info}', return only 'none'"},
            {"role":"system", "content":f"remember, your response should only contain {info} or 'none', nothing more."},
            {"role":"user", "content":command}
        ]
        
        extract = self.chat_Completion_method(messages)
        return extract
    
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    
                                       
    def extract_Legal_information(self, command):
        messages =[
            {"role":"system", "content":"you are an AI assistant tasked to help attorneys extract specific information from user command."},
            {"role":"system", "content":f"extract the following detail: related legal practice area for lawyers."},
            {"role":"system", "content":f"if the user's message is related to any legal practice area return that practice area."},
            {"role":"system", "content":f"if the user's message doesn't relate to any legal practice area return 'none'."},
            {"role":"system", "content":f"remember, your response should only contain a practice area or 'none', nothing else."},
            {"role":"system", "content":f"for non practice area message return only 'none' nothing else"},
            {"role":"user", "content":command}
        ]
        
        extract = self.chat_Completion_method(messages)
        return extract
    
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    #------------------------------------------------------------------------------------------------------------------------------------------------ 
    
    
    def rephrase(self,text):
        messages =[
            {"role":"system", "content":"you are an helpfull rephrasing assistant. you need to rephase a vocal assistant message in a diffrent, yet equivalent way."},
            {"role":"system", "content":"you should keep the same meaning and average name but change the structure and words if possible."},
            {"role":"system", "content":"gpt should try to avoid using uncommon or complicated words in the rephrawsed version, keep it simple."},
            {"role":"system", "content":"keep in mind the text should be simple and concise, and shouldn't take more than 20 seconds to say out loud."},
            {"role":"user", "content":text}
        ]
        
        rephrased_command = self.chat_Completion_method(messages)
        return rephrased_command
    
    