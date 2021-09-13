from googletrans import Translator, constants
from pprint import pprint

translator = Translator()

translation = translator.translate("Hola Mundo")
translation2 = translator.translate("Wie gehts ?", src="de")

print(translation.text)
print(translation2.text)