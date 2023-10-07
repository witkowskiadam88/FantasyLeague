import json

file_path = open("fantasyleague/FL_project/players_dict.json")
players_dict_json_file = json.load(file_path)

class Players:
    def __init__(self, dict_main, position_dict, player, name, surname, age, position, skill):
        self.dict_main = dict_main
        self.position = position_dict
        self.player = player
        self.name = name
        self.surname = surname
        self.age = age
        self.position = position
        self.skill = skill

    @classmethod
    def player_create_object(cls, chosen_player, dict_main, position_dict, player, name, surname, age, position, skill):
        for dict_main_step in players_dict_json_file:
            for position_step in players_dict_json_file[dict_main_step]:
                for player_step in players_dict_json_file[dict_main_step][position_step]:
                    if player_step == chosen_player:
                        player = chosen_player
                        position_dict = position_step
                        dict_main = dict_main_step
                        name = players_dict_json_file[dict_main][position_dict][player]["name"]
                        surname = players_dict_json_file[dict_main][position_dict][player]["surname"]
                        age = players_dict_json_file[dict_main][position_dict][player]["age"]
                        position = players_dict_json_file[dict_main][position_dict][player]["position"]
                        skill = players_dict_json_file[dict_main][position_dict][player]["skill"]

                        return cls(player, dict_main, position_dict, name, surname, age, position, skill)

