'''
dictionary:- dictionary is collection in python in which elements are stored in key and values pairs.
'''
'''
dict1={
"id":1001,
"name":"dhirendra",
"salary":100000
}
'''
#wap to understand concept of dictionary.

dict1={
"id":1001,
"name":"saurabh",
"salary":6000
}
print(type(dict1))#<class 'dict1'>
print(dict1)
for k,v in dict1.items():
	print(k,"=",v)