import numpy as np
from sklearn import svm
# Function that takes a sequence as an input and creates an input vector to sklearn
#1st parser to read the input file and slip it it into 3 lists of ids, sequences, and states

def parser(filename):
    #mydict={]    
    mydict1={}
    mydict2={}
    fulldict={}
    ids=[]
    seq=[] 
    states=[] 
      
    parser = dict()
    filereader = open(filename,'r')
    text = filereader.read().splitlines()                                                                               
   
    
    for i in range (0, len(text), 3):
        ids.append(text[i].lstrip ('>'))
        seq.append(text[i+1])
        states.append(text[i+2])
  
    #mydict = dict(zip(ids, [seq,states]))  ### why does this take only the 1st prot name but no the rest? 
    mydict1 = dict(zip(ids, seq)) 
    mydict2 = dict(zip(ids, states))

    for key in mydict1.keys() & mydict2.keys():
        fulldict [key] = (mydict1[key], mydict2[key])
       
  
    #text.close()
    print (fulldict)



# sliding window

winsize = 31 # it should be an odd integer >= 3 input
hwinsize= float(winsize/2)

windlist= []


#for i in seq:
    #i = ((hwinsize)*'0')+i+((hwinsize)*'0')
    #for j in range(0, len(i)):
        #if j+(winsize) > len(i):
         #   break
        #temp = i[j:j+(winsize)]
#i.append(temp)
 
#https://stackoverflow.com/questions/8269916/what-is-sliding-window-algorithm-examples


#mapping

prot = list('ACDEFGHIKLMNPQRSTVWY') 
states_dict = {1:'H', 2:'S', 3:'C'}
aa_dict = {'A': 1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'K':9, 'L':10, 'M':11, 'N':12, 'P':13, 'Q':14, 'R':15, 'S':16, 'T':17, 'V':18, 'W':19, 'Y':20}
	

	






if __name__=="__main__":
 print (parser('jpred1.3line.txt'))



























