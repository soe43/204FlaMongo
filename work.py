import pymongo
from pprint import pprint

connection = pymongo.MongoClient('149.89.150.100')
db = connection.test
collection = db.restaurants

#All restaurants in a specified borough.
def boroughSearch(borough):
    results = collection.find({'borough' : borough})
    a=[]
    for i in results:
        a.append(i)
    return pprint(a)

#All restaurants in a specified zip code.
def zipCodeSearch(zipcode):
    results=collection.find({'address.zipcode':zipcode})
    a=[]
    for i in results:
        a.append(i)
    return pprint(a)

#All restaurants in a specified zip code and with a specified grade.
def zipcodeGrade(zipcode, grade):
    results=collection.find({'address.zipcode':zipcode, 'grades.grade':grade})
    a=[]
    for i in results:
        a.append(i)
    return pprint(a)

#All restaurants in a specified zip code with a score below a specified threshold.
def score(zipcode, score):
    results=collection.find({'address.zipcode':zipcode, 'grades.score':{"$lt": score}})
    a=[]
    for i in results:
        a.append(i)
    return pprint(a)

#Search for restaurants by cuisine in a specified borough and with a specified grade.
def cuisineGradeBorough(cuisine, grade, borough):
    results=collection.find({'borough':borough, 'grades.grade':grade, 'cuisine':cuisine})
    a=[]
    for i in results:
        a.append(i)
    return pprint(a)

##TEST CASES
#print boroughSearch('Manhattan')
#print zipCodeSearch('10017')
#print zipcodeGrade('10017', 'B')
#print score('10017', 1)
#print cuisineGradeBorough("American", "A", "Queens")
