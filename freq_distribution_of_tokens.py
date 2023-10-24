import nltk
import pandas
import seaborn
import matplotlib.pyplot

def PrintFrequencyDistribution(tokens:list):
    TokenFD = nltk.FreqDist(tokens)
    for token in list(TokenFD.items()):
        print(token[0], token[1])
    print("X-------------------------------------------------X-------------------------------------------------X")

def VisualiseFrequencyDistribution(tokens:list):
    mostCommonFdist = nltk.FreqDist(tokens).most_common(20)
    mostCommonFdist = pandas.Series(dict(mostCommonFdist))
    figure, ax = matplotlib.pyplot.subplots(figsize = (10,10))

    freqDistribution_plot = seaborn.barplot(x = mostCommonFdist.index, y = mostCommonFdist.values, ax = ax)
    matplotlib.pyplot.xticks(rotation = 30)






