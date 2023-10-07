import Metody_scenariusza
import Players_module

""" 1.Printujemy listę graczy z poniższych pozycji """

Metody_scenariusza.player_function("striker")
Metody_scenariusza.player_function("middle")
Metody_scenariusza.player_function("defender")
Metody_scenariusza.player_function("goalkeeper")

""" 2. Wpisujemy numer zespolu """

Metody_scenariusza.team_name_input()


""" 3. Wybieramy zawodnika. Jeśli wybór jest prawidłowy (dostępny w słowniku Players)
to tworzymy obiekt takiego piłkarza i dodajemy go do drużyny """


team_amount= 2
player_amount = 2
for team_no in range(1,team_amount):
    team_list= Metody_scenariusza.create_team()
    for player_no in range(1,player_amount):
        choice = Metody_scenariusza.player_choice_function()
        team_list.append(choice)

print("lista wybranych graczy to:",team_list)
print(getattr(team_list[0]), "surname")








