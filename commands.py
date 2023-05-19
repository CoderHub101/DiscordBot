import random

commandList = {'codinglang':'Selects a random coding language.', 'coinflip': 'Flips a coin.'}
proglangs = ['Python', 'JavaScript', 'Java', 'C', 'C++', 'C#', 'Go', 'Rust', 'Swift', 'Kotlin', 'Scala', 'PHP']

# Gives random programming language
def random_lang():
    return proglangs[random.randint(0, len(proglangs))]

def coinflip():
    rand = random.randint(0, 2)
    if rand == 1:
        return "Heads"
    else:
        return "Tails"