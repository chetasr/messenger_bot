# Import essentials

import random

# Definitions

greetings = ['Hello there!',
             'Hi!',
             'Hello!',
             'Greetings!']

class returnGreeting:
    # Greet the user
    def __init__(self):
        self.inp = 'greeting'
        self.out = 'greet'

    def do(self, entities):
        entities['greet'] = [random.choice(greetings)]
        return entities
