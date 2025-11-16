from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

#this below code will not work for langchain

'''chat_template = ChatPromptTemplate([
    SystemMessage(content="You are a helpful {domain} expert"),
    HumanMessage(content="Explain in simple terms , what is {topic}")

])# chat_template is an object of ChatPromptTemplate class

#this below code will not work for langchain
#so no need of humanmessage and aimessage and systemmessage
prompt = chat_template.invoke({
    'domain': 'cricket',
    'topic' : 'Dusra'
})

print(prompt)'''

chat_template = ChatPromptTemplate.from_messages([
    ('system', 'You are are helpful {domain} expert'),
    ('human', 'Explain in simple terms , what is {topic}')
])
prompt = chat_template.invoke({'domain': 'cricket', 'topic': 'Dusra'})
print(prompt)
