from langchain_core.prompts import ChatMessagePromptTemplate, MessagesPlaceholder
#chat template
chat_template = ChatMessagePromptTemplate([
    
        ('system','You are a helpful customer support agent'),
        MessagesPlaceholder(variable_name = 'chat_history'), # retreive the chat_history
        ('human', '{query}') # human message with all chat history
    
]) #ek template banaya hai jo jab bhi call ya invoke hoga to sabse phle previous chat history load krega and then user ki query lega 

chat_history = []

# load chat history 
# -- chat_template invoke krne se phle chat_history ko is file mein le aate hai 
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)  

    
#create prompt
prompt = chat_template.invoke({'chat_history': chat_history, 'query': 'Where is my refund'})

print(prompt)