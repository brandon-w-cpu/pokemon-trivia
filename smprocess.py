
from scrapertest import addToDB
import pymongo
import math  
import time 
myclient = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false")
mydb = myclient["PokemonTrivia"]
mycol = mydb["AllPokemon"]
mycol.drop()

start = 1
end = 800
est_time = end - start * 1.5



print("Estimated runtime: " + str(math.floor(est_time / 60)) + " minutes and " + str(est_time % 60) + " seconds")
t0 = time.time()
for i in range(start, end):
    result = str(i)
    
    while len(result) < 3:
        result = "0" + result
    addToDB(result + ".shtml")

t1 = time.time()
total = math.floor(t1-t0)

print("Operation took " + str(math.floor(total / 60))+ " minutes and " + str(total % 60) + " seconds")


