from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
def removeStopWords(tokens:list):
    stop_words = set(stopwords.words('english'))
    finalList = [word for word in tokens if word not in stop_words]
    
    return finalList