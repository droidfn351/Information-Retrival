'''
Naive Based Text Classification
C is Edible or Poisonous
D is the document
'''
#Attribute values
attlist=[]
listval=[]
tmpist=[] #fro p(x)
#Training the data set
N=8124
C=['e','p']
prior=[float(4208)/N,float(3916)/N]
print prior
PE=float(4208)
PP=float(3916)


for i in range(0,22):
    attlist.append({})
    tmpist.append({})


listval.append(['b','c','x','f','k','s'])
listval.append(['f','g','y','s'])
listval.append(['n','b','c','g','r','p','u','e','w','y'])
listval.append(['t','f'])
listval.append(['a','l','c','y','f','m','n','p','s'])
listval.append(['a','d','f','n'])
listval.append(['c','w','d'])
listval.append(['b','n'])
listval.append(['k','n','b','h','g','r','o','p','u','e','w','y'])
listval.append(['e','t'])
listval.append(['b','c','u','e','?','z','r'])
listval.append(['f','y','k','s'])
listval.append(['f','y','k','s'])
listval.append(['n','b','c','g','o','p','e','w','y'])
listval.append(['n','b','c','g','o','p','e','w','y'])
listval.append(['p','u'])
listval.append(['n','o','w','y'])
listval.append(['n','o','t'])
listval.append(['c','e','f','l','n','p','s','z'])
listval.append(['k','n','b','h','r','o','u','w','y'])
listval.append(['a','c','n','s','v','y'])
listval.append(['g','l','m','p','u','w','d'])




for i in range(0,len(attlist)):
    for a in listval[i]:
        attlist[i][a]=[0,0]
        tmpist[i][a]=[0,0] 



# attlist contains the attribute dictonary along with the proboblity of the class

fo=open("agaricus-lepiota.data","r")
for lis in fo:
    lis=lis.replace(',',' ')
    docvcb=lis.split()
    flag=-1
    # vals[0] is P(e) and vals[1] is P(p)
    if(docvcb[0]=='e'):
        flag=0
    else:
        flag=1
    
   
    for i in range(1,len(docvcb)):
        tmp1=tmpist[i-1].get(docvcb[i])
        tmp=attlist[i-1].get(docvcb[i])
        tmp[flag]+=1
        tmp1[flag]+=1

#print attlist


for a in tmpist:
    vb=a.values()
    for v in vb:
        sum1=v[0]+v[1]
        if(sum1!=0):
            v[0]/=float(sum1)
            v[1]/=float(sum1)
          
        
for a in attlist:
    vb=a.values()
    for v in vb:
        v[0]/=PE
        v[1]/=PP
print attlist

print "Enter the Query String to be searched"
query=raw_input()
query=query.replace(',',' ')
qlist=query.split()
print qlist

ppe=float(1)
ppp=float(1)
for i in range(0,len(qlist)):
    
    if(qlist[i]!='-'):
        #print str(attlist[i])+"val="+str(qlist[i])
        val=attlist[i].get(qlist[i])
        cal=tmpist[i].get(qlist[i])
        print val
        print cal
        if val[0]!=float(0) and val[1]!=float(0):
            print val[1]!=float(0)
            ppe*=val[0]
            ppp*=val[1]
            ppe/=cal[0]
            ppp/=cal[1]
    else:
        continue
print ppe
print ppp
    

ppe*=prior[0]
ppp*=prior[1]
print "Final="+str(ppe)+"----->"+str(ppp)
if(ppe>ppp):
    print "Given Mushroom is edible"
else:
    print "Given Mushroom is poisonous"


