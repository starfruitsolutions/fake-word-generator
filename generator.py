import random
import string

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
startBlends = ['bl', 'br', 'cl', 'cr', 'dr', 'fr', 'tr', 'fl', 'gl', 'gr', 'pl', 'pr', 'sl', 'sm', 'sp', 'st']
endBlends = ['ll', 'tt', 'ck', 'rt', 'rst', 'st', 'ble', 'nd', 'nk', 'nt', 'ng', 'mp', 'sk', 'ft', 'ct', 'pt', 'lt', 'lk', 'ld', 'lf', 'lp', 'lm', 'rm', 'rn', 'rp', 'rt', 'rd', 'rf', 'rk', 'rl', 'mb']
digraphs = ['sh', 'ch', 'th', 'wh', 'ph']
vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'ai', 'ae', 'ao', 'au', 'ay', 'ea', 'ee', 'ey', 'ia', 'ie', 'io', 'oa', 'oi', 'ou','oy', 'ua', 'ui', 'uo', 'uy' ]
endings = ['s','x', 'z']
minLength = 1
maxLength = 7

numberOfWords = 500

def newLetter (isVowel, position, length):
    return (if isVowel:
        random.choice(vowels)
    else:
        isBlend = random.randint(0,1)
        if isBlend:
            if position == 0:
                random.choice(startBlends)
            elif position > length - 1:
                random.choice(endBlends)
            else:
                random.choice(startBlends + endBlends)
        else:
            random.choice(consonants + digraphs)
    )

def generateWord():
    #pick some random shit and end with a random ending
    length = random.randint(minLength, maxLength)
    word = ''
    isVowel = random.randint(0,1)

    while len(word)  < length:
        #add shit
        word += newLetter(isVowel, len(word), length)
        isVowel = not isVowel        

    #add ending
    #word += random.choice(endings)
    return word

words = []
for n in range(numberOfWords):
    words.append(generateWord())

paragraph = ''
for word in words:
    paragraph += ' ' + word

 
print(words)
print(paragraph)