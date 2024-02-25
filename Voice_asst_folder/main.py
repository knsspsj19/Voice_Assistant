import speech_recognition as sr

def ask_question(question):
    print(question)

def get_response():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        response = recognizer.recognize_google(audio)
        return response.lower()
    except sr.UnknownValueError:
        return "invalid"
    except sr.RequestError:
        return "error"

def handle_response(question):
    for _ in range(3):  # Allow up to 3 attempts
        answer = get_response()
        if answer in ['yes', 'no']:
            return answer
        else:
            print("Please answer with 'Yes' or 'No'.")
    return "invalid"

def main():
    question = "Is technology making humanity better?"
    ask_question(question)
    response = handle_response(question)

    # Logging interaction
    with open("interaction.log", "a") as f:
        f.write(f"Question: {question}\nResponse: {response}\n")

if __name__ == "__main__":
    main()
