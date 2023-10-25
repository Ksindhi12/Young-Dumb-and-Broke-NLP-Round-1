from pre_processing import runPreprocessing
from tokenization import runTokenization
from stop_words_removal import removeStopWords
from freq_distribution_of_tokens import PrintFrequencyDistribution, VisualiseFrequencyDistribution, CreateWordCloud
from pos_tagging import PerformPOSTagging, GetFrequencyDistributionOfTags
import random
from bigram_modelling import generateBigrams, CreateAndPrintBigramProbabilityTable
from shannon_game import CreateBlanksForShannonGame, PlayingTheShannonGame

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
CreateWordCloud(tokenisedTextWithoutStopwords)

PerformPOSTagging(tokenisedTextWithoutStopwords)
GetFrequencyDistributionOfTags(tokenisedTextWithoutStopwords)

randomlySelected10chapters = random.sample(range(1, len(preprocessedTextChapters)), 10)
trainingSetForBigramModel = ""
for chapterNumber in randomlySelected10chapters:
    trainingSetForBigramModel += preprocessedTextChapters[chapterNumber]

trainingSetForBigramModel = runTokenization(trainingSetForBigramModel)

bigrams = generateBigrams(trainingSetForBigramModel)
bigramProbabiltyTable = CreateAndPrintBigramProbabilityTable(bigrams, trainingSetForBigramModel)

distinct_tokens = list(set(sorted(trainingSetForBigramModel)))
preprocessedTextChaptersNotPartOfTheTrainingSet = []

for chapterNumber in range(len(preprocessedTextChapters)):
    if(chapterNumber not in randomlySelected10chapters):
        preprocessedTextChaptersNotPartOfTheTrainingSet.append(preprocessedTextChapters[chapterNumber])

testPreprocessedTextChapter = random.choice(preprocessedTextChaptersNotPartOfTheTrainingSet)
testTokenSetForShannonGame = runTokenization(testPreprocessedTextChapter)
testTokenSetForShannonGameWithBlanks, originalTokens = CreateBlanksForShannonGame(testTokenSetForShannonGame, 50)
PlayingTheShannonGame(testTokenSetForShannonGameWithBlanks, bigramProbabiltyTable, 50, distinct_tokens, originalTokens)
