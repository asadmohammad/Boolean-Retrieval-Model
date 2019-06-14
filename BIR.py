# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 12:00:05 2019

@author: Mohammad Asad
"""

import re
import json
from functools import reduce



def splitWords(string):
    words = []
    words = re.split('\W+',string)
    return words

def tokeniseWords(wordList):
    newWord = []
    newWord = re.sub(r'[^\w]', '', wordList)
    #print(newWord)
    return newWord
    

def toLowerCase(wordList):
    i = 0
    lowCaseWord = []
    for word in wordList:
        i = i + 1
        lcWord = word.lower()
        lowCaseWord.append((i, lcWord))
    return lowCaseWord
    #print(lowCaseWord)
    #removeStopWords(lowCaseWord)
    

def removeStopWords(words):
    #emp = ''
    stopWords = ['is','a','the','of','all','and','to','can','be','as','once','for',
                 'at','am','are','has','have','had','up','his','her','in','on','no','we','do']
    i = 0
    wordsWoSW = []
    for i, word in words:
        if word in stopWords:
            continue
        wordsWoSW.append((i,word))
    return wordsWoSW
    #print(lowCaseWord)


def readFromFile():
    stories = []
    for i in range(0,50):
        f = open("F:\\Subjects\\Python-WORKSPACE\\IRP1\\Short Stories\\" +str(i+1) + ".txt", "r")
        string = f.read()
        stories.append(string)
        del string
        #print("****")
    
    return stories


def menuEmulat(string):
    words = splitWords(string)
    words = toLowerCase(words)
    words = removeStopWords(words)
    #words = tokeniseWords(words)
    #print(words)
    return words

def fetchDoc(invInd, query):
    wordList = [tok for _, tok in menuEmulat(query) if tok in invInd]
    fetchedResults = [set(invInd[tok].keys()) for tok in wordList]
    fdDocs = reduce(lambda tok,key : tok & key,fetchedResults) if fetchedResults else[]
    return fdDocs




def trialInvInd(words):
    invInd = {}           #Dictionary
    for i, word in menuEmulat(words):
        positions = invInd.setdefault(word,[])         #value of item with key/ Dictionary
        positions.append(i)                             #storing positions of word in a document
    return invInd

def invertedIndex(invInd, postings, lex):
    for word, pos in lex.items():
        i = invInd.setdefault(word,{})         #Setting dictionary for each 
        i[postings] = pos
    return invInd

def andOp(queryTerms):
    i = 0
    #noTerms = len(queryTerms)
    #tAr = [[] for _ in range(noTerms)]
    tempAr = []
    tempAr1 = []
    for query in queryTerms:
        resultSet = fetchDoc(inv_Index,query)
            
        #print ("'%s' Appears in ===> %r" % (query, resultSet))
        for x  in resultSet:
            if i < 1:    
                tempAr.append(x)
            else:
                tempAr1.append(x)
        i = i + 1
    #AND    OPERATION WORKING   USING SET   PROPERTY
    aset = set(tempAr)
    bset = set(tempAr1)
    #tSets = [set() for _ in range(noTerms)]
    if (aset & bset):
        andResult = (aset & bset)
        return andResult
    else:
        return "notfound"



def andOp2(queryTerms):
    i = 0
    #noTerms = len(queryTerms)
    #tAr = [[] for _ in range(noTerms)]
    tempAr = []
    tempAr2 = []
    tempAr1 = []
    tempAr3 = []
    xtemp = []
    utemp = []
    y = []
    p = []

    na = []
    #queryTerms = [x for x in queryTerms if x!= 'and']
    queryTerms = queryTerms.split(' and ')
    #queryTerms = [x for x in queryTerms if x!= '']
    #print("QueryTerms:" ,queryTerms)
    
    
    
    
   
    
    
    
    
    for k in queryTerms:
        tempAr1.append(k.replace(" ",""))
    print(tempAr1)
    for qu in tempAr1:
        resultSet = fetchDoc(inv_Index,qu)

        #print ("'%s' Appears in ===> %r" % (query, resultSet))
        for x  in resultSet:
            
            if i == 0 :
                
                tempAr.append(x)
                #print(tempAr)
            else:
                xtemp.insert(0,x)
                #print(xtemp)
                #print(tempAr)
                tempAr2 = list((set(tempAr) & set(xtemp)))
                
# =============================================================================
#             else:
#                 utemp.append(x)
#                 na = tempAr2.copy()
#                 tempAr3 = list((set(tempAr2) & set(utemp)))
# =============================================================================

            #print(tempAr)
                
                #if (set(tempAr) & set(xtemp)):
                 #   tempAr = set(tempAr) & set(xtemp)
                #else:
                 #   tem = "Nahi hai"
                    #print(x)
        i = i + 1
    #AND    OPERATION WORKING   USING SET   PROPERTY
# =============================================================================
#     aset = set(tempAr)
#     bset = set(tempAr1)
#     #tSets = [set() for _ in range(noTerms)]
#     if (aset & bset):
#         andResult = (aset & bset)
#         return andResult
#     else:
#         return "notfound"
# =============================================================================
   
    if i ==1:
        return tempAr
    else:
        return tempAr2




def notTermDL(nqTerm):
    #print(nqTerm)
    
    allDocID = []
    for x in range(0,50):                   #DOCUMENT'S   ID      LIST
        allDocID.append("doc"+str(x+1))
    resultSet = fetchDoc(inv_Index,nqTerm)          #TypeList    
    
    return list(set(allDocID) - resultSet)
    

def queryProcessing(queryString):
    k = 0
    t = []
    t1 = []
    sInString = []
    queryS = []
    resultList = []
    result = []
    andCount = 0
    orCount = 0
    ts = 'and'
    tO = 'or'
    y = []
    
# =============================================================================
#     for orc in queryString:
#         if orc == tO:
#             orCount = orCount +1
#     if orCount >= 1:
# =============================================================================
    queryS = queryString.split(" or ")
    for i in queryS:
        result = andOp2(i)
        #sInString = re.split('\W+',queryS[k])
# =============================================================================
#         for an in sInString:
#             if an == ts:    
#                 andCount = andCount +1 
#         if andCount >= 1:
#             result= andOp2(sInString)
#         
#         else:
#             result = orOp(sInString)
# =============================================================================
        resultList.append(result)
        del result
        #del sInString
        k = k +1 
    for p in resultList:
        for t in p:
            y.append(t)
    y = list(dict.fromkeys(y))  
    return y



def queryProc(query):
    operations = ['and','or','not']
    s = []
    query = []
    notWord = []
    tAnd = []
    tOr = []
    andResult = []
    orResult = []
    notCount = 0
    andCount = 0
    k = 0
    c = 0
    
    
    for word in query:
       if word !=  operations[2]:
           #print("Khair hai bas!")
           
           if notCount >=1:
               notWord.append(word)
               notCount = notCount - 1
               k = k + 1
           else:    
               s.append(word)
               k = k +1
           
       else:
           #print("Idhar khair nahi")
           wonL.append(notTermDL(inputString[k+1]))
           notCount = notCount + 1
           k = k + 1
           
    
    
    
    
    if len(notWord) == 0:
        for word in query:
            if word == operations[0] and query[c-1] != operations[1] and query[c+1] != operations[1]:           #Simple AND Query
                  tAnd.append(query[c-1])
                  tAnd.append(query[c+1])
                  andCount = andCount + 1
                  #print(word)
                  if len(andResult) == 0:
                      andResult.append(list(andOp(tAnd)))
                      #del temp
                  else:
                      andResult.append(list(set(andResult[0]) & set(fetchDoc(inv_Index,tAnd[3]))))
            elif word == operations[1] and query[c-1] != operations[0] and query[c+1] != operations[0]:
                    tOr.append(query[c-1])
                    tOr.append(query[c+1])
                    orResult.append(orOp(tOr))
                
            c = c + 1
    if len(andResult)>1:
       # print(andResult)
        aset = set(andResult[0])
        bset = set(andResult[1])
    #tSets = [set() for _ in range(noTerms)]
        if (aset & bset):
            at = (aset & bset)
            return at
        else:
            return "notfound"
    
# =============================================================================
#         for subList in andResult:
#               for fList in subList:
#                   kl.append(fList)
# =============================================================================
# =============================================================================
#     else:
#         print(andResult)
#         #te = list(dict.fromkeys(orResult[0]))
#         #print(te)
# =============================================================================




    
def orOp(queryTerms):
    tempAr = []
    queryTerms = [x for x in queryTerms if x!= '']
    for query in queryTerms:
        resultSet = fetchDoc(inv_Index,query)
            
        #print ("'%s' Appears in ===> %r" % (query, resultSet))
        #OR operation Working
        for x  in resultSet:
            tempAr.append(x)
            
    #RemoveDuplicates       
    tempAr = list(dict.fromkeys(tempAr))
    return tempAr
    

def printInvIndFile(inv_Index):
    fop = open("Dictionary.txt","w")
    #fop.write(json.dumps(iv))
    for tokens, wpos in inv_Index.items():
        fop.write(tokens)
        fop.write("  ===>  ")
        fop.write(json.dumps(wpos))
        fop.write("\n")
        fop.write("\n")
        
    fop.close()
    
    
def proxfetchDoc(invInd, query):
    wordList = [tok for _, tok in menuEmulat(query) if tok in invInd]
    fetchedResults = [set(invInd[tok].keys()) for tok in wordList]
    fdDocs = reduce(lambda tok,key : tok & key,fetchedResults) if fetchedResults else[]
    return fdDocs



fio = readFromFile()

def posIn(fio):
    ind = {}
    for i in range(50):
        with open(fio[i+1])as f:
            dc = menuEmulat(fio[i+1])
        for ix, wd in enumerate(doc):
            ind[wd] = [(i,ix)]
        else:
            ind[wd].append((i,idx))
    return id

def proximitySearch(queryTm,c):
    a = []
    i =  0
    for q in iv:
        if queryTm == q:
            print(q)
            print(wpos)
    
    
    


if __name__ == '__main__':
    inv_Index = {}
    corpus = {}
    documentID = []
    inputString = []
    wonL = []
    flatResult = []
    hav = []
    z = []
    fin = 0
    ac = 0
    av = 0
    operations = ['and','or','not']
    stories = readFromFile()


    
    for x in range(0,50):                   #DOCUMENT'S   ID      LIST
        documentID.append("doc"+str(x+1))
        #print("****")    
    for y in range(0,50):
       corpus.update({documentID[y] : stories[y]})
       #print("****")    
    for ID, story in corpus.items():        #INVERTED   INDEX   CREATION
        docInCorp = trialInvInd(story)
        iv = invertedIndex(inv_Index,ID,docInCorp)
        #print("****")
    printInvIndFile(iv)              #INVERTED       INDEX       PRINTING IN     FOLDER
    
    qt = input("Enter Query Type:proximity/inverted ")
    x = input("Enter Query: ")
    if qt == 'inverted':
        z= re.split('\W+',x)
        jut = 0
        for e in z:
           if e == 'not':
               da = notTermDL(z[jut+1])
               ac = ac +1
           jut = jut +1
    
         
            
           
           
           
           if ac == 0:
               
               finalResult = queryProcessing(x)
# =============================================================================
#         for an in x:
#             if an == 'or':
#                 ac = ac +1   
#         for an in x:
#             if an == 'and':
#                 av = av +1          
#                 
#         if ac >= 1:        
#             finalResult = queryProcessing(x)
#         
#         elif  av > 1:
#             hav = re.split('\W+',x)
#             finalResult = queryProc(hav)
#         else:
#             finalResult = queryProcessing(x)
#     
# =============================================================================
     
        

    
    elif  qt == 'proximity':
        proximitySearch(x,inv_Index)
    if ac > 0:
        print(da)
    elif ac == 0 :
        print(finalResult)
    #print(wonL)
    #print(s)
    #print(notWord)
    #print(orOp(inputString))
    
    
    
    
