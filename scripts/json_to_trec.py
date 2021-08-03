import sys
import json 
import urllib

k=1
fp = open("test_queries.txt",encoding="utf-8")
corename= ['BM25_Model','Language_Model','DFR_Model']
fields= ['text_en','text_ru','text_de']
for i in fp: 
    text= i.partition(' ')[2]
    qid= i.partition(' ')[0]
    text=text.replace(":","\:")
    text=urllib.parse.quote(text)
    for j in corename:
        for lang in fields:
            inurl = 'http://ec2-18-220-165-111.us-east-2.compute.amazonaws.com:8984/solr/'+j+'/select?q='+lang+':'+text+'&fl=id%2Cscore&wt=json&indent=true&rows=20'
            print(inurl)
            outfn = './'+j+'/'+str(k)+'.txt'
            outf = open(outfn, 'a+')
            data = urllib.request.urlopen(inurl)
        # if you're using python 3, you should use
        # data = urllib.request.urlopen(inurl)

            temp_docs = json.load(data)['response']['docs']
            if(len(temp_docs)>len(docs)):
                docs=temp_docs
        # the ranking should start from 1 and increase
        rank = 1
        for doc in docs:
                outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + j + '\n')
                rank += 1
        outf.close()
        temp_docs=[]
        docs=[]
    k+=1
    
    