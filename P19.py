my_dict = {'banana':3,'apple':1,'cherry':2,'dates':4}
print("Original list : ",my_dict)
assorted_dict = dict(sorted(my_dict.items()))
print("Ascending order : ",assorted_dict)
dsorted_dict = dict(sorted(my_dict.items(),reverse=True))
print("Descending order : ",dsorted_dict)
