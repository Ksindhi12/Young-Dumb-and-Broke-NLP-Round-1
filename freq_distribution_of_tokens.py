from wordcloud import WordCloud, STOPWORDS
import nltk
import pandas
import seaborn
import matplotlib.pyplot as plt


def PrintFrequencyDistribution(tokens:list):
    TokenFD = nltk.FreqDist(tokens)
    for token in list(TokenFD.items()):
        print(token[0], token[1])
    print("X-------------------------------------------------X-------------------------------------------------X")

def VisualiseFrequencyDistribution(tokens:list):
    mostCommonFdist = nltk.FreqDist(tokens).most_common(20)
    mostCommonFdist = pandas.Series(dict(mostCommonFdist))
    figure, ax = plt.pyplot.subplots(figsize = (10,10))

    freqDistribution_plot = seaborn.barplot(x = mostCommonFdist.index, y = mostCommonFdist.values, ax = ax)
    plt.pyplot.xticks(rotation = 30)

def CreateWordCloud(tokens:list):
    wordcloud = WordCloud(width = 800, height = 800, background_color = 'white', min_font_size = 10).generate(tokens)
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()






