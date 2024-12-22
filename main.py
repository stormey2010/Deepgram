from deepgram import DeepgramClient, SpeakOptions
import os

# Deepgram TTS
def deepgram_tts(text):
    print("Deepgram function called")
    filename = "core/static/sound/text.mp3" # Filename to save TTS to

    if os.path.exists(filename):
        os.remove(filename)
    
    text = {
        "text": text
    }

    try:
        deepgram = DeepgramClient("DEEPGRAM_API")

        options = SpeakOptions(
            model="aura-asteria-en", # TTS voice
        )

        response = deepgram.speak.v("1").save(filename, text, options)
        print(f"Deepgram tts saved: {response}")

        return filename

    except Exception as e:
        print(f"Deepgram tts failed: {e}")
        return
