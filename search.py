
def searchtable(word, table, offset=0):
    count = 0
    result = ""
    for entry in table: 
        if(word in str(entry)):
            result = table[count + offset]
            break
        count+=1
    return result


