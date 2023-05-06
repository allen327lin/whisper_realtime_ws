import whisper

def detect():
    model = whisper.load_model("tiny")
    print("===");
    result = model.transcribe("bird.wav", language="chinese")
    print(result["text"])