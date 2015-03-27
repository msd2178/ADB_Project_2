__author__ = 'meril'

import urllib2
import base64
import json
import urllib

#add the k's into a dictionary
#store the url thingy in strings for beautification
#check the count

query = raw_input("Enter the list of query words :")
query = urllib.quote(query)
print "escaped query: " , query

fbUrl = 'https://www.googleapis.com/freebase/v1/search?query=' + query + '&key='
print "the fburl: " , fbUrl
#Provide your account key here
accountKey = ''

accountKeyEnc = base64.b64encode(accountKey + ':' + accountKey)
headers = {'Authorization': 'Basic ' + accountKeyEnc}
req = urllib2.Request(fbUrl, headers = headers)
response = urllib2.urlopen(req)
# content = response.read()
# #content contains the xml/json response from Bing.
# print content
# print type(content)

json_obj = json.load(response)
print type (json_obj)
l=  len(json_obj['result'])
print l , ":this is d length"
#print json_obj

print json_obj['result']

for x in range(0,l):
    print "The entry number", x+1, "is :"
    print "The mid is", json_obj['result'][x]['mid']
    print

print "=============================="

#query the Topic API for this mid using the URL https://www.googleapis.com/freebase/v1/topic/m/017nt?key=API_KEY

topicUrl = 'https://www.googleapis.com/freebase/v1/topic' + json_obj['result'][0]['mid'] + '?key='

print topicUrl , ": topic url"

req1 = urllib2.Request(topicUrl, headers = headers)
response1 = urllib2.urlopen(req1)
json_obj1 = json.load(response1)
print type (json_obj1)
print json_obj1
# l1=  len(json_obj1['result'])
# print l1 , ":this is d length"
# #print json_obj
#
# print json_obj1['result']
print "========================================================="
print
a = {}
b = {}
for k in json_obj1['property']:
    b[k] = 'true'
#print type(k)

    if('/people/person' in k):
        #person(json_obj1['property'])
        #a.update('person': 'true')
        a['person'] = 'true'
    if('/book/author' in k):
        a['business_person'] = 'true'


def person(p):
    if ('/type/object/name' in b):
        print "Name: " , p['/type/object/name']['values'][0]['text']
    if ('/people/person/date_of_birth' in b):
        print "Birthday: " , p['/people/person/date_of_birth']['values'][0]['text']
    if ('/people/person/place_of_birth' in b):
        print "Place of Birth: " , p['/people/person/place_of_birth']['values'][0]['text']
    # if ('/people/person/place_of_birth' in b):
    #     print "Death(Place, Date, Cause): " , p['/people/person/date_of_birth']['values'][0]['text']
    if ('/people/person/sibling_s' in b):
        if p['/people/person/sibling_s']['count']>0:
            l = len(p['/people/person/sibling_s']['values'])
            print "Siblings: "
            for i in range(0,l):
                print p['/people/person/sibling_s']['values'][i]['property']['/people/sibling_relationship/sibling']['values'][0]['text'] , ","

    if ('/people/person/spouse_s' in b):
        if p['/people/person/spouse_s']['count']>0:
            l = len(p['/people/person/spouse_s']['values'])
            print "Spouses: "
            for i in range(0,l):
                print p['/people/person/spouse_s']['values'][i]['property']['/people/marriage/spouse']['values'][0]['text'] , ","

    print "Description: " , p['/common/topic/description']['values'][0]['value']
    return

def business_person(b):

    return

for i in a:
    if(i=='person'):
        person(json_obj1['property'])
    if(i=='business_person'):
        business_person(json_obj1['property'])







