#!/bin/bash

#rm -rf model
#rm -rf model.output.txt

#rnn model is trained here
#time ./rnnlm -train ../data/Train_data/TRAIN -valid ../data/Train_data/VALID -anti-kasparek 500000 -rnnlm ../save_model/rnn_model_moreiter -hidden 50 -rand-seed 1 -debug 2 -bptt 4 -bptt-block 10 -direct-order 3 -direct 2 -binary

#ngram model is trained here, using SRILM tools
#../../../srilm/bin/i686-m64/ngram-count -text ../data/Train_data/TRAIN -order 5 -lm templm -kndiscount -interpolate -gt3min 1 -gt4min 1
../../../srilm/bin/i686-m64/ngram -lm ../templm -order 5 -ppl ../result/sys_result -debug 2 > temp.ppl

python get_ngram.py temp.ppl

#combination of both models is performed here
time ../rnnlm -rnnlm ../../save_model/rnn_model -test ../result/sys_result -lm-prob srilm.txt -lambda 1 -nbest
