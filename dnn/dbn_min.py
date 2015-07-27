from sklearn import preprocessing
from nolearn.dbn import DBN
import numpy
import cPickle
from sklearn.cross_validation import train_test_split

train_x = numpy.load('data/X_train.npy')
test_x = numpy.load('data/X_test.npy')
train_y = numpy.load('data/Y_train.npy')

print train_x.shape
print train_y.shape
print test_x.shape

(train_x,vali_x,train_y,vali_y) = train_test_split(train_x,train_y,test_size = 0.2)

dbn = DBN(
        [300,1024,120000],
        learn_rates = 0.025,
        learn_rate_decays = 0.98,
        l2_costs = 0.0001,
        minibatch_size=256,
        epochs=5,
        momentum = 0.9,
        #dropouts=0.22,
        verbose = 2)

dbn.fit(train_x, train_y)
print 'validation score is:' ,dbn.score(vali_x,vali_y)

result = dbn.predict(test_x)
with open('data/result','w') as f:
    for el in result:
        f.write(el+'\n')

#predicted_y_proba = dbn.predict_proba(test_x)


#if __name__ == "__main__":
    #p_proba_str = cPickle.dumps(predicted_y_proba)
    '''import sys
    file_name = sys.argv[1]
    with open(file_name, 'w') as a:
        a.write(p_proba_str)'''

