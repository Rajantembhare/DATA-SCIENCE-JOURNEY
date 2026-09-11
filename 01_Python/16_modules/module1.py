import pyttsx3
# Initialize the TTS engine
engine = pyttsx3.init()
# Convert text to speech
engine.say("hey ,rajan how are you what is going on ")
# Wait for the speech to finish
engine.runAndWait()

print("rajan")