from collections import Counter
import port1
fo=open("vocabs12.txt")
ftsp=open("C:\Users\Sriram\Downloads\stop_word_list.txt")
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
print qpor.sort()

filcnt=[]
for lin in fo:
    lilis=lin.split()
    for x in qpor:
        if(lilis[0]==x):
            #print lilis
            maxi=1
            findex=""
            for j in range(1,len(lilis)):
                           tmp=lilis[j]
                           tmp=tmp.replace('(',' ')
                           tmp=tmp.replace(')',' ')
                           tmps=tmp.split()
                           if(int(maxi)<=int(tmps[1])):
                               maxi=int(tmps[1])
                               findex=tmps[0]
            print findex
            filcnt.append(findex)
print filcnt

print "Query can be found at "
c=Counter(filcnt)
val=max(c.itervalues())
for key in c:
    if c[key]==val:
        print key

