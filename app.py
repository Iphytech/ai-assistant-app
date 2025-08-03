import speech_recognition as sr
import pyttsx3
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# load AI model
llm = OllamaLLM(model="mistral")


# initialize chat history
chat_history = ChatMessageHistory()
# initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)  # Set speech rate

# speech recognition setup
recognizer = sr.Recognizer()

# function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# function to listen and recognize speech
def listen():
    with sr.Microphone() as source:
        print(" Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""

    # AI chat prompt template
prompt= PromptTemplate(
    input_variables=["chat_history", "question"],
    template="previous conversation: {chat_history}\nUser: {question}\nAI:"

)

# function to process the AI response
def run_chain(question):
    # retrive the past chat history manually
    chat_history_text = "\n".join(
        [f"{msg.type.capitalize()}: {msg.content}" for msg in chat_history.messages]
    )

# run AI response
    response = llm.invoke(prompt.format(
        chat_history=chat_history_text,
        question=question
    ))

    # store new user input and AI response in memory
    chat_history.add_user_message(question)
    chat_history.add_ai_message(response)

    return response

# main loop
speak("Hello! I am your AI Assistant. How can I assist you today?")
while True:
    query = listen()
    if "exit" in query or "stop" in query:
        speak("Goodbye! Take care!")
        break
    if query:
        response = run_chain(query)
        print (f"AI: {response}")
        speak(response)
    else:
        speak("Please try again.")
