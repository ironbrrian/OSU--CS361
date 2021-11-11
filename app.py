from flask import Flask, render_template, request, redirect
import os
import random

os.system('python TransService.py')

from flask.helpers import url_for

# Configuration

app = Flask(__name__)

# Routes 
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


response_file = "response.txt"

with open(response_file) as f:
    contents = f.readlines()
    # print(contents)

    for ele in contents:
        print("Converted Number:",text2int(ele))



def randomID(amount):
    amount = int(amount)
    for i in range(amount):
        return [random.randint(1000, 9999)]

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
             'CD': 400, 'CM': 900}
    i = 0
    num = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i + 2] in roman:
            num += roman[s[i:i + 2]]
            i += 2
        else:
            # print(i)
            num += roman[s[i]]
            i += 1
    return num

def int_to_Roman(num): 
        num = int(num)
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

@app.route('/')
def home():
    return render_template("main.j2")

@app.route('/', methods =['POST', 'GET'])
def my_form_post():
    if request.method == "POST":
        text = request.form["num"]
        converted = int_to_Roman(text)
        return redirect(url_for("user", usr=converted))
    
    else: 
        return render_template("main.j2")

@app.route('/numeral', methods = ['GET', 'POST'])
def numeral():
    if request.method == "POST":
        text = request.form["text"]
        converted = romanToInt(text)
        return redirect(url_for("user", usr=converted))
    
    else:
        return render_template("numeral.j2")


@app.route('/integer', methods = ['GET', 'POST'])
def integer():
    if request.method == "POST":
        text = request.form["num"]
        converted = int_to_Roman(text)
        return redirect(url_for("user", usr=converted))
    
    else:
         return render_template("main.j2")

@app.route('/randint', methods = ['GET', 'POST'])
def randint(): 
    if request.method == "POST":
        text = request.form["num"]
        converted = randomID(text)
        return redirect(url_for("user", usr=converted))
    
    else:
         return render_template("randomID.j2")

@app.route("/<usr>")
def user(usr):
    return f"<h1>Copy this: {usr}</h1>"



# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 1604)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port) 