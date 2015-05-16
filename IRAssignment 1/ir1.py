#Program to remove stop words and punctuations
fo=open("Text4.txt")
fp=open("tmp.txt","w+")
ftsp=open("C:\Users\Sriram\Downloads\stop_word_list.txt")
for str1 in ftsp:
    stop=str1.split()
print stop
for lin in fo:

    lin=lin.replace(',',' ')
    lin=lin.replace('.',' ')
    lin=lin.replace(':',' ')
    lin=lin.replace(';',' ')
    lin=lin.replace('[',' ')
    lin=lin.replace(']',' ')
    lin=lin.replace('_',' ')
    lin=lin.replace('_',' ')
    lin=lin.replace('(',' ')
    lin=lin.replace(')',' ')
    lin=lin.replace('*',' ')
    lin=lin.replace('"',' ')
    lin=lin.replace('?',' ')
    lin=lin.replace('!',' ')
    lin=lin.replace("'s"," ")
    lin=lin.replace('-',' ')
    lin=lin.replace('/',' ')
    lin=lin.replace('*',' ')
    lin=lin.replace('+',' ')
    lin=lin.replace('0',' ')
    lin=lin.replace('1',' ')
    lin=lin.replace('2',' ')
    lin=lin.replace('3',' ')
    lin=lin.replace('4',' ')
    lin=lin.replace('5',' ')
    lin=lin.replace('6',' ')
    lin=lin.replace('7',' ')
    lin=lin.replace('8',' ')
    lin=lin.replace('9',' ')
    lin=lin.replace('the',' ')
    lin=lin.replace('#',' ')
    lin=lin.replace('&',' ')
    lin=lin.replace('}',' ')
    lin1=(str(lin)).lower()
    #print lin1
    
    
    lins=lin1.split()
    #print lins
         
   
    if(lins!=0):
       for x in lins:
            flag=1
            for y in stop:
               if(y==x):
                    flag=0
                    break
            if(flag==1 and x!=' '):
               fp.write(x+" ")
           
       
