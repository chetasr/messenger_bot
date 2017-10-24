# Import essentials

from translate import translator

# Definitions

class translateText:
    # Translate text
    def __init__(self):
        self.inp = 'phrase_to_translate'
        self.out = 'translation'

    def do(self, entities):
        #! TO DO !#
        entities['translation'] = [translator('en', entities['language'], entities['phrase_to_translate'])[0][0][0]]
        return entities
