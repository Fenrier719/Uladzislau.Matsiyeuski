import collections

def first(list):
    sum = 0
    for i in list:
        sum += i
    return sum

def second(list):
    return[item for item, count in collections.Counter(list).items() if count > 1]

def third(str):   
    return(str[::-1])

def fourth(list1,list2):
    result = list(list1+list2)
    return(list(collections.OrderedDict.fromkeys(result)))

def fifth(str):
   return(dict(collections.OrderedDict.fromkeys(str.split())))

def sixth(str):
    return(dict(collections.Counter(str.split())))
    


print(first([1, 2, 3, 5, 6, 8, 9]))
print(second([1, 1, 2, 3, 5, 5, 6]))
print(third('hello'))
print(fourth(['hello','hi'],['hi','bye']))
print(fifth('hi hi bye bye bye'))
print(sixth('hi hi bye bye bye'))