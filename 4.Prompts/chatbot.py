from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = []


while True:
    user_input = input('You: ')
    user_messages = {
        "role" : "user",
        "content" : user_input
    }
    chat_history.append(user_messages)
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    ai_messages = {
        "role": "ai",
        "content" : result.content
    }
    chat_history.append(ai_messages) # chat history going to llm
    print("AI: " , result.content)
    
    

print(chat_history)


#[' hello', 'Hello! How can I assist you today?', ' how are oyu', "I'm just a computer program, so I don't have feelings in the same way that humans do. But I'm here and ready to help you with whatever you need. How can I assist you today?", ' ok', "Great! If you have any questions or need assistance with anything, feel free to let me know. I'm here to help.", 'exit']
# chat history doesnt contain which message was sent by whom , no role assigned so assign rle like human , ai


# after appending dictionary to list 
#[{'role': 'user', 'content': 'hello'}, {'role': 'ai', 'content': 'Hello! How can I assist you today?'}, {'role': 'user', 'content': 'how are you'}, {'role': 'ai', 'content': "I'm just a computer program, so I don't have feelings in the same way humans do. But I'm here and ready to help you with any questions or tasks you might have!"}, {'role': 'user', 'content': 'exit'}]
