CC = gcc
#Using -Ofast instead of -O3 might result in faster code, but is supported only by newer GCC versions
CFLAGS =  -lm -pthread -O3  -Wall -funroll-loops -Wno-unused-result

all: word2vec modifyword2vec testw2v word2phrase distance word-analogy compute-accuracy

word2vec : word2vec.c
	$(CC) word2vec.c -o word2vec $(CFLAGS)
modifyword2vec : modword2vec.c
	$(CC) modword2vec.c -o modifyword2vec $(CFLAGS)
testw2v : testw2v.c
	$(CC) testw2v.c -o testw2v $(CFLAGS)
word2phrase : word2phrase.c
	$(CC) word2phrase.c -o word2phrase $(CFLAGS)
distance : distance.c
	$(CC) distance.c -o distance $(CFLAGS)
word-analogy : word-analogy.c
	$(CC) word-analogy.c -o word-analogy $(CFLAGS)
compute-accuracy : compute-accuracy.c
	$(CC) compute-accuracy.c -o compute-accuracy $(CFLAGS)
	chmod +x *.sh

clean:
	rm -rf word2vec modifyword2vec testw2v word2phrase distance word-analogy compute-accuracy
