import json

#wytlumaczenie importowania jsona: https://www.tech-otaku.com/mac/using-python-to-loop-through-json-encoded-data/


f = open("players_dict_lista.json")
data = json.load(f)

for key,value in data.items():
    print("key to:", key, ", value to:", value)

print("printuje data[gracze]", data["gracze"])
print("\n", data["gracze"][0]["imie"])  #printuje pierwszy obiekt z listy gracze i z niego printuje imie
f.close()

f = open("../Json/players_dict_slownik.json")
data = json.load(f)

print("\n", "\n", "\n", data["gracze"][0]["napastnicy"][0]["imie"])

f.close()


