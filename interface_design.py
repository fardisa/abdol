```python
from flask import Flask, render_template, request
from chatbot_mistral_ai import Chatbot
from user_roles import User

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    bot = Chatbot()
    bot_response = bot.get_response(user_message)
    return bot_response

@app.route('/user_profile/<user_id>')
def user_profile(user_id):
    user = User(user_id)
    return render_template('user_profile.html', user=user)

@app.route('/booking_form')
def booking_form():
    return render_template('booking_form.html')

@app.route('/review_form')
def review_form():
    return render_template('review_form.html')

if __name__ == "__main__":
    app.run(debug=True)
```
This code assumes that the HTML templates (index.html, user_profile.html, booking_form.html, review_form.html) are located in a templates folder in the same directory as this script. The templates should be designed to provide a user-friendly interface for the chatbot platform.