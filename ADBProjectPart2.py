import json
import re
import urllib

# This code is used for removing the cleaning up the user query before searching the FreeBaseAPI.
def removePunctuation(str):
    return re.sub(ur"[\,\|\-\?\[\]\{\}\(\)\"\:\;\!\@\#\$\ %\^\&\*\>\<]|(\.$)|(\.\.\.)", ' ', str)

def QuestionAnswering(key, fullQuery):
    # Process results only if the query matches the result Who created [xxx]?
    q = fullQuery.strip().split(' ')
    if len(q)>2 and q[0].lower() == 'who' and q[1].lower() == 'created':
        # Find the query
        search = removePunctuation(' '.join(fullQuery.split(' ')[2:]))

        output = {}
        api_key = key
        service_url = 'https://www.googleapis.com/freebase/v1/mqlread'
        # Query for organization founders
        query = [{"organizations_founded":[{"a:name": None,"name~=": search}],"id":None,"name":None,"type":"/organization/organization_founder"}]

        params = {
                'query': json.dumps(query),
                'key': api_key
        }

        url = service_url + '?' + urllib.urlencode(params)
        response = json.loads(urllib.urlopen(url).read().decode('utf-8'))

        # If the api returns results add it to output.
        for founders in response['result']:
            founderDict = {}
            if founders['name'] not in output:
                output[founders['name']] = {"organizations":[],"books":[]}

            for organization in founders['organizations_founded']:
                output[founders['name']]["organizations"].append(organization['a:name'])

        # Query for book authors
        query = [{"works_written":[{"a:name":None,"name~=":search}],"id":None,"name":None,"type":"/book/author"}]
        params = {
                'query': json.dumps(query),
                'key': api_key
        }

        url = service_url + '?' + urllib.urlencode(params)
        response = json.loads(urllib.urlopen(url).read().decode('utf-8'))

        # If the api returns results add it to output.
        for authors in response['result']:
            authorDict = {}
            if authors['name'] not in output:
                output[authors['name']] = {"organizations":[],"books":[]}
            for books in authors['works_written']:
                output[authors['name']]["books"].append(books['a:name'])

        # Check if some valid results were returned by Freebase API.
        if len(output)>0:
            print("\n")
            for key in sorted(output):
                orgs = output[key]["organizations"]
                numOrganizations = len(orgs)
                if numOrganizations > 0:
                    outputString = key + ' (as BusinessPerson) created '
                    index = 0
                    for org in orgs:
                        if(index > 0 and (index + 1) < numOrganizations):
                            outputString = outputString + ', '
                        elif(index > 0):
                            outputString = outputString + ' and '
                        outputString = outputString + org
                        index = index + 1
                    print(outputString)
                books = output[key]["books"]
                numBooks = len(books)
                if numBooks > 0:
                    outputString = key + ' (as Author) created '
                    index = 0
                    for book in books:
                        if(index > 0 and (index + 1) < numBooks):
                            outputString = outputString + ', '
                        elif(index > 0):
                            outputString = outputString + ' and '
                        outputString = outputString + book
                        index = index  + 1
                    print(outputString)
            print("\n========================================================================\n")
        else:
            print("No results found.")
    else:
            print("Query: " + fullQuery + ", not in the correct format.")


#if __name__=='__main__':
#    QuestionAnswering("AIzaSyDYqLECS8jeMv18aAWdFgUQeA-AxD94jp8","Who created")