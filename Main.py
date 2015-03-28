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
#print "escaped query: " , query

fbUrl = 'https://www.googleapis.com/freebase/v1/search?query=' + query + '&key=AIzaSyBW2UrVGC4_05gNjzEojWziXZivR1NFF6Y'
print "the fburl: " , fbUrl
#Provide your account key here
accountKey = 'AIzaSyBW2UrVGC4_05gNjzEojWziXZivR1NFF6Y'

accountKeyEnc = base64.b64encode(accountKey + ':' + accountKey)
headers = {'Authorization': 'Basic ' + accountKeyEnc}
req = urllib2.Request(fbUrl, headers = headers)
response = urllib2.urlopen(req)
# content = response.read()
# #content contains the xml/json response from Bing.
# print content
# print type(content)

json_obj = json.load(response)
#print type (json_obj)
l=  len(json_obj['result'])
#print l , ":this is d length"
#print json_obj

#print json_obj['result']

# for x in range(0,l):
#     print "The entry number", x+1, "is :"
#     print "The mid is", json_obj['result'][x]['mid']
#     print

#print "=============================="

#query the Topic API for this mid using the URL https://www.googleapis.com/freebase/v1/topic/m/017nt?key=API_KEY

topicUrl = 'https://www.googleapis.com/freebase/v1/topic' + json_obj['result'][0]['mid'] + '?key=AIzaSyBW2UrVGC4_05gNjzEojWziXZivR1NFF6Y'

print topicUrl , ": topic url"

req1 = urllib2.Request(topicUrl, headers = headers)
response1 = urllib2.urlopen(req1)
json_obj1 = json.load(response1)
# print type (json_obj1)
# print json_obj1
# l1=  len(json_obj1['result'])
# print l1 , ":this is d length"
# #print json_obj
#
# print json_obj1['result']
# print "========================================================="
# print
a = {} #empty dictionaries
b = {}
for k in json_obj1['property']:
    b[k] = 'true' #add to dictionary k:true
    if('/people/person' in k):
        a['Person'] = 'true'
    if('/book/author' in k):
        a['Author'] = 'true'
    if('/film/actor' in k or '/tv/tv_actor' in k):
        a['Actor'] = 'true'
    if('/organization/organization_founder' in k or '/business/board_member' in k):
        a['BusinessPerson'] = 'true'
    if('/sports/sports_league' in k):
        a['League'] = 'true'
    if('/sports/sports_team' in k or '/sports/professional_sports_team' in k):
        a['SportsTeam'] = 'true'


def person(p):

    if ('/type/object/name' in b):
        print
        print "Name: " , p['/type/object/name']['values'][0]['text']

    if ('/people/person/date_of_birth' in b):
        print
        print "Birthday: " , p['/people/person/date_of_birth']['values'][0]['text']

    if ('/people/person/place_of_birth' in b):
        print
        print "Place of Birth: " , p['/people/person/place_of_birth']['values'][0]['text']

    if ('/people/deceased_person/place_of_death' in b):
        print
        print "Death: (Place, Date, Cause ) "
        print "   " , p['/people/deceased_person/place_of_death']['values'][0]['text']
    if ('/people/deceased_person/date_of_death' in b):
        print "   " , p['/people/deceased_person/date_of_death']['values'][0]['text']
    if ('/people/deceased_person/cause_of_death' in b):
        if p['/people/deceased_person/cause_of_death']['count']>0:
            l = len(p['/people/deceased_person/cause_of_death']['values'])

            for i in range(0,l):
                print p['/people/deceased_person/cause_of_death']['values'][i]['text'] , ","

    if ('/people/person/sibling_s' in b):
        if p['/people/person/sibling_s']['count']>0:
            l = len(p['/people/person/sibling_s']['values'])
            print
            print "Siblings: "
            for i in range(0,l):
                print p['/people/person/sibling_s']['values'][i]['property']['/people/sibling_relationship/sibling']['values'][0]['text'] , ","

    # if ('/people/person/spouse_s' in b):
    #     if p['/people/person/spouse_s']['count']>0:
    #         l = len(p['/people/person/spouse_s']['values'])
    #         print
    #         print "Spouses: "
    #         for i in range(0,l):
    #             print p['/people/person/spouse_s']['values'][i]['property']['/people/marriage/spouse']['values'][0]['text'] , ","

    if ('/people/person/spouse_s' in b):
        if p['/people/person/spouse_s']['count']>0:
            l = len(p['/people/person/spouse_s']['values'])
            print
            print "Spouses: "
            for i in range(0,l):
                duration = ""
                place = ""
                name = p['/people/person/spouse_s']['values'][i]['property']['/people/marriage/spouse']['values'][0]['text']
                if '/people/marriage/from' in p['/people/person/spouse_s']['values'][i]['property']:
                    duration = duration + p['/people/person/spouse_s']['values'][i]['property']['/people/marriage/from']['values'][0]['text']
                if p['/people/person/spouse_s']['values'][i]['property']['/people/marriage/to']['count']>0:
                    duration = duration + " - " + p['/people/person/spouse_s']['values'][i]['property']['/people/marriage/to']['values'][0]['text']
                else:
                    duration = duration + " - now"

                if '/people/marriage/location_of_ceremony' in p['/people/person/spouse_s']['values'][i]['property']:
                    if p['/people/person/spouse_s']['values'][i]['property']['/people/marriage/location_of_ceremony']['count']>0:
                        place = " @ " + p['/people/person/spouse_s']['values'][i]['property']['/people/marriage/location_of_ceremony']['values'][0]['text']

                print name , "(" , duration , ")" + place



    if ('/common/topic/description' in b):
        print
        print "Description: " , p['/common/topic/description']['values'][0]['value']

    return

def author(p):

    if ('/book/author/works_written' in b):
        if p['/book/author/works_written']['count']>0:
            l = len(p['/book/author/works_written']['values'])
            print
            print "Books: "
            for i in range(0,l):
                print p['/book/author/works_written']['values'][i]['text'] , ","

    if ('/book/book_subject/works' in b):
        if p['/book/book_subject/works']['count']>0:
            l = len(p['/book/book_subject/works']['values'])
            print
            print "Books about: "
            for i in range(0,l):
                print p['/book/book_subject/works']['values'][i]['text'] , ","


    if ('/influence/influence_node/influenced' in b):
        if p['/influence/influence_node/influenced']['count']>0:
            l = len(p['/influence/influence_node/influenced']['values'])
            print
            print "Influenced: "
            for i in range(0,l):
                print p['/influence/influence_node/influenced']['values'][i]['text'] , ","

    if ('/influence/influence_node/influenced_by' in b):
        if p['/influence/influence_node/influenced_by']['count']>0:
            l = len(p['/influence/influence_node/influenced_by']['values'])
            print
            print "Influenced by: "
            for i in range(0,l):
                print p['/influence/influence_node/influenced_by']['values'][i]['text'] , ","

    return


def actor(p):
    if ('/film/actor/film' in b):
        if p['/film/actor/film']['count']>0:
            l = len(p['/film/actor/film']['values'])
            print
            print "Films :           Character                   Film Name"
            for i in range(0,l):

                if '/film/performance/character' in p['/film/actor/film']['values'][i]['property']:
                    character = p['/film/actor/film']['values'][i]['property']['/film/performance/character']['values'][0]['text']
                else:
                    character = "           "

                if '/film/performance/film' in p['/film/actor/film']['values'][i]['property']:
                    film = p['/film/actor/film']['values'][i]['property']['/film/performance/film']['values'][0]['text']
                else:
                    film = "            "

                print "                 ", character , "                   ", film


    # if ('/film/actor/film' in b):
    #     if p['/film/actor/film']['count']>0:
    #         l = len(p['/film/actor/film']['values'])
    #         print "Films : "
    #         for i in range(0,l):
    #             print p['/film/actor/film']['values'][i]['text'] , ","

    return

def businessPerson(p):

    if('/business/board_member/leader_of' in b):
        print
        print "LEADERSHIP:"
        if p['/business/board_member/leader_of']['count']>0:
            l = len(p['/business/board_member/leader_of']['values'])
            print "Organization                   Role                        Title                           From-To"
            for i in range(0,l):
                print p['/business/board_member/leader_of']['values'][i]['property']['/organization/leadership/organization']['values'][0]['text'] , "      " ,p['/business/board_member/leader_of']['values'][i]['property']['/organization/leadership/role']['values'][0]['text'] , "      " ,p['/business/board_member/leader_of']['values'][i]['property']['/organization/leadership/title']['values'][0]['text'], "      " ,p['/business/board_member/leader_of']['values'][i]['property']['/organization/leadership/from']['values'][0]['text'], "-" ,p['/business/board_member/leader_of']['values'][i]['property']['/organization/leadership/to']['values'][0]['text']


    if('/business/board_member/organization_board_memberships' in b):
        if p['/business/board_member/organization_board_memberships']['count']>0:
            print
            print "Board Member:"
            l = len(p['/business/board_member/organization_board_memberships']['values'])
            print "Organization                   Role                        Title                           From / To"
            for i in range(0,l):
                #print p['/business/board_member/leader_of']['values'][i]['property']['/organization/leadership/organization']['values'][0]['text'] , "      " ,p['/business/board_member/leader_of']['values'][i]['property']['/organization/leadership/role']['values'][0]['text'] , "      " ,p['/business/board_member/leader_of']['values'][i]['property']['/organization/leadership/title']['values'][0]['text'], "      " ,p['/business/board_member/leader_of']['values'][i]['property']['/organization/leadership/from']['values'][0]['text'], "-" ,p['/business/board_member/leader_of']['values'][i]['property']['/organization/leadership/to']['values'][0]['text']

                role = ""
                organization = ""
                title = ""
                duration = ""

                organization += p['/business/board_member/organization_board_memberships']['values'][i]['property']['/organization/organization_board_membership/organization']['values'][0]['text']

                if '/organization/organization_board_membership/role' in p['/business/board_member/organization_board_memberships']['values'][i]['property']:
                    if p['/business/board_member/organization_board_memberships']['values'][i]['property']['/organization/organization_board_membership/role']['count']>0:
                        l2= len(p['/business/board_member/organization_board_memberships']['values'][i]['property']['/organization/organization_board_membership/role']['values'])
                        for j in range(0,l2):
                            role = role + p['/business/board_member/organization_board_memberships']['values'][i]['property']['/organization/organization_board_membership/role']['values'][j]['text'] + ", "

                if '/organization/organization_board_membership/title' in p['/business/board_member/organization_board_memberships']['values'][i]['property']:
                    if p['/business/board_member/organization_board_memberships']['values'][i]['property']['/organization/organization_board_membership/title']['count']>0:
                        l3= len(p['/business/board_member/organization_board_memberships']['values'][i]['property']['/organization/organization_board_membership/title']['values'])
                        for k in range(0,l3):
                            title = title + p['/business/board_member/organization_board_memberships']['values'][i]['property']['/organization/organization_board_membership/title']['values'][k]['text'] + ", "


                if '/organization/organization_board_membership/from' in p['/business/board_member/organization_board_memberships']['values'][i]['property']:
                    duration = p['/business/board_member/organization_board_memberships']['values'][i]['property']['/organization/organization_board_membership/from']['values'][0]['text']
                if '/organization/organization_board_membership/to' in p['/business/board_member/organization_board_memberships']['values'][i]['property'] and p['/business/board_member/organization_board_memberships']['values'][i]['property']['/organization/organization_board_membership/to']['count']>0:
                    duration = duration + " / " + p['/business/board_member/organization_board_memberships']['values'][i]['property']['/organization/organization_board_membership/to']['values'][0]['text']
                else:
                    duration = duration + " / now"

                print organization , "              " , role , "                " , title , "               " , "( " + duration + " )"


    if '/organization/organization_founder/organizations_founded' in b:
        if p['/organization/organization_founder/organizations_founded']['count']>0:
            l = len(p['/organization/organization_founder/organizations_founded']['values'])
            print
            print "Founded: "
            for i in range (0,l):
                print p['/organization/organization_founder/organizations_founded']['values'][i]['text']




    return

def league(p):
    if('/type/object/name' in b):
        # if ['/type/object/name']['count']>0:
        #     l= len (p['/type/object/name']['values'])
        print
        print "Name:    " , p['/type/object/name']['values'][0]['text']
    if('/sports/sports_league/sport' in b):
        print
        print "Sport:   " , p['/sports/sports_league/sport']['values'][0]['text']
    if('/organization/organization/slogan' in b):
        print
        print "Slogan:   " , p['/organization/organization/slogan']['values'][0]['text']
    if('/common/topic/official_website' in b):
        print
        print "Official Website:   " , p['/common/topic/official_website']['values'][0]['text']
    if('/sports/sports_league/championship' in b):
        print
        print "Championship:   " , p['/sports/sports_league/championship']['values'][0]['text']

    if('/sports/sports_league/teams' in b):
        if p['/sports/sports_league/teams']['count']>0:
            l = len(p['/sports/sports_league/teams']['values'])
            print
            print "Teams: "
            for i in range(0,l):
                print p['/sports/sports_league/teams']['values'][i]['property']['/sports/sports_league_participation/team']['values'][0]['text']

    if '/common/topic/description' in b:
        print
        print "Description:"
        print p['/common/topic/description']['values'][0]['value']
    return

def sportsTeam(p):
    if '/type/object/name' in b:
        print
        print "Name:    " , p['/type/object/name']['values'][0]['text']

    if '/sports/sports_team/sport' in b:
        print
        print "Sport:    " , p['/sports/sports_team/sport']['values'][0]['text']


    if '/sports/sports_team/arena_stadium' in b:
        print
        print "Arena:    " , p['/sports/sports_team/arena_stadium']['values'][0]['text']

    if '/sports/sports_team/championships' in b:
        if p['/sports/sports_team/championships']['count']>0:
            l=len(p['/sports/sports_team/championships']['values'])
            print
            print "Championships:"
            for i in range(0,l):
                print p['/sports/sports_team/championships']['values'][i]['text']

    if '/sports/sports_team/founded' in b:
        print
        print "Founded:    " , p['/sports/sports_team/founded']['values'][0]['text']

    if '/sports/sports_team/league' in b:
        if p['/sports/sports_team/league']['count']>0:
            l=len(p['/sports/sports_team/league']['values'])
            print
            print "Leagues:"
            for i in range(0,l):
                print p['/sports/sports_team/league']['values'][i]['property']['/sports/sports_league_participation/league']['values'][0]['text']

    if '/sports/sports_team/location' in b:
        print
        print "Locations:    " , p['/sports/sports_team/location']['values'][0]['text']

    if('/sports/sports_team/coaches' in b):
        print
        print "Coaches:"
        if p['/sports/sports_team/coaches']['count']>0:
            l = len(p['/sports/sports_team/coaches']['values'])
            print "Name                   Position            From / To"
            for i in range(0,l):
                if(p['/sports/sports_team/coaches']['values'][i]['property']['/sports/sports_team_coach_tenure/to']['count'] > 0):
                    print p['/sports/sports_team/coaches']['values'][i]['property']['/sports/sports_team_coach_tenure/coach']['values'][0]['text'] , "      " ,p['/sports/sports_team/coaches']['values'][i]['property']['/sports/sports_team_coach_tenure/position']['values'][0]['text'] ,  "      " ,p['/sports/sports_team/coaches']['values'][i]['property']['/sports/sports_team_coach_tenure/from']['values'][0]['text'], " / " ,p['/sports/sports_team/coaches']['values'][i]['property']['/sports/sports_team_coach_tenure/to']['values'][0]['text']
                else:
                    print p['/sports/sports_team/coaches']['values'][i]['property']['/sports/sports_team_coach_tenure/coach']['values'][0]['text'] , "      " ,p['/sports/sports_team/coaches']['values'][i]['property']['/sports/sports_team_coach_tenure/position']['values'][0]['text'] ,  "      " ,p['/sports/sports_team/coaches']['values'][i]['property']['/sports/sports_team_coach_tenure/from']['values'][0]['text'], " /  now"

    if '/sports/sports_team/roster' in b:
        l = len(p['/sports/sports_team/roster']['values'])
        print
        print "PlayersRoster:"
        print "Name                   Position            Number        From / To"
        for i in range(0,l):
            positions = ""
            number = ""
            if '/sports/sports_team_roster/position' in p['/sports/sports_team/roster']['values'][i]['property']:
                l2 = len(p['/sports/sports_team/roster']['values'][i]['property']['/sports/sports_team_roster/position']['values'])
                for j in range(0,l2):
                    positions = positions + p['/sports/sports_team/roster']['values'][i]['property']['/sports/sports_team_roster/position']['values'][j]['text'] + ", "
            if '/sports/sports_team_roster/number' in p['/sports/sports_team/roster']['values'][i]['property']:
                number = p['/sports/sports_team/roster']['values'][i]['property']['/sports/sports_team_roster/number']['values'][0]['text']
            #if(p['/sports/sports_team/roster']['values'][i]['property']['/sports/sports_team_coach_tenure/to']['count'] > 0):
            print p['/sports/sports_team/roster']['values'][i]['property']['/sports/sports_team_roster/player']['values'][0]['text'] , "      " , positions ,  "      " , number , "      " , p['/sports/sports_team/roster']['values'][i]['property']['/sports/sports_team_roster/from']['values'][0]['text'] , " / " ,p['/sports/sports_team/roster']['values'][i]['property']['/sports/sports_team_roster/to']['values'][0]['text']
            #else:
                #print p['/sports/sports_team/coaches']['values'][i]['property']['/sports/sports_team_coach_tenure/coach']['values'][0]['text'] , "      " ,p['/sports/sports_team/coaches']['values'][i]['property']['/sports/sports_team_coach_tenure/position']['values'][0]['text'] ,  "      " ,p['/sports/sports_team/coaches']['values'][i]['property']['/sports/sports_team_coach_tenure/from']['values'][0]['text'], " /  now"

    if '/common/topic/description' in b:
        print
        print "Description:"
        print p['/common/topic/description']['values'][0]['value']

    return

for i in a:
    if(i=='Person'):
        person(json_obj1['property'])
        if(i=='Author'):
            author(json_obj1['property'])
        if(i=='Actor'):
            actor(json_obj1['property'])
        if(i=='BusinessPerson'):
            businessPerson(json_obj1['property'])
    if(i=='League'):
        league(json_obj1['property'])
    if(i=='SportsTeam'):
        sportsTeam(json_obj1['property'])