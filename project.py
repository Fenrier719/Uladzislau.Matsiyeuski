import collections

def first(my_list_with_numbers):
    return(sum(my_list_with_numbers)) 

def second(my_list):
    my_list1 = set(my_list)
    return[x for x in my_list1 if my_list.count(x) > 1]

def third(str_):   
    return(str_[::-1])

def fourth(my_list1,my_list2):
    result = list(my_list1+my_list2)
    return(list(set(result)))

def fifth(str_):
   return(list(set(str_.split())))

def sixth(str_):
    return(dict(collections.Counter(str_.split())))
    


print(first([1, 2, 3, 5, 6, 8, 9]))
print(second([1, 1, 2, 3, 5, 5, 6]))
print(third('hello'))
print(fourth(['hello','hi'],['hi','bye']))
print(fifth('hi hi bye bye bye'))
print(sixth('hi hi bye bye bye'))