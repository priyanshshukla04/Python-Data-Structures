hero = ['spider man','thor','hulk','iron man','captain america']
#a
# 1
print(len(hero))

# 2
hero.append("Black Panther")
print(hero)

# 3
hero.remove("Black Panther")
index = hero.index("hulk")
hero.insert(index+1, "Black Panther")
print(hero)

# 4
hero[1:3] = ['doctor strange']
print(hero)

# 5
hero.sort()
print(hero)


#b
max_num = int(input())
odd_num = []
for i in range(max_num):
    if i%2 != 0:
        odd_num.append(i)

print(odd_num)
