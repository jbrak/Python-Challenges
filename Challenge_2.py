from random import randint

def replace(w):
    new = ""
    for i in range(0,len(w)):
        new += "*"
    return(new)


words = [{"ZOO" : "an establishment which maintains a collection of wild animals"},
        {"OFFICE" : "a room, set of rooms, or building used as a place for commercial, professional, or bureaucratic work"},
        {"HOUSE" : "a building for human habitation"},
        {"APPARTMEANT" : "a flat, typically one that is well appointed or used for holidays"}]

randWord = words[randint(0,3)]

w = list(randWord.keys())[0]

hidden = replace(w)

print(ranWord.values())
print(hidden)
