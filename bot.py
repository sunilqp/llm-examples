import streamlit as st

import nltk
import re
import random
import string

from string import punctuation

#st.text_input("Your name", key="name")

# Download stopwords from nltk
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(nltk.corpus.stopwords.words('english'))
st.write("welcome to Bot")
def sentence_tokenizer(data):
   # Function for Sentence Tokenization
   return nltk.sent_tokenize(data.lower())

def word_tokenizer(data):
   # Function for Word Tokenization
   return nltk.word_tokenize(data.lower())

def remove_noise(word_tokens):
   # Function to remove stop words and punctuation
   cleaned_tokens = []
   for token in word_tokens:
      if token not in stop_words and token not in punctuation:
         cleaned_tokens.append(token)
   return cleaned_tokens

# Define the Patterns and Responses
patterns = [
   (r'hi|hello|hey', ['Hi there!', 'Hello!', 'Hey!']),
   (r'bye|goodbye', ['Bye', 'Goodbye!']),
   (r'(\w+)', ['Yes, go on', 'Tell me more', 'I’m listening...']),
   (r'(\?)', ['I’m sorry, but I can’t answer that', 'Please ask me another question', 'I’m not sure what you mean.'])
]

# Function to generate response for the user input
def generate_response(user_input):
   # Append User Input to chat history
   conversation_history.append(user_input)
   # Generate Random response
   response = random.choice(responses)
   return response

# Main loop of chatbot
conversation_history = []
responses = [response for pattern, response in patterns]
while True:
   # User Input
   # user_input = input("You: ")
   user_input=st.text_input("Your:  ")
   # End the Loop if the User Says Bye or Goodbye
   if user_input.lower() in ['bye', 'goodbye']:
      #print('Chatbot: Goodbye!')
      st.write('Chatbot: Goodbye!')
      break
   # Tokenize the User Input
   user_input_tokenized = word_tokenizer(user_input)
   # Remove Stop Words
   user_input_nostops = remove_noise(user_input_tokenized)
   # Process Query and Generate Response
   chatbot_response = generate_response(user_input_nostops)
   # Print Response
   #print('Chatbot:', chatbot_response)
   st.write('Chatbot:', chatbot_response)
