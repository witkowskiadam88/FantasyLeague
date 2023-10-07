import json
import Players_module

"""wytlumaczenie importowania jsona: https://www.tech-otaku.com/mac/using-python-to-loop-through-json-encoded-data/ """

def player_function(position):
    file_path = open("../Fantasy_League/players_dict.json")
    players_dict_json_file = json.load(file_path)

    print("\n",position,":")
    for player_step in players_dict_json_file["players"][position]:
        print(player_step.upper(),"(", players_dict_json_file["players"][position][player_step]["skill"], ")")
        for key, value in players_dict_json_file["players"][position][player_step].items():
            print(key, ":", value)
        print("####################")

    file_path.close()


def player_choice_function():
    # print(f"\n\n Wybierz zawodnika nr {i + 1} wpisując jego imie i nazwisko")
    player_input = input()
    # print(f"wybrales zawodnika {player_input}")
    player_picked = Players_module.Players.player_create_object(player_input, None, None, None, None, None, None, None,None)
    # print("Jego wiek to:", getattr(player_picked, 'age'))
    # print("printuje player_choice_function ",player_picked)
    return player_picked


def create_team():
    team = []
    return team

def player_picked_to_team(*args):

    player1 = args
    team.append(player1)

