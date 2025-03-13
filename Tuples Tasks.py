Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
academic_tuple=('Name','Father Name','Reg no','CGPA')
Mishaal_Reg=('SP24-BBA-111',)
number_tuple=(1,2,3,4,5)
string_tuple=('apple','orange','Guava')
mixed_tuple=(1,3.15,'apple',True)
single_tuple=(5,)
print(string_tuple[0])
apple
print(string_tuple[1])
orange
print(string_tuple[2])
Guava
print(string_tuple[-1])
Guava
print(string_tuple[-2])
orange
print(string_tuple[-3])
apple

string_tuple[0]=('Blueberry')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    string_tuple[0]=('Blueberry')
TypeError: 'tuple' object does not support item assignment
tuple1=(1,2,3)
tuple2=(4,5,6)
combined_tuple=tuple1+tuple2
print(combined_tuple)
(1, 2, 3, 4, 5, 6)
tuple1=('Mishaal')
repeated_tuple=tuple1*3
print(repeated_tuple)
MishaalMishaalMishaal
numbers=(1,2,3,4,5,6)
print(numbers[1:4])
(2, 3, 4)
print(numbers[:3])
(1, 2, 3)
print(numbers[4:])
(5, 6)
print(string_tuple.index('apple'))
0
string_tuple=('apple','orange','Guava','apple')
print(string_tuple.count('apple'))
2


for i in range(5):
    if i==3:
        break
    print(i)

    
0
1
2
for i in range(5):
    if i==3:
        continue
      print(i)

0
1
2
3
4














    

