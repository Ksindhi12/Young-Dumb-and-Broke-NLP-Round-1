import nltk
import random
import sys


def CreateBlanksForShannonGame(tokens:list, num_blanks:int):
    blank_positions = random.sample(range(1, len(tokens)), num_blanks)
    blank_positions.sort()
    originalTokens = []
    for i in blank_positions:
        originalTokens.append(tokens[i])
        tokens[i] = "_"
    return tokens, originalTokens

def PlayingTheShannonGame(tokens: list, bigramProbabilityTable, num_blanks, distinct_tokens: list, originalTokens):
    ogTokenIndex = -1
    correctlyFilledBlanks = num_blanks
    for i in range(len(tokens)):
        if(tokens[i] == "_"):
            ogTokenIndex += 1
            try:
                previousWordIndex = i - 1
                maxProb = -sys.maxsize
                list_index = distinct_tokens.index(tokens[previousWordIndex])
                for prob in bigramProbabilityTable[list_index]:
                    maxProb = max(prob, maxProb)
                indexOfTokenToBeReplaced = bigramProbabilityTable[list_index].index(maxProb)
                if(distinct_tokens[indexOfTokenToBeReplaced] != originalTokens[ogTokenIndex]):
                    correctlyFilledBlanks -= 1
            except:
                correctlyFilledBlanks -= 1           
    GetPerformanceOfBigramModel(correctlyFilledBlanks, num_blanks)


def GetPerformanceOfBigramModel(correctlyFilledBlanks, num_blanks):
    print(correctlyFilledBlanks)
    print(num_blanks)
    accuracyOfModel = (correctlyFilledBlanks / num_blanks) * 100
    print("Accuracy of the bigram model generated is: ")
    print(accuracyOfModel)