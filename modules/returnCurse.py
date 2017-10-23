# Import essentials

import random

# Definitions

curses = ['Hey! I don\'t think I deserve that',
          'I\'d never speak to you that way']

class returnCurse:
    # Replies for cursing
    def __init__(self):
        self.inp = 'curseword'
        self.out = 'curse'

    def do(self, entities):
        entities['curse'] = [random.choice(curses)]
        return entities
