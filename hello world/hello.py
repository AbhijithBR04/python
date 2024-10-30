# def func1():

#     a= 1
#     b =4
#     return  a+b


# result = func1()
# print(result)


my_list = [1,2,3,4,5,6,7,8,9,10,11,12]

evnt = filter(lambda num: num%2 == 0, my_list)

print(list(evnt))