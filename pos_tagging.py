import nltk
nltk.download('punkt')
import pandas
import matplotlib.pyplot as plt
import seaborn
nltk.download('averaged_perceptron_tagger')


def PerformPOSTagging(tokens:list):
    taggedTokens = []
    taggedTokens += nltk.pos_tag(tokens)
    #GetFrequencyDistributionOfTags(taggedTokens)
    #for token in taggedTokens:
    #    print(token)

def GetFrequencyDistributionOfTags(tokens: list):
    taggedToken = nltk.pos_tag(tokens)
    tagFreqDistribution = nltk.FreqDist(tag for (word, tag) in taggedToken)
    tagFreqDistribution.plot(10)
    tagFreqDistribution.tabulate()