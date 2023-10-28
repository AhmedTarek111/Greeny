import random

def generate_code(length=15):
    data='1234567890abcdefgijklmnopqi'
    code = ''.join(random.choice(data) for _ in range(length))
    return code
    

