import json
import mysql.connector
from difflib import get_close_matches
import os

data = json.load(open("data.json"))

def definition(word):
       
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]        
    else :
        match = get_close_matches(word,data.keys(),cutoff=0.78)
        if len(match)!=0:
            yn = input("Unkown word %s .Did you mean %s ? Enter Y|y if yes , N|n if no."%(word,match[0]))
            if yn == "Y" or yn =="y":
                return data[match[0]]
            elif yn == "n" or yn =="n":
                return ["Sorry word doesn't exist. Please check it."]        
            else:
                return ["We didn't understand your entery"]    
            
        else:
            return ["Sorry word doesn't exist. Please check it."]    

def takeWord():
    os.system("cls")
    word=input("Enter a word :\n")
    definition(word)
    meaning = definition(word.lower())
    for i in range(len(meaning)):
        print(i+1,". ",meaning[i])        

takeWord()    