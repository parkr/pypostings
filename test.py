from pyposting import *

# Text is courtesy of hipsteripsum.me, modified to be proper English (proper nouns capitalized and such).
test_corpus = """Cray gluten-free put a bird on it, Etsy reprehenderit odd future do fingerstache mollit bicycle rights bushwick vinyl lomo skateboard. American Apparel esse veniam, art party officia carles jean shorts Brooklyn Wes Anderson do. Aliqua ex American Apparel pickled. Shoreditch vinyl 8-bit biodiesel keytar nulla. Cliche occaecat iphone sartorial, Austin do yr magna jean shorts tattooed delectus. Exercitation salvia et kogi, pop-up brunch single-origin coffee. Adipisicing next level semiotics, duis consectetur organic trust fund magna sartorial ut nesciunt squid."""

test_corpus_posting = [
    ['Cray', 1],
    ['gluten-free', 2],
    ['put', 3],
    ['a', 4],
    ['bird', 5],
    ['on', 6],
    ['it', 7],
    ['Etsy', 8],
    ['reprehenderit', 9],
    ['odd', 10],
    ['future', 11],
    ['do', 12],
    ['fingerstache', 13],
    ['mollit', 14],
    ['bicycle', 15],
    ['rights', 16],
    ['bushwick', 17],
    ['vinyl', 18],
    ['lomo', 19],
    ['skateboard', 20],
    ['American', 21],
    ['Apparel', 22],
    ['esse', 23],
    ['veniam', 24],
    ['art', 25],
    ['party', 26],
    ['officia', 27],
    ['carles', 28],
    ['jean', 29],
    ['shorts', 30],
    ['Brooklyn', 31],
    ['Wes', 32],
    ['Anderson', 33],
    ['do', 34],
    ['Aliqua', 35],
    ['ex', 36],
    ['American', 37],
    ['Apparel', 38],
    ['pickled', 39],
    ['Shoreditch', 40],
    ['vinyl', 41],
    ['8-bit', 42],
    ['biodiesel', 43],
    ['keytar', 44],
    ['nulla', 45],
    ['Cliche', 46],
    ['occaecat', 47],
    ['iphone', 48],
    ['sartorial', 49],
    ['Austin', 50],
    ['do', 51],
    ['yr', 52],
    ['magna', 53],
    ['jean', 54],
    ['shorts', 55],
    ['tattooed', 56],
    ['delectus', 57],
    ['Exercitation', 58],
    ['salvia', 59],
    ['et', 60],
    ['kogi', 61],
    ['pop-up', 62],
    ['brunch', 63],
    ['single-origin', 64],
    ['coffee', 65],
    ['Adipisicing', 66],
    ['next', 67],
    ['level', 68],
    ['semiotics', 69],
    ['duis', 70],
    ['consectetur', 71],
    ['organic', 72],
    ['trust', 73],
    ['fund', 74],
    ['magna', 75],
    ['sartorial', 76],
    ['ut', 77],
    ['nesciunt', 78],
    ['squid', 79]
]

test_corpus_posting_list = {}

def test_posting():
    posting_ = posting(test_corpus)
    print posting_
    # ensure that the difference is 0
    print (test_corpus_posting == posting_)
    print ([item for item in test_corpus_posting if not item in posting_])

def test_posting_list():
    posting_list_ = posting_list(test_corpus)
    print posting_list_
    print (test_corpus_posting_list == posting_list_)
    
if __name__ == "__main__":
    test_posting()
    test_posting_list()