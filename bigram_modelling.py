import nltk
import random

def generateBigrams(tokens:list):
    tokenBigrams = nltk.ngrams(tokens, 2)
    bigrams = list(tokenBigrams)
    print("\n")
    print("Total number of Bigrams: ")
    print(len(bigrams))
    print("\nSome Examples of Bigrams:\n")
    print(bigrams[:20], "......")
    return bigrams


def CreateAndPrintBigramProbabilityTable(bigrams: list, tokens: list):
    bigramFD = nltk.FreqDist(bigrams)
    bigramFD.plot(10)
    print("\nSome Bigram counts and frequency distribution:")
    bigramFDMostCommon = bigramFD.most_common(20)
    for bigram in bigramFDMostCommon:
        print(bigram)
    distinct_tokens = list(set(sorted(tokens)))
    token_dct = dict(nltk.FreqDist(tokens))
    bigram_dct = dict(bigramFD)
    bigramProbabiltyTable = CalculateBigramProbabilitiesAndPrintProbabilityTable(distinct_tokens, token_dct, bigram_dct)
    return bigramProbabiltyTable


def FindBigram(bigram : tuple, bigram_dct: dict):
    try:
        return bigram_dct[bigram]
    except:
        return 0


def CalculateBigramProbabilitiesAndPrintProbabilityTable(distinct_tokens:list, token_dct: dict, bigram_dct: dict):
    n = len(distinct_tokens)
    bigramProbabilityDistribution = [[]*n for i in range(n)]
    for i in range(n):
        countOfPreviousWord = token_dct[distinct_tokens[i]]
        for j in range(n):
            bigram = (str(distinct_tokens[i]), str(distinct_tokens[j]))
            countOfTheBigram = FindBigram(bigram, bigram_dct)
            bigramProbabilityDistribution[i].append(float("{:.3f}".format(countOfTheBigram/countOfPreviousWord)))
    PrintBigramProbabilityTable(bigramProbabilityDistribution, distinct_tokens)
    return bigramProbabilityDistribution
    

def PrintBigramProbabilityTable(bigramProbabiltyTable, distinct_tokens):
    n = len(distinct_tokens)
    print("Probability Table = \n")
    print("\t", end = "")
    randomList = random.sample(range(0, len(distinct_tokens)), 10)
    for i in randomList:
        print(distinct_tokens[i], end = "\t")
    print("\n")
    for i in randomList:
        print(distinct_tokens[i], end = "\t")
        for j in randomList:
            print(bigramProbabiltyTable[i][j], end = "\t")
        print("\n")
    zeroCount = 0
    for i in range(n):
        for j in range(n):
            if(bigramProbabiltyTable[i][j] != 0.0):
                zeroCount += 1
    print(zeroCount)
    print(n*n)
    print(zeroCount/(n*n))
