from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = [
    SystemMessage(content="You are a helpful assistant that answers questions based on facts and figures")
]


while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content= result.content)) # chat history going to llm
    print("AI: " , result.content)
    
    

print(chat_history)



#[SystemMessage(content='You are a helpful assistant that answers questions based on facts and figures', additional_kwargs={}, response_metadata={}), HumanMessage(content='hello', additional_kwargs={}, response_metadata={}), AIMessage(content='Hello! How can I assist you today?', additional_kwargs={}, response_metadata={}), HumanMessage(content='tell me about the recent tarrif imposed on india by usa', additional_kwargs={}, response_metadata={}), AIMessage(content='As of my last update, the United States imposed tariffs on various products imported from India, including steel and aluminum. These tariffs were implemented in response to certain trade practices and policies of India that the U.S. deemed unfair. It is important to note that trade relations between countries can change rapidly, so I recommend checking the latest news or updates for the most current information on this topic. Let me know if you need more details or have any other questions.', additional_kwargs={}, response_metadata={}), HumanMessage(content='tell me about austria', additional_kwargs={}, response_metadata={}), AIMessage(content='Austria is a landlocked country located in Central Europe, known for its rich history, stunning alpine scenery, and cultural heritage. Here are some quick facts about Austria:\n\n- Capital: Vienna\n- Population: Approximately 9 million people\n- Official language: German\n- Currency: Euro (EUR)\n- Government: Federal parliamentary republic\n- Famous for its historical figures like Mozart, Strauss, and Freud\n- Known for its Baroque architecture, alpine landscapes, and charming villages\n- Popular tourist destinations include Vienna, Salzburg, Innsbruck, and the Austrian Alps\n\nAustria has a high standard of living, excellent healthcare and education systems, and a strong focus on cultural activities. It is also a member of the European Union. If you have any specific questions about Austria or want more detailed information, feel free to ask!', additional_kwargs={}, response_metadata={}), HumanMessage(content='exit', additional_kwargs={}, response_metadata={})]
  #history ----
'''You: exit
[SystemMessage(content='You are a helpful assistant that answers questions based on facts and figures', additional_kwargs={}, response_metadata={}), HumanMessage(content='hello', additional_kwargs={}, response_metadata={}), AIMessage(content='Hello! How can I assist you today?', additional_kwargs={}, response_metadata={}), HumanMessage(content='tell me about the recent tarrif imposed on india by usa', additional_kwargs={}, response_metadata={}), AIMessage(content='As of my last update, the United States imposed tariffs on various products imported from India, including steel and aluminum. These tariffs were implemented in response to certain trade practices and policies of India that the U.S. deemed unfair. It is important to note that trade relations between countries can change rapidly, so I recommend checking the latest news or updates for the most current information on this topic. Let me know if you need more details or have any other questions.', additional_kwargs={}, response_metadata={}), HumanMessage(content='tell me about austria', additional_kwargs={}, response_metadata={}), AIMessage(content='Austria is a landlocked country located in Central Europe, known for its rich history, sng alpine scenery, and cultural heritage. Here are some quick facts about Austria:\n\n- Capital: Vienna\n- Population: Approximately 9 million people\n- Official language: German\n- Currency: Euro (EUR)\n- Government: Federal parliamentary republic\n- Famous for its historical figures like Mozart, Strauss, and Freud\n- Known for its Baroque architecture, alpine landscapes, and charm quick facts about Austria:\n\n- Capital: Vienna\n- Population: Approximately 9 million people\n- Official language: German\n- Currency: Euro (EUR)\n- Government: Federal parliamentary republic\n- Famous for its historical figures like Mozart, Strauss, and Freud\n- Known for its Baroque architecture, alpine landscapes, and charmulation: Approximately 9 million people\n- Official language: German\n- Currency: Euro (EUR)\n- Government: Federal parliamentary republic\n- Famous for its historical figures like Mozart, Strauss, and Freud\n- Known for its Baroque architecture, alpine landscapes, and charmguage: German\n- Currency: Euro (EUR)\n- Government: Federal parliamentary republic\n- Famous for its historical figures like Mozart, Strauss, and Freud\n- Known for its Baroque architecture, alpine landscapes, and charmderal parliamentary republic\n- Famous for its historical figures like Mozart, Strauss, and Freud\n- Known for its Baroque architecture, alpine landscapes, and charmal figures like Mozart, Strauss, and Freud\n- Known for its Baroque architecture, alpine landscapes, and charming villages\n- Popular tourist destinations include Vi its Baroque architecture, alpine landscapes, and charming villages\n- Popular tourist destinations include Viing villages\n- Popular tourist destinations include Vienna, Salzburg, Innsbruck, and the Austrian Alps\n\nAustria has a high standard of living, excellent healthcare and education systems, and a strong focus on culturalenna, Salzburg, Innsbruck, and the Austrian Alps\n\nAustria has a high standard of living, excellent healthcare and education systems, and a strong focus on cultural activities. It is also a member of the European Union.e and education systems, and a strong focus on cultural activities. It is also a member of the European Union. activities. It is also a member of the European Union. If you have any specific questions about Austria or waree to ask!', additional_kwargs={}, response_metadata={}), HumanMessage(content='exit', additional_kwargs={icket expert', additional_kwargs={}, reicket expert', additional_kwargs={}, response_metadata={}), HumanMessage(conteicket expert', additional_kwargs={}, response_metadicket expert', additional_kwargs={}, response_metadata={}), HumanMessage(content='Explain in simple terms , what is Dusra', additional_kwargs={}, response_metadata={})]
(venv) PS E:\Langchain> python 4.Prompts\messages.py
You:  Hello
AI:  Hello! How can I assist you today?
You: name the beautiful place in india
AI:  India is home to numerous beautiful places. Some of the most famous ones include:

1. The Taj Mahal in Agra
2. The backwaters of Kerala
3. The Golden Temple in Amritsar
4. The Hawa Mahal in Jaipur
5. The beaches of Goa
6. The hill stations of Darjeeling and Shimla
7. The historical ruins of Hampi
8. The serene beauty of Munnar in Kerala
9. The spiritual town of Varanasi
10. The vibrant city of Mumbai

These are just a few examples of the many beautiful places you can visit in India.
You: taj mahal is it good?
AI:  The Taj Mahal is widely considered one of the most beautiful and iconic structures in the world. It is a UNESCO World Heritage Site and a symbol of love, as it was built by the Mughal emperor Shah Jahan in memory of his wife Mumtaz Mahal. The Taj Mahal's stunning white marble architecture, intricate carvings, and picturesque gardens make it a must-visit destination for travelers from around the globe. It is definitely worth a visit if you appreciate history, architecture, and breathtaking beauty.
You: is it spacious?
AI:  The Taj Mahal complex is spread out over a large area of about 42 acres (17 hectares). The main mausoleum building itself is spacious and covers an area of approximately 42 meters by 58 meters. The surrounding gardens, walkways, and reflecting pools add to the overall expansive feel of the complex. Visitors have plenty of space to walk around, explore the different sections of the complex, and take in the beauty of the Taj Mahal from various angles. The wide open spaces and intricate layout of the Taj Mahal complex contribute to its grandeur and magnificence.
You: how long is it
AI:  The Taj Mahal is an impressive structure that measures approximately 73 meters (240 feet) in height. It is a symmetrical building with each side of the main mausoleum measuring about 55 meters (180 feet) in length. The central dome of the Taj Mahal reaches a height of around 35 meters (115 feet) above the main platform. These dimensions contribute to the majestic appearance of the Taj Mahal and its iconic silhouette that is recognized worldwide.
You: ok and does it have canteen
AI:  Yes, the Taj Mahal complex does have facilities for visitors, including a canteen where you can purchase food and beverages. The canteen typically offers a variety of snacks, drinks, and light meals for visitors to enjoy during their visit to the monument. This can be convenient for those who want to take a break and have a quick bite to eat while exploring the Taj Mahal and its surroundings.
You: exit
[SystemMessage(content='You are a helpful assistant that answers questions based on facts and figures', additional_kwargs={}, response_metadata={}), HumanMessage(content=' Hello', additional_kwargs={}, response_metadata={}), AIMessage(content='Hello! How can I assist you today?', additional_kwargs={}, response_metadata={}), The Taj Mahal is an impressive structure that measures approximately 73 meters (240 feet) in height. It is a symmetrical building with each side of the main mausoleum measuring about 55 meters (180 feet) in length. The central dome of the Taj Mahal reaches a height of around 35 meters (115 feet) above the main platform. These dimensions contribute to the majestic appearance of the Taj Mahal and its iconic silhouette that is recognized worldwide.', additional_kwargs={}, response_metadata={}), HumanMessage(content='ok and does it have canteen', additional_kwargs={}, response_metadata={}), AIMessage(content='Yes, the Taj Mahal complex does have facilities for visitors, including a canteen where you can purchase food and beverages. The canteen typically offers a variety of snacks, drinks, and light meals for visitors to enjoy during their visit to the monument. This can be convenient for those who want to take a break and have a quick bite to eat while exploring the Taj Mahal and its surroundings.', additional_kwargs={}, response_metadata={}), HumanMessage(content='exit', additional_kwargs={}, response_metadata={})]
(venv) PS E:\Langchain>
'''