import webbrowser
from google import genai
from google.genai import types
import speech_recognition as sr    
import webbrowser
import pyttsx3
import io
import traceback
import cv2
import pyaudio
import PIL.Image
import mss
import argparse
import pyautogui
import pyperclip
import datetime
import base64
import asyncio
import time
import numpy as np

import requests 
import subprocess
import os
import json
import hmac
import hashlib
import sys
import random


FORMAT = pyaudio.paInt16
CHANNELS = 1
SEND_SAMPLE_RATE = 16000
RECEIVE_SAMPLE_RATE = 24000
CHUNK_SIZE = 1024

recognizer = sr.Recognizer()
engine = pyttsx3.init()

MODEL = "models/gemini-2.0-flash-exp"
DEFAULT_MODE = "camera"

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

client = genai.Client(http_options={"api_version": "v1alpha"}, api_key="AIzaSyD_E8mcnGagr9GFxWvpPLuf8K6YknCQvvE")



def open_youtube():
    """Open YouTube in the default web browser."""
    print("Opening YouTube...")
    speak("Opening YouTube...")
    webbrowser.open("https://www.youtube.com")

def open_github():
    """Open github in the default web browser."""
    print("Opening github...")
    speak("Opening github...")
    webbrowser.open("https://www.github.com")

def open_whatsapp():
    """Open whasapp in the default web browser."""
    print("Opening whatsapp...")
    speak("Opening whatsapp...")
    webbrowser.open("https://web.whatsapp.com/")

def send_message():
    """Send a message on WhatsApp."""
    try:
        # Ask for the message
        speak("Please tell me the message.")
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            message = recognizer.recognize_google(audio, language="en-in")
            print(f"Message: {message}")
  
        # Ask for the contact name
        speak("Please tell me the name of the contact.")
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            contact = recognizer.recognize_google(audio, language="en-in")
            print(f"Contact: {contact}")
  
        # Open WhatsApp Web and send the message
        if contact and message:
            speak(f"Sending message to {contact}.")
            webbrowser.open("https://web.whatsapp.com/")
            time.sleep(10)  # Wait for WhatsApp Web to load
            pyperclip.copy(message)
            pyautogui.click(x=239, y=313)  
            time.sleep(3)
            pyautogui.write(contact)
            time.sleep(5)
            pyautogui.press("enter")
            time.sleep(2)
            pyautogui.click(x=1086, y=965) 
            pyautogui.hotkey("ctrl", "v")
            time.sleep(2)
            pyautogui.press("enter")
            speak("Message sent successfully.")
        else:
            speak("I could not understand the contact or message. Please try again.")
   
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")
        speak("Sorry, I didn't catch that. Please try again.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        speak("There was an error with the speech recognition service.")
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("An error occurred while sending the message.")


def tell_time():
    """Tell the current time."""
    hour = datetime.datetime.now().strftime("%I")
    minute = datetime.datetime.now().strftime("%M")
    am_pm = datetime.datetime.now().strftime("%p")
    print(f"Sir, the time is {hour} {minute} {am_pm}")
    speak(f"Sir, the time is {hour} {minute} {am_pm}")

def exit_site():
    print("exiting the site")
    speak("exiting the site")
    pyautogui.click (x=1881, y=21)               
    time.sleep(3) 
    
def play_music():        
        speak("please tell me the song name")
        with sr.Microphone() as source:
            print("listening.......")
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
            song_name = recognizer.recognize_google(audio).lower()
            print(f"song name:{song_name}")
            speak(f"song name {song_name}")
            time.sleep(1)
         # Open YouTube and search for the song
            webbrowser.open(f"https://www.youtube.com/results?search_query={song_name}")
            time.sleep(5)  # Wait for the page to load    
        pyautogui.click(x=282, y=533)  
        speak("Enjoy your music!")

    
CONFIG = types.LiveConnectConfig(
    response_modalities=[
        "audio",
    ],
    speech_config=types.SpeechConfig(
        voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name="puck")
        )
    ),
)
pya = pyaudio.PyAudio()

class AudioLoop:
    def __init__(self, video_mode=DEFAULT_MODE):
        self.video_mode = video_mode
        self.audio_in_queue = None
        self.out_queue = None
        self.session = None
        self.send_text_task = None
        self.receive_audio_task = None
        self.play_audio_task = None

    async def send_text(self):
        while True:
            # text = takeCommand()
                text = await asyncio.to_thread(input, "message > ")
                if text.lower() == "q":
                    break
                elif "youtube" in text.lower(): 
                    open_youtube()              
                elif "github" in text.lower():  
                    open_github()  
                elif "whatsapp" in text.lower():  
                    open_whatsapp()  
                elif "time" in text.lower(): 
                    tell_time() 
                elif "send message" in text.lower():  
                    send_message() 
                elif "send" in text.lower():
                    send_message()  
                elif "exit" in text.lower():
                    exit_site()  
                elif "play" in text.lower():  
                    play_music() 
                else:
                    await self.session.send(input=text or ".", end_of_turn=True)
           
# 5. Capturing Video Frames

    def _get_frame(self, cap):
        # Read the frameq
        ret, frame = cap.read()
        # Check if the frame was read successfully
        if not ret:
            return None
        # Fix: Convert BGR to RGB color space
        # OpenCV captures in BGR but PIL expects RGB format
        # This prevents the blue tint in the video feed
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = PIL.Image.fromarray(frame_rgb)  # Now using RGB frame
        img.thumbnail([1024, 1024])
        image_io = io.BytesIO()
        img.save(image_io, format="jpeg")
        image_io.seek(0)
        mime_type = "image/jpeg"
        image_bytes = image_io.read()
        return {"mime_type": mime_type, "data": base64.b64encode(image_bytes).decode()}

    async def get_frames(self):
        # This takes about a second, and will block the whole program
        # causing the audio pipeline to overflow if you don't to_thread it.
        cap = await asyncio.to_thread(
            cv2.VideoCapture, 0
        )  # 0 represents the default camera
        while True:
            frame = await asyncio.to_thread(self._get_frame, cap)
            if frame is None:
                break
            await asyncio.sleep(1.0)
            await self.out_queue.put(frame)
        # Release the VideoCapture object
        cap.release()

# Capturing Screenshots

    def _get_screen(self):
        sct = mss.mss()
        monitor = sct.monitors[0]
        i = sct.grab(monitor)
        mime_type = "image/jpeg"
        image_bytes = mss.tools.to_png(i.rgb, i.size)
        img = PIL.Image.open(io.BytesIO(image_bytes))
        image_io = io.BytesIO()
        img.save(image_io, format="jpeg")
        image_io.seek(0)
        image_bytes = image_io.read()
        return {"mime_type": mime_type, "data": base64.b64encode(image_bytes).decode()}

    async def get_screen(self):
        while True:
            frame = await asyncio.to_thread(self._get_screen)
            if frame is None:
                break
            await asyncio.sleep(1.0)
            await self.out_queue.put(frame)

# 7. Sending Real-Time Data

    async def send_realtime(self):
        while True:
            msg = await self.out_queue.get()
            await self.session.send(input=msg)

# Listening to Audio
   
    async def listen_audio(self):
        recognizer = sr.Recognizer()
        mic_info = pya.get_default_input_device_info()
        self.audio_stream = await asyncio.to_thread(
            pya.open,
            format=FORMAT,
            channels=CHANNELS,
            rate=SEND_SAMPLE_RATE,
            input=True,
            input_device_index=mic_info["index"],
            frames_per_buffer=CHUNK_SIZE,
        )
        if __debug__:
            kwargs = {"exception_on_overflow": False}
        
        else:
            kwargs = {}
        while True:        
           data = await asyncio.to_thread(self.audio_stream.read, CHUNK_SIZE, **kwargs)
           await self.out_queue.put({"data": data, "mime_type": "audio/pcm"}) 
             

#  Receiving Audio

    async def receive_audio(self):
        "Background task to reads from the websocket and write pcm chunks to the output queue"
        while True:
            turn = self.session.receive()
            async for response in turn:
                if data := response.data:
                   # # self.audio_in_queue.put_nowait(data)
                    self.audio_in_queue.put_nowait(data)
                    # print(self.audio_in_queue)
                    continue
                if text := response.text:
                     print(text, end="")               
            while not self.audio_in_queue.empty():
                self.audio_in_queue.get_nowait()
                
            # If you interrupt the model, it sends a turn_complete.
            # For interruptions to work, we need to stop playback.
            # So empty out the audio queue because it may have loaded
            # much more audio than has played yet.


# . Playing Audio

    async def play_audio(self):
        stream = await asyncio.to_thread(
            pya.open,
            format=FORMAT,
            channels=CHANNELS,
            rate=RECEIVE_SAMPLE_RATE,
            output=True,     
        )   
        while True:
            bytestream = await self.audio_in_queue.get()
            await asyncio.to_thread(stream.write, bytestream)

# Running the Main Loop

    async def run(self):
        try:
            async with (
                client.aio.live.connect(model=MODEL, config=CONFIG) as session,
                asyncio.TaskGroup() as tg,
            ):
                self.session = session
                self.audio_in_queue = asyncio.Queue()
                self.out_queue = asyncio.Queue(maxsize=5)

                send_text_task = tg.create_task(self.send_text())
                tg.create_task(self.send_realtime())
                tg.create_task(self.listen_audio())
                if self.video_mode == "camera":
                    tg.create_task(self.get_frames())
                elif self.video_mode == "screen":
                    tg.create_task(self.get_screen())

                tg.create_task(self.receive_audio())
                tg.create_task(self.play_audio())
              
                await send_text_task  
                raise asyncio.CancelledError("User requested exit")
             
        except asyncio.CancelledError:
            pass
        except ExceptionGroup as EG:
            self.audio_stream.close()
            traceback.print_exception(EG)
                                                

# Main function to run the program
if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        type=str,
        default=DEFAULT_MODE,
        help="pixels to stream from",
        choices=["camera", "screen", "none"],
    )
    args = parser.parse_args()
    main = AudioLoop(video_mode=args.mode)
    asyncio.run(main.run())