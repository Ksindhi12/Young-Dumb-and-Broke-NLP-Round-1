import nltk
# nltk.download()

def runTokenization(text:str):
    return nltk.tokenize.word_tokenize(text)
