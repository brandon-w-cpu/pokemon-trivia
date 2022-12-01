import requests
from search import searchtable 
from bs4 import BeautifulSoup
import pymongo
import csv


def addToDB(pokemon): 
    print("Adding " + pokemon + " to database")

    
    URL = 'https://www.serebii.net/pokedex-sm/' + pokemon 

    
    pokemon.lower()
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')




    content = soup.find(id="content")
    main = content.find("main")
    tables = content.find_all("table", class_="dextable")

#Table for names and information
    nametable = tables[1]
    moves = (tables[9].text)
    
    if("Level" in moves or "Flavor" in moves):
        print("nice")
    else:
        moves = (tables[8].text)
        if("Level" in moves or "Flavor" in moves):
            print("nice")
        else:
            moves = (tables[7].text)

    #print(moves)
    moves = moves.split("\n")
    moves = moves[1:len(moves)]
    
    #moves = moves[1:len(moves)]
    count = 1
    append = ""
    movedict = {}
    blacklist = False
    tmset = False
    move = []
    
    print(movedict)
    for col in moves: 
        if(count == 1):
           move.append(col)
          # print(move[0])   
        elif(count == 2):
           move.append(col)
           movedict[move[0]] = move[1]
          # print(move[1])
           move = []
           #print("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
        count+=1
        count %= 9



           
        #if(count % 9 == 0):
        #    append += col + "\n"
        #    levelmoves.append(append)
        #    append = ""
        #    if("TM" in col):
        #        tmset = True
        #else: 
        #     append += col + ","
        #count+=1
    
    #print(levelmoves)
    #if(not levelmoves):
    #    blacklist = True



   # with open('mycsv.csv', 'w') as f: 
      #  writer = csv.writer(f)
       # writer.writerow

    names = nametable.find_all("td")
    name = names[5].text
    print(name)

    #name = searchtable(pokemon, names)
    #print(name)

    types = searchtable("cen", names).find_all("a")

    typelist = []
    for t in types:
        t = str(t)
        start = t.index("img alt=")+ 9
        t = t[start:len(t)]
        end = (t.index("\""))
        t = t[0: end]
        typelist.append(t)
    
    classification = searchtable("Pokémon", names)

    size = searchtable("Pokémon", names, 1)
    size = size.text
    size = size.split("\n")
    size[1] = size[1].strip()

    weight = searchtable("Pokémon", names, 2)
    weight = weight.text
    weight = weight.split("\n")
    weight[1] = weight[1].strip()


    
    
    
    #print(evochain)

    #evochain = evochain.split("img alt=")

    #print("Evolutionary Chain")
    #for i in range(1, len(evochain)): 
     #   print(evochain[i].split(" ")[0])

    #for count, t in enumerate(evochain) :
     #   endstr = ""
      #  if(count != 0):
         #   t = str(t)

          #  print(t)
            #if(count % 2 == 0):
              #  start = t.index(".png") - 2
              #  endstr = "."
              #  t = t[1:len(t)]
              #  endstr = "\""


            
        
        
        #end = (t.index(endstr))
        #t = t[0: end]
        #print(t)



    #print(classification.text)
    ##print(size.text)
    #print(weight.text)

    myclient = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false")
    mydb = myclient["PokemonTrivia"]

   

    mycol = mydb["AllPokemon"]
    pokemon = pokemon.replace(".shtml", "")

    pokemon = int(pokemon)
    print(pokemon)

    if(pokemon <= 151):
        region = "Kanto"

    elif(pokemon > 151 and pokemon <= 251):
        region = "Johto"
    elif(pokemon > 251 and pokemon <= 386):
        region = "Hoenn"
    elif(pokemon > 386 and pokemon <= 493):
        region = "Sinnoh"
    elif(pokemon > 493 and pokemon <= 649):
        region = "Unova"
    elif(pokemon > 649 and pokemon <= 721):
        region = "Kalos"
    elif(pokemon > 721 and pokemon <= 809):
        region = "Alola"

    mydict = {"dexno" : pokemon, "name": name, "region" : region, "classification": classification.text, "types" : typelist, "size": { "us" : size[0], "metric": size[1]}, "weight" : { "us" : weight[0], "metric": weight[1]}, "levelmoves" : movedict}
    x = mycol.insert_one(mydict)


