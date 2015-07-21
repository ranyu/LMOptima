from sklearn import preprocessing
from nolearn.dbn import DBN
import numpy
import cPickle
from sklearn.cross_validation import train_test_split

train_x = numpy.load('data/fuck_fbank_X_n.npy')
test_x = numpy.load('data/fuck_fbank_test_n.npy')
train_y = numpy.load('data/1943_label.npy')

print train_x.shape
print train_y.shape
print test_x.shape

(train_x,vali_x,train_y,vali_y) = train_test_split(train_x,train_y,test_size = 0.2)

dbn = DBN(
        [759,1024,1943],
        learn_rates = 0.025,
        learn_rate_decays = 0.98,
        l2_costs = 0.0001,
        minibatch_size=256,
        epochs=10,
        momentum = 0.9,
        #dropouts=0.22,
        verbose = 2)

dbn.fit(train_x, train_y)
print 'validation score is:' ,dbn.score(vali_x,vali_y)

#predicted_y_proba = dbn.predict_proba(test_x)


#if __name__ == "__main__":
    #p_proba_str = cPickle.dumps(predicted_y_proba)
    '''import sys
    file_name = sys.argv[1]
    with open(file_name, 'w') as a:
        a.write(p_proba_str)'''

