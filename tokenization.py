import nltk
nltk.download('punkt')

def runTokenization(text:str):
    return nltk.tokenize.word_tokenize(text)
