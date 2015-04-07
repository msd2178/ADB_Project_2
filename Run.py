import os
import sys
from ADBProjectPart1 import Infobox
from ADBProjectPart2 import QuestionAnswering

#python Run.py -key XXXXXX -q Who created Microsoft? -t question

key = ''
filePath = ''
query = ''
type = ''

#print(len(sys.argv))

if len(sys.argv) > 0:
    query = ""
    j=0
    for i in xrange(1,len(sys.argv)):
        if sys.argv[i] == "-key":
            key = sys.argv[i+1]
        elif sys.argv[i] == "-t":
            type = sys.argv[i+1]
        elif sys.argv[i] == "-f":
            filePath = sys.argv[i+1]
        elif sys.argv[i] == "-q":
            j=i
            next = sys.argv[j+1]
            while '-' not in next:
                query = query + next + " "
                if j < len(sys.argv):
                    j = j + 1
                    next = sys.argv[j+1]
                else:
                    continue
if  len(sys.argv) > 3:
    if filePath!="" and query =="":
        with open(filePath) as queryFile:
            for q in queryFile:
                if type.lower()=="question":
                    QuestionAnswering(key,q)
                else:
                    Infobox(key, q)
    elif filePath=="" and query !="":
        if type.lower()=="question":
            QuestionAnswering(key,query)
        else:
            Infobox(key, query)
else:
    query = raw_input("Please enter the query:")
    while True:
        q = query.strip().split(' ')
        if len(q)>2 and q[0].lower() == 'who' and q[1].lower() == 'created':
            QuestionAnswering(key,query)
        else:
            Infobox(key, query)
        query = raw_input("Please enter the query:")





