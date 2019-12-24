
# Python program to  
# demonstrate creation of an 
# assistant using wolf ram API 
  
import wolframalpha 
  
# Taking input from user 

  
# App id obtained by the above steps 
# app_id = ‘Your app_id’ 
  
# Instance of wolf ram alpha  
# client class 
client = wolframalpha.Client('PTXAVW-7G94KUAYPA') 
  
# Stores the response from  
# wolf ram alpha 
while True:
    question = input('Question: ') 

    res = client.query(question) 
  
# Includes only text from the response 
    answer = next(res.results).text 
  
    print(answer) 