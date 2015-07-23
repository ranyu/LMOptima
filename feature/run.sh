zcat *.gz >> bbs_cor
echo 'finish gz to text'
python3 read_corpus.py bbs_cor >> bbs_sen
rm bbs_cor
