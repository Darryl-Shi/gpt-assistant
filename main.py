import sys
from config import Config
from speech_recognizer import SpeechRecognizer
from gpt_assistant import GPTAssistant

def main(audio_file):
    config = Config()
    recognizer = SpeechRecognizer(config)
    assistant = GPTAssistant(config)

    transcript = recognizer.transcribe_speech(audio_file)
    wake_word = "gpt"
    if wake_word in transcript:
        prompt = transcript.split(wake_word, 1)[1].strip()
        reply = assistant.generate_reply(prompt)
        print(reply)
    else:
        print("Wake word not detected.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Usage: python main.py [audio_file]")
