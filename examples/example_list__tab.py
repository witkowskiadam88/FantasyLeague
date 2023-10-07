
tab1 = [1, 4, 5]
tab2 = [2, 2, 2]
print(len(tab1))
print(tab1+tab2)
print(tab1[1])

print(tab2)
tab2.append(tab1[1])
print("tab2 after append tab1[1]",tab2)
tab2.pop(3)
print("tab2 after pop index 3",tab2)


tab3=[1,2,3,4],[5,6]
print(f"tab3 has to groups of data. group with index 0 is {tab3[0]}, group with index 1 is {tab3[1]}")


tab3=None
print(f"tab3={tab3}")