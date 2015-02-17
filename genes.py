from random import randint

n = ['A','T','C','G']
length = 80

sequence = []

for i in xrange(4000):
    num = randint(0,3)
    sequence.append(n[num])

# print sequence[:5]

def best(list, length):

    goal = [0,0]
    
    for i in xrange(len(list)-(length-1)): # last  to be counted together
        l = list[i:i+length]
        count = l.count('A') + l.count('T')
  
#        print l,'\n',i,count
        current = [i,count]
#        print current
        
        if current[1] > goal[1]:
            goal = current
     
#        print goal
    
    return goal


index,amount = best(sequence)

start = index
stop = index + length

print index, amount
print sequence[start:stop].count('A')+sequence[start:stop].count('T')
