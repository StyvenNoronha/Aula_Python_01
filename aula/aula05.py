'''
l1 = [1,2,3,4,5,6,6,6,6,6,6,6,6,6,7,8,9]
l1 = list(set(l1))
print(l1)
print(6 in l1)
print(10 not in  l1)
for i in l1:
    print(i)
l1 = set()
l1.update([2,3,4,5,6,7,8,9,10])    
l1.add('styven')  
#l1.clear()
l1.discard('styven')
print(l1)
'''
s1 = {1,2,3,4,5}
s2 = {0,1,2,3,4,5,6,7,8,9,10}
s3 = s1 | s2 #união
s4 = s1 & s2 #a junta os elementos iguais
s5 = s1 - s2 #diferença
print(s5)