#!/bin/bash

rm -rf model
rm -rf model.output.txt

#rnn model is trained here
time ./rnnlm -train ./Train_data/TRAIN -valid ./Train_data/VALID -anti-kasparek 100000 -one-iter 1 -rnnlm save_model/rnn_model -hidden 50 -rand-seed 1 -debug 2 -bptt 4 -bptt-block 10 -direct-order 3 -direct 2 -binary

#ngram model is trained here, using SRILM tools
#../../srilm/bin/i686-m64/ngram-count -text O_Train -order 3 -lm templm -kndiscount -interpolate -gt3min 1 -gt4min 1
#../../srilm/bin/i686-m64/ngram -lm templm -order 3 -ppl test -debug 2 > temp.ppl

#gcc convert.c -O2 -o convert
#./convert <temp.ppl >srilm.txt

#combination of both models is performed here
#time ./rnnlm -rnnlm save_model/rnn_model -test O_Test -nbest #-lm-prob srilm.txt -lambda 0.5 -nbest
