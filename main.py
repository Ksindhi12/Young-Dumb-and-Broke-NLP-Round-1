from pre_processing import runPreprocessing
from tokenization import runTokenization
from stop_words_removal import removeStopWords
from freq_distribution_of_tokens import PrintFrequencyDistribution, VisualiseFrequencyDistribution

orignalFile = open('Pride_and_Prejudice.txt', 'r')
content = orignalFile.read()

preprocessedTextChapters = runPreprocessing(content)

preprocessedText= ""
for i in preprocessedTextChapters:
    preprocessedText = preprocessedText + i + "\n"

tokenizedText = runTokenization(preprocessedText)
print(len(removeStopWords(tokenizedText)))

tokenisedTextWithoutStopwords = removeStopWords(tokenizedText)

PrintFrequencyDistribution(tokenisedTextWithoutStopwords)
VisualiseFrequencyDistribution(tokenisedTextWithoutStopwords)



