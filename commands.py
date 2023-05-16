import random

proglangs = ['Python', 'JavaScript', 'Java', 'C', 'C++', 'C#', 'Go', 'Rust', 'Swift', 'Kotlin', 'Scala', 'PHP']

# Gives random programming language
def random_lang():
    return proglangs[random.randint(0, len(proglangs))]