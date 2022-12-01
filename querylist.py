
class Trivia:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer 

    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answer

def whatRegion(pokemon):
    question = "What region does " + getName(pokemon) + " come from?"
    answer = getRegion(pokemon)
    return Trivia(question, answer)
def howTall(pokemon):
    question = "How tall is " + getName(pokemon) + "?"
    answer = (getSize(pokemon))
    return Trivia(question, answer)
def whatTypes(pokemon):
    print("What type(s) does " + getName(pokemon) + " have?")
    print(getTypes(pokemon))
    print()



def getName(pokemon):
    return (pokemon[0]["name"])

def getRegion(pokemon):
    return (pokemon[0]["region"])

def getClassification(pokemon):
    return (pokemon[0]["classification"])

def getTypes(pokemon):
    return (pokemon[0]["types"])

def getSize(pokemon):
    return (pokemon[0]["size"])

def getSize(pokemon):
    return (pokemon[0]["size"])

def getWeight(pokemon):
    return (pokemon[0]["weight"])

def getLevelMoves(pokemon):
    return (pokemon[0]["levelmoves"])