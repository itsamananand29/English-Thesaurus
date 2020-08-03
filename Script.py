import json
import mysql.connector
from difflib import get_close_matches
import os
conn = mysql.connector.connect(
    host ='localhost',
    user ='root',
    passwd ='root',
    database ='dictionary'

)
curr = conn.cursor()

# def loadData():
#     curr.execute("drop table if exists dict_db")
#     curr.execute("create table dict_db(expression varchar(150),meaning varchar(1500));")
#     for i in data.keys():
#         for j in range(len(data[i])):
#             curr.execute("""insert into dict_db values(%s,%s)""",(i,data[i][j]))
#             conn.commit()
def definition(word):
    curr.execute("""Select meaning from dict_db where expression = '%s'""" %word.lower())
    
    res = curr.fetchall()
   
    if len(res)!=0:
        for i in range(len(res)):
            print(i+1,":",res[i][0])
    else :
        curr.execute("""Select expression from dict_db""") 
        expr = curr.fetchall()
        l=[]
        for i in expr:
            l.append(i[0])
        match = get_close_matches(word,l,cutoff=0.78) 
        if len(match)!=0:
            yn = input("Unkown word %s .Did you mean %s ? Enter Y|y if yes , N|n if no.: "%(word,match[0]))
            if yn == "Y" or yn =="y":
                curr.execute("""Select meaning from dict_db where expression = '%s'""" %match[0].lower())
               
                res2 = curr.fetchall()
                if len(res2)!=0:
                    for i in range(len(res2)):
                        print(i+1,":",res2[i][0])

            elif yn == "n" or yn =="n":
                print("Sorry word doesn't exist. Please check it.")        
            else:
                print("We didn't understand your entry")    
        else:
            print("Sorry word doesn't exist. Please check it.")   
    

def takeWord():
    os.system("cls")
    word=input("Enter a word :\n")
    definition(word)
           
#loadData()
takeWord()    