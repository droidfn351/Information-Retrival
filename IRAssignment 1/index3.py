#Index Construction of all four text files

fps=open("vocabs12.txt","w+")
fo=open("stemt1.txt")
str1=fo.read
for lin in fo:
    lis1=lin.split()
lis1.sort()
fo.close()

fo=open("stemt2.txt")
str1=fo.read
for lin in fo:
    lis2=lin.split()
lis2.sort()
fo.close()

fo=open("stemt3.txt")
str1=fo.read
for lin in fo:
    lis3=lin.split()
lis3.sort()
fo.close()

fo=open("stemt4.txt")
str1=fo.read
for lin in fo:
    lis4=lin.split()
lis4.sort()
fo.close()



for i in range(0,len(lis1)):
    lis1[i]=lis1[i]+" i1"
for i in range(0,len(lis2)):
    lis2[i]=lis2[i]+" i2"
for i in range(0,len(lis3)):
    lis3[i]=lis3[i]+" i3"
for i in range(0,len(lis4)):
    lis4[i]=lis4[i]+" i4"


final=lis1+lis2+lis3+lis4
final.sort()
#print final

i=0
while(i<len(final)):
    cnt=1
    j=i+1
    stri=final[i]
    #print "final"+final[i]
    tmpsp=final[i].split()
    while(j<len(final)):
        #print "j= "+final[j]
        jf=final[j].split()
        if(tmpsp[0]==jf[0] and tmpsp[1]==jf[1]):
            #print "enter"
            cnt+=1
            j+=1
        elif(tmpsp[0]==jf[0] and tmpsp[1]<>jf[1]):
            tmpsp[1]=jf[1]
            stri+='('+str(cnt)+')'+' '+jf[1]
            cnt=1
            j+=1
        else:
            stri+='('+str(cnt)+')'
            #print stri
            fps.write(stri+'\n')
            break
       
    i=j
fps.close()
