import random, sys

inputFile = ""
csl = 1
outputLength = 10

if len(sys.argv) == 4:
    inputFile = open(sys.argv[1])
    csl = int(sys.argv[2])
    outputLength = int(sys.argv[3])
else:
    inputFile = open(input("Enter file path (ex: C:\\Users\\user\\Desktop\\names.txt): "))
    csl = int(input("Enter markov chain seed length: "))
    outputLength = int(input("Enter output length in characters: "))

inputText = []
inputText = inputFile.read()
inputText = "\n" + inputText + "\n"
inputText = inputText.replace("\n","\n"*csl)
inputText = inputText.lower()
    
markovDict = dict()


for index in range(len(inputText)-(csl-1)):
    if inputText[index:index+csl] not in markovDict:
        markovDict[inputText[index:index+csl]] = dict()

for index in range(len(inputText)-(csl)):
    if inputText[index + csl] in markovDict[inputText[index:index+csl]]:
        markovDict[inputText[index:index+csl]][inputText[index+csl]] += 1
    else:
        markovDict[inputText[index:index+csl]][inputText[index+csl]] = 1


#balance probabilities
for key in markovDict:
    keySum = 0
    for character in markovDict[key]:
        keySum += markovDict[key][character]
    cumProb = 0
    for character in markovDict[key]:
        markovDict[key][character] /= keySum
        markovDict[key][character] += cumProb
        cumProb = markovDict[key][character]
    
#output markov generations
outputString = "\n"*csl
for i in range(outputLength):
    randomNumber = random.random()
#    print(markovDict[outputString[len(outputString)-csl:]])
    for key in markovDict[outputString[len(outputString)-csl:]]:
        if randomNumber <= markovDict[outputString[len(outputString)-csl:]][key]:
            outputString += key
            break

outputString = outputString.replace("\n"*csl,"\n")
print(outputString)
input("Press enter to close.")