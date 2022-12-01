from querylist import *
import random
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false")
mydb = myclient["PokemonTrivia"]

allpokemon = mydb["AllPokemon"]
levelevos = mydb["LevelEvos"]
moves = mydb["Moves"]

myquery = { "dexno" : random.randint(1,21)}
pokemon = allpokemon.find(myquery)


whatRegion(pokemon)
whatTypes(pokemon)