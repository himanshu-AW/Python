letter='''Dear <|Name|>
Greeting from ABC coding house . I'm happy to tell you about your selection
You are selected !
Have a great day ahead!
Date : <|Date|>'''
name=input("Enter your name \n")
date=input("Enter your date \n")
letter =letter.replace("<|Name|>",name)
letter=letter.replace("<|Date|>",date)
print(letter)