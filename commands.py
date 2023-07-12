import random

commandList = {'codinglang':'Selects a random coding language.', 
               'coinflip': 'Flips a coin.'}
proglangs = ['Python', 'JavaScript', 'Java', 'C', 'C++', 'C#', 'Go', 'Rust', 'Swift', 'Kotlin', 'Scala', 'PHP']
todo = []


# Gives random programming language
def random_lang():
    return proglangs[random.randint(0, len(proglangs))]

def coinflip():
    rand = random.randint(0, 2)
    if rand == 1:
        return "Heads"
    else:
        return "Tails"
    
def help():
    string = ''
    for command in commandList:
        string += f"coderbot {command} - {commandList[command]}\n"
        
    return string
    
class ToDoListItem:
    def __init__(self, item, due_date):
        self.item = item
        self.due_date = due_date

    def done(self):
        todo.remove(self)
        del self

    
    
def todo_list(item, due_date):
    todo.append(ToDoListItem(item, due_date))
    
def print_todo():
    for task in todo:
        print(task.item, task.due_date)
        # TODO: Fix this

