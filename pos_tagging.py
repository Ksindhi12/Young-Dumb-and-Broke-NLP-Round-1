import nltk

nltk.download("universal_tagset")


def runPOSTagging(tokens):
    return nltk.pos_tag(tokens)