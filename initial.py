name = 'Den'
age = 34

print('----------------- f\'My name is {name} and i am {age}\' -----------------------\n')
print(f'My name is {name} and i am {age}')

spam = [0, "one", "two", "tree", "four", "five"]

print('-------------------- spam --------------------\n')
print(spam)
print(f'len(spam): {len(spam)}')
print('\n')

print('------------------spam[5]----------------------\n')
print(spam[5])
print(f'len(spam): {len(spam)}')
print(spam)
print('\n')

print('-------------------spam[int(5.0)]---------------------\n')
print(spam[int(5.0)])
print(f'len(spam): {len(spam)}')
print(f'len(spam[int(5.0)]): {len(spam[int(5.0)])}')
print(spam)
print('\n')

print('------------------- append six---------------------\n')
spam.append('six')
print(f'len(spam): {len(spam)}')
print(spam)
print('\n')
print('------------------- remove 0 ---------------------\n')
spam.remove(spam[0])
print(f'len(spam): {len(spam)}')
print(spam)
print('\n')
print('------------------- remove 5 ---------------------\n')
spam.remove(spam[5])
print(f'len(spam): {len(spam)}')
print(spam)
print('\n')
print('------------------- insert Triple Seven ---------------------\n')
spam.insert(777, 'Triple Seven')
print(f'len(spam): {len(spam)}')
print(spam)
print('\n')
print('------------------- spam6 ---------------------\n')
print(f'len(spam): {len(spam)}')
print(spam)
print('\n')
print('------------------- pop(5) ---------------------\n')
spam.pop(5)
print(f'len(spam): {len(spam)}')
print(spam)



