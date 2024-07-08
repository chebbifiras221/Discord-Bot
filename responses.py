from random import choice, randint
import os
from dotenv import load_dotenv

load_dotenv()

def get_response(user_message: str) -> str:
    lowered: str = user_message.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'hello' in lowered:
        return choice(['Hello !', 'Hi !', 'Aslema !'])
    elif 'how are you' in lowered:
        return 'Good, How about you !'
    elif 'good' in lowered:
        return ':)'
    elif 'bad' in lowered:
        return ':('
    elif 'alright' in lowered:
        return ':|'
    elif 'bye' in lowered:
        return 'See you !'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
