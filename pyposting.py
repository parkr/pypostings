import re, string

def posting(corpus):
    posting = []
    
    tokens = tokenize(corpus)
    for index, token in enumerate(tokens):
        # normalize token
        #   strip punctuation
        token = re.sub('\W\Z', '', token)
        posting.append([token, (index+1)])

    return posting

def posting_list(corpus):
    posting_list = {}
    
    tokens = tokenize(corpus)
    for index, token in enumerate(tokens):
        # normalize token
        #   strip punctuation
        token = re.sub('\W\Z', '', token)
        token = re.sub('\A\W', '', token)
        if token not in posting_list:
            posting_list[token] = [(index + 1)]
        else:
            posting_list[token].append(index + 1)
    
    return posting_list

# _____________________________________________________________________________
# Helper Methods

def tokenize(corpus):
    check_corpus_type(corpus)
    tokenized = filter(not_string, re.split(r'(\s)', corpus))
    return tokenized

def check_corpus_type(corpus=None):
    if type(corpus) is not str:
        raise TypeError("Corpus must be a string of characters.")

def not_string(a):
    return a != " " and a != ""