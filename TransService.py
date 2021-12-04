from flask import Flask, render_template, request, redirect
import os
import random 
from googletrans import Translator
from time import sleep

# Configuration

app = Flask(__name__) 

def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

def translate(text):
    ret_list = []
    request = open('response.txt', 'w')
    request.write(text) 
# while True:
    # opens the txt file
    f = open("request.txt", 'r')
    a = open("response.txt", 'a')
    if f.mode == 'r':
        text_to_translate = f.read()
        # Prints the text that will eventually be translated
        print(text_to_translate)

    translator = Translator()

    # translate contents of request.txt
    translated_text = translator.translate(text_to_translate, dest="en")
    # Prints the translated text
    print(translated_text.text)

    # More supported languages can be found at https://py-googletrans.readthedocs.io/en/latest/, just scroll down!

    # write translation to the response.txt
    # I had to add encoding = utf-8 for it to work with certain languages, like Japanese for example
    with open('response.txt', 'w', encoding="utf-8") as f:
        f.write(translated_text.text)
    ret_list.append(translated_text.text) 
    
    
    f.close()
    a.close()
    return ret_list 

    # sleep(20)

@app.route('/', methods =['POST', 'GET'])
def my_form_post():
    if request.method == "POST":
        text = request.form["text"]
        converted = translate(text)
        return render_template("translatedisplay.j2", data=converted)
        
    
    else: 
        return render_template("translate.j2")


# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 1679)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port) 