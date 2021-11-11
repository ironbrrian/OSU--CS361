from googletrans import Translator
from time import sleep

while True:
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

    f.close()
    a.close()

    sleep(20)