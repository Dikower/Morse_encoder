MorseCodeEng = {"A": ".-","B": "-...","C": "-.-.","D": "-..","E": ".","F": "..-.","G": "--.","H": "....","I": "..","J": ".---","K": "-.-","L": ".-..","M": "--","N": "-.","O": "---","P": ".--.","Q": "--.-","R": ".-.","S": "...","T": "-","U": "..-","V": "...-","W": ".--","X": "-..-","Y": "-.--","Z": "--..","0": "-----","1": ".----","2": "..---","3": "...--","4": "....-","5": ".....","6": "-....","7": "--...","8": "---..","9": "----.","Ä": ".-.-","Ü": "..--","ß": "...--..","À": ".--.-","È": ".-..-","É": "..-..",".": ".-.-.-",",": "--..--",":": "---...",";": "-.-.-.","?": "..--..","-": "-....-","_": "..--.-","(": "-.--.",")": "-.--.-","'": ".----.","=": "-...-","+": ".-.-.","/": "-..-.","@": ".--.-."," ": " ","" : ""}
def encodeToMorse(text = 'Разработчики: TevaSTARK,semenis,Dikower',language = MorseCodeEng):
    res = []
    for i in text.upper():
        if i in language:
            res.append(language[i])
    return(' '.join(res))
print(encodeToMorse('Text example'))
