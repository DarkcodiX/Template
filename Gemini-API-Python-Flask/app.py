# Simple python flask application for Gemini API by Th3-C0der
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
app = Flask(__name__) 

#Configure the Gemini API

genai. configure(api_key='Geminai-key')
model = genai. GenerativeModel('gemini-1. 0-pro')
@app.route('/', methods=['GET', 'POST'])
def index():
if request.method == 'POST':
prompt = request.form['prompt']
response = model.
generate_content(prompt)
return jsonify({'response': response.
text})
return render_template('index.html')
if_name__ == '__main__':
app.run(debug=True)
