
def uni(s):
    if isinstance(s, unicode):
        print s.encode('gb2312')
    else:
        print s.decode('utf-8').encode('gb2312')


with open('head_100','r') as f:
    for data in f:
        print data.strip().split()[0]
        print uni(data.strip().split()[0])
        raw_input()
