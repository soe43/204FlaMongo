import pymongo, json, urllib2
from pprint import pprint

"""
NAME: United States Population Table (Ages 0-100) in 2010

DESCRIPTION: This dataset contains information about the number of females and males of each age (0 to 100) in the U.S.

DOWNLOAD HYPERLINK: http://api.population.io/1.0/population/2010/United%20States/?format=json

IMPORT MECHANISM:
1. Uses urllib2 library to open the JSON file from the link to be read.
2. .loads turns JSON object into a dictionary.
3. Creates the database "gaoJsoeW" and collection "population".
4. Inserts documents into the collection "population".  There is one document for each age; each document contains the age, number of females, number of males, and the total (females + males).

"""

###Another way of retrieving JSON data (by using .JSON file downloaded):
#data=json.load(open('Population.json'))

connection = pymongo.MongoClient('149.89.150.100')
db=connection.gaoJsoeW
collection=db.population

def createDB():
    u=urllib2.urlopen("http://api.population.io/1.0/population/2010/United%20States/?format=json")
    data=u.read()
    eventDict=json.loads(data)
    for i in range(len(eventDict)):
        age=eventDict[i]["age"]
        numFemales=eventDict[i]["females"]
        numMales=eventDict[i]["males"]
        total=eventDict[i]["total"]
        db.population.insert({"age":age, "females":numFemales, "males":numMales, "total":total})

#Search for population statistics (number of females/males/total) by age
def ageSearch(age):
    results=collection.find({"age": age})
    a=[]
    for i in results:
        a.append(i)
    return pprint(a)

#Search for ages where the number of females is less than or equal to the population specified
def femalePopLessThanEqualTo(population):
    results=collection.find({"females": {"$lte":population}})
    a=[]
    for i in results:
        a.append(i)
    return pprint(a)

#Search for ages where the number of males is greater than or equal to the population specified
def malePopGreaterThanEqualTo(population):
    results=collection.find({"males": {"$gte":population}})
    a=[]
    for i in results:
        a.append(i)
    return pprint(a)

#Search for ages where the number of females or the number of males is less than the population specified
def popLessThan(population):
    results=collection.find({"$or":[{"males": {"$lt":population}}, {"females":{"$lt":population}}]})
    a=[]
    for i in results:
        a.append(i)
    return pprint(a)

#Search for total population greater than the population specified at an age greater than or equal to the age specified
def totalGreaterThanAtAgeGreaterThanEqual(population, age):
    results=collection.find({"total":{"$gt":population},"age":{"$gte":age}})
    a=[]
    for i in results:
        a.append(i)
    return pprint(a)

#createDB()
#Creates database.  Should only call once to avoid duplicate documents.

#Tests ageSearch method
#ageSearch(100)

#Test femalePopLessThanEqualTo method
#femalePopLessThanEqualTo(51200)

#Test malePopGreaterThanEqualTo method
#malePopGreaterThanEqualTo(2054000)

#Test popLessThan method
#popLessThan(64800)

#Test totalGreaterThanAtAgeGreaterThanEqual method
#totalGreaterThanAtAgeGreaterThanEqual(1000000,76)
