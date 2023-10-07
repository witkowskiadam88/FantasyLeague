tuple1 = (1, 5, "pies")

print("dlugosc krotki to:", len(tuple1))
print("tuple[0] to:",tuple1[0])
print("tuple[1] to:",tuple1[1])
print("tuple[2] to:",tuple1[2])

for i in reversed(range(len(tuple1))):
    print(f"for i ={i} tuple[{i}] = {tuple1[i]}")



