# ADB_Project_2

README
(a) Team Members:
Utkarsha Prakash (up2127)
Meril Dsouza (msd2178)

(b) Python files included:
Run.py
ADBProjectPart1.py
ADBProjectPart2.py

Transcripts for Part 1:
BillGates.txt
RobertDowneyJr.txt
Jackson.txt
NFL.txt
NBA.txt
NYKnicks.txt
MiamiHeat.txt

Transcripts for Part 2:
Google.txt
LOTR.txt
RomeoAndJuliet.txt
Microsoft.txt


(c) Run Program:

You will need to run the python file Run.py with the following parameters:
-key: Freebase API key
-q: Query
-f: File name
-t: Infobox/Question

Sample commands:
1.	python Run.py -key AIzaSyDYqLECS8jeMv18aAWdFgUQeA-AxD94jp8 -q Who created Microsoft? -t question

2.	python Run.py -key AIzaSyDYqLECS8jeMv18aAWdFgUQeA-AxD94jp8 -f Queries.txt -t infobox

3. 	python Run.py -key AIzaSyDYqLECS8jeMv18aAWdFgUQeA-AxD94jp8
   	(for interactive mode)

4.	python Run.py -key AIzaSyDYqLECS8jeMv18aAWdFgUQeA-AxD94jp8 -f C:\Users\Utkarsha\Desktop\IB.txt -t infobox

5. python Run.py -key AIzaSyDYqLECS8jeMv18aAWdFgUQeA-AxD94jp8 -f      C:\Users\Utkarsha\Desktop\QNA.txt -t question


(d) Internal Design:

Important Functions:

1. Run.py (key, filePath, query, type): 
This function is the starting point of the code. It reads in the command line arguments key, filePath, query and type and appropriately calls the corresponding functions.
If type is “infobox” the function called is Infobox(key,query)
If type is “question” the function called is QuestionAnswering(key, query). Also in case a file is passed to this function it reads and parses the file and appropriately calls the Infobox or QuestionAnswering function for each query in the file. In the interactive mode it takes the user query and on the basis of which kind of query has been entered it calls Infobox or QuestionAnswering function.

2. QuestionAnswering(key, fullQuery)
This function takes in a query, processes it and if the query is in the appropriate format it passes it to the Freebase API. If the Freebase API gives the correct results it displays the output in the console.

3. Infobox(key,query)
This function takes a query from the user and queries the Freebase Search API. The API returns the entities in order of relevance. The entities are then taken in order and the Freebase Topic API is queried by using the mid values returned from the search API. If a Freebase entity contains one or more of the entities desired for the project then we proceed to create the infobox. If not we move on to the next entity. If none of the entities from freebase contain the desired entities, then we inform the user than no relevant results are present.

In the case in which the desired entities are present, we then have to retrieve the properties of interest for each of the desired entities. We do this by checking if each of the properties of interest are present in the entity. If present then we include the information in our infobox, else we ignore it. 
There are cases in which some entries returned from Freebase contain empty fields. Thus, we check if the values exist or not and populate our infobox accordingly.

We create a dictionary that contains all the desired entities that are present in the entity from Freebase. In case Person is present then we modify the dictionary to exclude League and SportsTeam. Similarly if League or SportsTeam is present then we exclude Person, Actor, Author and Businessman from the dictionary. These conditions are all accounted for in our code. Thus only the entities that remain in our dictionary after modification will be displayed in our infobox by calling the relevant functions.

Mappings from Freebase properties to entity properties for infobox:

Person:
/type/object/name	Name
/people/person/date_of_birth	Birthday
/people/person/place_of_birth	Place of birth
/people/deceased_person/place_of_death	Death – Place
/people/deceased_person/date_of_death	Death – Date
/people/deceased_person/cause_of_death	Death – Cause
/people/person/sibling_s	Siblings
/people/person/spouse_s	Spouse
/common/topic/description	Description

Author:
/book/author/works_written	Books
/book/book_subject/works
	Book About the Author
/influence/influence_node/influenced	Influenced
/influence/influence_node/influenced_by	Influenced by


Actor:
/film/actor/film	Film Name
/film/performance/character	Character

BusinessPerson:
/organization/leadership/from	Leadership - from
/organization/leadership/to	Leadership - to
/organization/leadership/organization	Leadership - organization
/organization/leadership/role	Leadership - role
/organization/leadership/title	Leadership - title
/organization/organization_board_membership/from	BoardMember - from
/organization/organization_board_membership/to	BoardMember - to
/organization/organization_board_membership/organization	BoardMember - organization
/organization/organization_board_membership/role	BoardMember - role
/organization/organization_board_membership/title	BoardMember - title
/organization/organization_founder/organizations_founded	Founded – organization name

League:
/type/object/name	Name
/sports/sports_league/championship	Championship
/sports/sports_league/sport	Sport
/organization/organization/slogan	Slogan
/common/topic/official_website	Official Website
/common/topic/description	Description
/sports/sports_league/teams	Teams






SportsTeam:
/type/object/name	Name
/common/topic/description	Description
/sports/sports_team/sport	Sport
/sports/sports_team/arena_stadium	Arena
/sports/sports_team/championships	Championships
/sports/sports_team/coaches	Coaches
/sports/sports_team/founded	Founded
/sports/sports_team/league	Leagues
/sports/sports_team/location	Locations
/sports/sports_team/roster	PlayersRoster


Mappings from Freebase properties to entity properties for question answering:

"type":"/organization/organization_founder"	founders['name']]["organizations"]
"name"	founders['name']]
"organizations_founded”	organizations
“organizations_founded" - "a:name"	organization['a:name']
“organizations_founded" - " name~"	organization['name']

"type":"/book/author"	authors['name']]["books"]
"name"	authors['name']]
"works_written”	books
“works_written" - "a:name"	books['a:name']
“works_written" - " name~"	books['name']

(e) Freebase API key: XXXXXX, 
Requests per second per user: 10
