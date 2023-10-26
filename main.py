# Import necessary modules and functions from all the other modules
from pre_processing import runPreprocessing
from tokenization import runTokenization
from stop_words_removal import removeStopWords
from freq_distribution_of_tokens import GetFrequencyDistribution, VisualiseFrequencyDistribution, CreateWordCloud
from pos_tagging import PerformPOSTagging, GetFrequencyDistributionOfTags
import random
from bigram_modelling import generateBigrams, CreateBigramProbabilityTable
from shannon_game import CreateBlanksForShannonGame, PlayingTheShannonGame

# Import all the content of the selected book and open it in read mode 
orignalFile = open('Pride_and_Prejudice.txt', 'r')
content = orignalFile.read()

# Run preprocessing on the content to prepare NLP ready data
preprocessedTextChapters = runPreprocessing(content)

# Combine preprocessed chapters into a single string data structure
preprocessedText= ""
for i in preprocessedTextChapters:
    preprocessedText = preprocessedText + i + "\n"

# Tokenize the preprocessed text 
tokenizedText = runTokenization(preprocessedText)

# Remove stopwords from the tokenized text
tokenisedTextWithoutStopwords = removeStopWords(tokenizedText)

# Print and visualize the frequency distribution of tokens using BarGraphs and Frequency Distributions
tokenFD = GetFrequencyDistribution(tokenisedTextWithoutStopwords)
VisualiseFrequencyDistribution(tokenFD)

# Create a word cloud from the tokenized text to visualise its frequency distribution
CreateWordCloud(tokenisedTextWithoutStopwords)

# Perform Part-of-Speech (POS) tagging on the tokenized text using the default penn-treebank tagset 
taggedTokens = PerformPOSTagging(tokenisedTextWithoutStopwords)

#Analysing the frequency distrinution of the most frequent tags using plots
GetFrequencyDistributionOfTags(taggedTokens)

# Randomly select 10 chapters for the bigram model training set and merge them into a sinlge string of text
randomChapterIndexes = random.sample(range(1, len(preprocessedTextChapters)), 10)
trainingSetForBigramModel = ""
for chapterNumber in randomChapterIndexes:
    trainingSetForBigramModel += preprocessedTextChapters[chapterNumber]

# Tokenize the training set for bigram modeling without removing the stop words 
trainingSetForBigramModel = runTokenization(trainingSetForBigramModel)

# Generate bigrams from the training set
bigrams = generateBigrams(trainingSetForBigramModel)

# Create and print a bigram probability table
bigramProbabiltyTable = CreateBigramProbabilityTable(bigrams, trainingSetForBigramModel)

# Extract distinct tokens from the training set useful in the shannon game module
distinct_tokens = list(set(sorted(trainingSetForBigramModel)))

preprocessedTextChaptersForTesting = []
# Iterate through chapters and add chapters not in the training set to the list
for chapterNumber in range(len(preprocessedTextChapters)):
    if chapterNumber not in randomChapterIndexes:
        preprocessedTextChaptersForTesting.append(preprocessedTextChapters[chapterNumber])

# Randomly select a test chapter from the chapters not used in training
testPreprocessedTextChapter = random.choice(preprocessedTextChaptersForTesting)

# Tokenize the test chapter for the Shannon game
testTokenSetForShannonGame = runTokenization(testPreprocessedTextChapter)

# Create blanks in the test token set for the Shannon game and store original tokens that the blanks replaced
testTokenSetWithBlanks, originalTokens = CreateBlanksForShannonGame(testTokenSetForShannonGame, 50)

# Play the Shannon game with the test token set and get the accuracy of the bigram model trained above
PlayingTheShannonGame(testTokenSetWithBlanks, bigramProbabiltyTable, 50, distinct_tokens, originalTokens)
