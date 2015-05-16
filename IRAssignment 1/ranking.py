from collections import Counter
import port1
import operator
fo=open("vocabs12.txt")
ftsp=open("C:\Users\Sriram\Downloads\stop_word_list.txt")
fp1=open("vocabs121tfi.txt")
for str1 in ftsp:
    stop=str1.split()
query=raw_input()
query=query.replace(',',' ')
query=query.replace('.',' ')
query=query.replace(':',' ')
query=query.replace(';',' ')
query=query.replace('[',' ')
query=query.replace(']',' ')
query=query.replace('_',' ')
query=query.replace('-',' ')
query=query.replace('(',' ')
query=query.replace(')',' ')
query=query.replace('*',' ')
query=query.replace('"',' ')
query=query.replace('?',' ')
query=query.replace('!',' ')
query=query.replace("'s"," ")
query=query.replace('/',' ')
query=query.replace('*',' ')
query=query.replace('+',' ')
query=query.replace('0',' ')
query=query.replace('1',' ')
query=query.replace('2',' ')
query=query.replace('3',' ')
query=query.replace('4',' ')
query=query.replace('5',' ')
query=query.replace('6',' ')
query=query.replace('7',' ')
query=query.replace('8',' ')
query=query.replace('9',' ')
query=query.replace('the',' ')
query=query.replace('#',' ')
query=query.replace('&',' ')
query=query.replace('}',' ')
query=query.lower()

qlist=query.split()
#print qlist
qls=""
if(qlist!=0):
    for x in qlist:
        flag=1
        for y in stop:
            if(y==x):
                flag=0
                break
        if(flag==1 and x!=' '):
            qls+=x+" "
print qls
qlist=qls.split()
qpor=[]
for a in qlist:
    qpor.append(port1.stem(a))
print qpor

ranking=[0.0,0.0,0.0,0.0]
for lin in fp1:
    lsi=lin.split()
    for a in qpor:
        if(a==lsi[0]):
         for i in range(0,4):
             ranking[i]+=float(lsi[i+1])
print ranking

dictrnk={1:ranking[0],2:ranking[1],3:ranking[2],4:ranking[3]}
print dictrnk

sorted_x = sorted(dictrnk.items(), key=operator.itemgetter(1))
#print sorted_x

print "Document rankings:"
i=len(sorted_x)-1
while i>=0:
    print sorted_x[i]
    i-=1

