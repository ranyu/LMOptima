#!/bin/bash

#rnn model is trained here
time ./rnnlm -train O_Train -valid O_Valid -rnnlm model -hidden 50 -rand-seed 1 -debug 2  -bptt 4 -bptt-block 10 -direct-order 3 -direct 2 -binary
