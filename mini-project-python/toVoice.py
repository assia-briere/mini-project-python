from gtts import gTTS
import os

# Text you want to convert to speech
text = "Hello, this is a text-to-speech example in Python."

# Create a gTTS object
tts = gTTS(text)

# Save the speech as an audio file
tts.save("output.mp3")

# Play the speech using your default audio player (on Windows)
os.system("start output.mp3")
