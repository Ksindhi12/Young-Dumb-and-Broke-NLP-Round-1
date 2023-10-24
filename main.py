from pre_processing import runPreprocessing

orignalFile = open('Pride_and_Prejudice.txt', 'r')
content = orignalFile.read()

preprocessedTextChapters = runPreprocessing(content)
preprocessedText= ""
for i in preprocessedTextChapters:
    preprocessedText = preprocessedText + i + "\n"




