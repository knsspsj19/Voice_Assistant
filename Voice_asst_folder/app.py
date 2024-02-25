from flask import Flask, render_template, request, jsonify
# from main import handle_response,get_response
import speech_recognition as sr

app = Flask(__name__)

def ask_question(question):
    return question

def get_response():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        response = recognizer.recognize_google(audio)
        return response.lower()
    except OSError as e:
        return "No Default input device available. Run without docker using python app.py command within Voice_asst_folder"
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

@app.route('/')
def index():
    question = "Is technology making humanity better?"
    return render_template('index.html', question=question)

@app.route('/response', methods=['POST'])
def handle_user_response():
    data = request.json
    user_response = data.get('response')
    print(f"Your response is {user_response}")
    question = "Is technology making humanity better?"
    response = handle_response(question)
    
    # Logging interaction
    with open("interaction.log", "a") as f:
        f.write(f"Question: {question}\nResponse: {response}\n")

    return jsonify({'status': 'success'})



if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)
    
    

