# Import essentials

from googletrans import Translator

# Definitions

class translateText:
    # Translate text
    def __init__(self):
        self.inp = 'phrase_to_translate'
        self.out = 'translation'

    def do(self, entities):
        translator = Translator()
        entities['translation'] = [translator.translate(entities['phrase_to_translate'], dest=entities['language']).text]
        return entities
