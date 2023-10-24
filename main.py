from pre_processing import runPreprocessing
from tokenization import runTokenization

orignalFile = open('Pride_and_Prejudice.txt', 'r')
content = orignalFile.read()

preprocessedTextChapters = runPreprocessing(content)

preprocessedText= ""
for i in preprocessedTextChapters:
    preprocessedText = preprocessedText + i + "\n"

tokenizedText = runTokenization(preprocessedText)
print(len(tokenizedText))




