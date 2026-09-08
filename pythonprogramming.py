# list
marks = [90, 80, 70, 60, 50]
print(marks, type(marks))

#operations on list
print("Length of list:", len(marks))
print(marks[0])
print(marks[-1])
#slicing
print(marks[1:4])
print(marks[:3])
print(marks[:])

#using loop 
for score in marks:
    print(score)
    
    #add some value at the end of the list
  #marks.append(40) 
  #print(marks)
  
  #add at particular index 
  #marks.insert(2, 75)
  #print(marks)
  
   #print(97 in marks)  # check if 97 is in the list
    
    
#tuple- immutable
marks = (90, 80, 70, 60, 50)
print(marks, type(marks))

# operations on tuple 
print("Length of tuple:", len(marks))
print(marks.count(70))  # count occurrences of 70
print(marks.index(60))  # find index of 60


## set - unordered collection of unique elements
marks = {90, 80, 70, 60, 80, 60, 50}
print(marks, type(marks))
print("Length of set:", len(marks))

for score in marks:
    print(score)
    
    #add some value to the set
  #marks.add(40) 
  #print(marks)
  
  #remove a value from the set
  #marks.remove(80)
  #print(marks)
  
   #print(97 in marks)  # check if 97 is in the set 
   
   
   # dictionary - key-value pairs
marks = {'Math': 90, 'Science': 80, 'English': 70}
print(marks, type(marks))
marks['History'] = 60  # add a new key-value pair
print(marks['English'])

for key in marks:
    print(key, marks[key])
    
    #remove a key-value pair
  #del marks['Science']
  #print(marks)
  
   #print('Math' in marks)  # check if 'Math' is a key in the dictionary
         