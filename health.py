#include<stdio.h>
### Health Management APP
from dotenv import load_dotenv

load_dotenv() ## load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Google Gemini Pro Vision API And get response

def get_gemini_repsonse(input,image,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
##initialize our streamlit app

st.set_page_config(FORGE.RED ,page_title=" MACHIne AI-  jk ")

st.header("MACHIne AI-  jk")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Identify the Machine")

input_prompt="""
You are an expert in machines or electronics and you need to identify the machines and electronics parts
and need to define the parts and explain about the parts and how they work how the machine is made .
give real life application , about it and say how it is evolved 


output should be like the below mentioned thing 

                  FONT SHOULD TIMES NEW ROMAN 
                  
                  the identified name of the machine ( itshould be bold bigger in text in old london font it should be bigger than other text this is title)
                  
                  list its parts one by one like bulletin points
                  
                  explain about its parts in seperatley with minimuym 200 words

            
                  say how that identified machine works (470 WORDS)
                  
                  how the identified machine is made ( minimum350 word)
                  
                  how the identified machine has evolved (350 WORDS)
                
                 then  say its real life application , where it is usedin bulletin points minimum 18 points or application
                  
                  who invented the machine (300 WORDS)
                  
                  who manufactured that ,machine (375 WORDS)
                  
                  say about that manufacturing company, THEIR AIM ETC ( 450 WORDS)
                  
                  
       the above given shouldbe made properly , with good english .
                  

                  
                                    

               ----
               ----


"""

## If submit button is clicked

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt,image_data,input)
    st.subheader("DESCRIPTION ABOUT THE IDENTIFIED MACHINE IS GIVEN BELOW")
    st.write(response)


