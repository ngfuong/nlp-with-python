from nltk.book import *

if __name__ == "__main__":
    bigram_list = bigrams(["more", "is", "said", "than", "done"])
    for item in bigram_list:
        print(item, end=' ')

    fdist = FreqDist(text4)
    text4.collocations()
    fdist.tabulate()
    text9.index()
    list1 = ['a', 'b']
    list1.index()