from google import genai
from google.genai import types
import google.generativeai as genai
import speech_recognition as sr    
import webbrowser
import pyttsx3
import pyautogui
import pyperclip
import subprocess
import datetime
import time
import numpy as np
import threading
import requests 
import asyncio
import base64
import io
import traceback
import cv2
import pyaudio
import PIL.Image
import mss
import argparse
import os
import json
import hmac
import hashlib
import sys
import random


# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()


API_KEY = "AIzaSyD_E8mcnGagr9GFxWvpPLuf8K6YknCQvvE"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash-exp")
chat = model.start_chat()

# Speak function
def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()



def takeCommand():
    # Listen for a command from the user using the microphone and return the recognized text.
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise to improve recognition accuracy
        print("Listening...")
        audio = recognizer.listen(source)  # Capture audio input from the microphone
        try:
            query = recognizer.recognize_google(audio, language="en-in")  # Recognize speech using Google API
            print(f"user said: {query}")
            return query.lower()  # Return the recognized text in lowercase
        except sr.UnknownValueError:
            # Handle case where speech was not understood
            print("Sorry, I didn't catch that. Please try again.")
            return None
        except sr.RequestError as e:
            # Handle API request errors
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None
        except Exception as e:
            # Handle any other exceptions
            print("Some error occurred. Please try again.")
            return None
  
    
# it will open the sites based on the query

def open_sites(query):
    """Open specific websites based on the query."""
    sites = [
        ["youtube", "https://www.youtube.com"],
        ["wikipedia", "https://www.wikipedia.com"],
        ["google", "https://www.google.com"],
        ["instagram", "https://www.instagram.com"],
        ["whatsapp", "https://www.whatsapp.com"],
        ["github", "https://www.github.com"]
    ]
    for site in sites:
        if f"open {site[0]}" in query:
            speak(f"Opening {site[0]} sir...")
            webbrowser.open(site[1])
            return True
    return False

#  it will tell the time based on the query
def tell_time():
    """Tell the current time."""
    hour = datetime.datetime.now().strftime("%I")
    minute = datetime.datetime.now().strftime("%M")
    am_pm = datetime.datetime.now().strftime("%p")
    print(f"Sir, the time is {hour} {minute} {am_pm}") 
    speak(f"Sir, the time is {hour} {minute} {am_pm}") 

def exit():
    pyautogui.click (x=1881, y=21)         # Adjust coordinates for your screen resolution
    time.sleep(3) 
    
def play_music():
    """Play music on YouTube."""
    speak("Please tell me the name of the song.")
    song_name = takeCommand()
    if song_name:
        speak(f"Playing {song_name} on YouTube.")
        webbrowser.open(f"https://www.youtube.com/results?search_query={song_name}")
        time.sleep(5)
        pyautogui.click(x=282, y=533)  # Adjust coordinates for your screen resolution

def send_message():
    """Send a message on WhatsApp."""
    speak("Please tell me the message.")
    message = takeCommand()
    if message:
        speak("Please tell me the name of the contact.")
        contact = takeCommand()
        if contact:
            speak(f"Sending message to {contact}.")
            webbrowser.open("https://web.whatsapp.com/")
            time.sleep(10)  # Wait for WhatsApp Web to load
            pyperclip.copy(message)
            pyautogui.click(x=239, y=313)  # Adjust coordinates for the search bar
            time.sleep(3)
            pyautogui.write(contact)
            time.sleep(5)
            pyautogui.press("enter")
            time.sleep(2)
            pyautogui.click(x=1086, y=965)  # Adjust coordinates for the message box
            pyautogui.hotkey("ctrl", "v")
            time.sleep(2)
            pyautogui.press("enter")
            speak("Message sent successfully.")
       
            speak("Message sent successfully.")

def open_chrome(chrome):
    """
    Open an application using its executable path.

    Args:
        app_path (str): The full path to the application's executable file.
    """
    try:
        subprocess.Popen(chrome, shell=True)  # Open the application
        speak("Opening Chrome")
    except Exception as e:
        print(f"Failed to open the application: {e}")
        speak("Sorry, I couldn't open the application.")

def open_linux(linux):
    try:
        subprocess.Popen(linux, shell=True)  # Open the application
        speak("Opening linux")
    except Exception as e:
        print(f"Failed to open the application: {e}")
        speak("Sorry, I couldn't open the application.")
    pyautogui.click(x= 1174, y=169)    

def open_cursor(cursor):
    try:
        subprocess.Popen(cursor, shell=True)  # Open the application
        speak("Opening cursor")
    except Exception as e:
        print(f"Failed to open the application: {e}")
        speak("Sorry, I couldn't open the application.")

def open_sandbox(sandbox):
    try:
        subprocess.Popen(sandbox, shell=True)  # Open the application
        speak("Opening sandbox")
    except Exception as e:
        print(f"Failed to open the application: {e}")
        speak("Sorry, I couldn't open the application.")
   
def gen_ai():
    while True:
        query = input("you: ")
        if query.lower() == "exit":
            break
        try:
            response = chat.send_message(query)
            speak(f"gemini: {response.text}")
        except Exception as e:
            print("Error:", e)

# Main function
if __name__ == '__main__':
    print('ask me anything')
    speak("yes sir")
    while True:
        query = takeCommand()
        if query is None:
            continue  

        # Handle commands
        if open_sites(query):
            continue
        
        elif "time" in query:
            tell_time()
            
        elif "music" in query:
            play_music()
            
        elif "message" in query:
            send_message()
            
        elif "close" in query:
            exit()
            speak("exiting the site")    
       
        elif "jarvis shutdown" in query:
            speak("Goodbye, sir. Have a great day!")
            break
       
        elif "open chrome" in query:
            chrome_path = r"C:\Users\Public\Desktop\Google Chrome.lnk"  # Correct path to Chrome
            open_chrome(chrome_path)  # Call the function with the path
       
        elif "open linux" in query:
            linux_path = r"C:\Users\Public\Desktop\Oracle VirtualBox.lnk"  # Correct path to linux
            open_linux(linux_path)# Call the function with the path
       
        elif "open cursor" in query:
            cursor_path = r"C:\Users\lenovo\Desktop\Cursor.lnk"  # Correct path to cursor
            open_cursor(cursor_path)  # Call the function with the path
        
        elif "open sandbox" in query:
            sandbox_path = r"C:\Users\lenovo\Desktop\Windows Sandbox.lnk"
            open_sandbox(sandbox_path)
        
        else:
            try:
                response = chat.send_message(query)
                print(f"{response.text}")
                speak(f"{response.text}")
            except Exception as e:
                print("Error:", e)