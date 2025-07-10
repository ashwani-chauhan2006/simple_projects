import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get the list of available voices
voices = engine.getProperty('voices')

# Print the name and language of each voice
for voice in voices:
    print(f"Voice ID: {voice.id}")
    print(f"Name: {voice.name}")
    print(f"Language: {voice.languages}")
    print("-" * 30)