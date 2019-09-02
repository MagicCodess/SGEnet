import wget
import gzip


#Downloading word2vec
def get_word2vec():
    print("Downloading  Word2vec...")
    url = "https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz"
    wget.download(url)
    
    #Unzip word2vec
    print("\n")
    print("Unziping Word2vec")
    input = gzip.GzipFile("GoogleNews-vectors-negative300.bin.gz", 'rb')
    s = input.read()
    input.close()
    
    print("\n")
    output = open("GoogleNews-vectors-negative300.bin", 'wb')
    output.write(s)
    output.close()
