import gensim
from word2vecget import get_word2vec

get_word2vec()
print("Word2vec Downloaded and Unzipped Successfully")
print("Loading Word2vec...")
def make_word2vec():
    model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

    words = model.index2word
    w_rank = {}
    for i,word in enumerate(words):
        w_rank[word] = i
    WORDS = w_rank
    return WORDS

    