import math
fo=open("vocabs12.txt")
fop=open("vocabs12tfi.txt","w+")
N=4

i=0
for lin in fo:
    n=0
    maxi=0
    lwrd=lin.split()
    #print lwrd
    fop.write(lin+"  tf=")
    tffile=[0,0,0,0]
    for i in range(0,len(lwrd)):
        
        if( lwrd[i].find('i1' ,0,len(lwrd[i]))==0):
            ir1=lwrd[i].replace('(',' ')
            ir1=ir1.replace(')',' ')
            ir2=ir1.split()
            if(maxi<ir2[1]):
                maxi=ir2[1]
            tffile[0]=ir2[1]
            n+=1
        if( lwrd[i].find('i2' ,0,len(lwrd[i]))==0):
            ir1=lwrd[i].replace('(',' ')
            ir1=ir1.replace(')',' ')
            ir2=ir1.split()
            if(maxi<ir2[1]):
                maxi=ir2[1]
            tffile[1]=ir2[1]
            n+=1
        if( lwrd[i].find('i3' ,0,len(lwrd[i]))==0):
            ir1=lwrd[i].replace('(',' ')
            ir1=ir1.replace(')',' ')
            ir2=ir1.split()
            if(maxi<ir2[1]):
                maxi=ir2[1]
            tffile[2]=ir2[1]
            n+=1
        if( lwrd[i].find('i4' ,0,len(lwrd[i]))==0):
            ir1=lwrd[i].replace('(',' ')
            ir1=ir1.replace(')',' ')
            ir2=ir1.split()
            if(maxi<ir2[1]):
                maxi=ir2[1]
            tffile[3]=ir2[1]
            n+=1
    for i in range(0,len(tffile)):
        tffile[i]=float(tffile[i])/float(maxi)
    #print "tf "+str(tffile)
    #print "idf "+str(math.log10(N/n))
    fop.write(str(tffile))
    fop.write("  idf="+str(math.log10(N/n))+"\n") 
    #x=input()
