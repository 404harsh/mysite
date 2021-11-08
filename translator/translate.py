from googletrans import Translator

def translate(text):
    translation = Translator()
    return translation.translate(text=text, dest='hi').text
    