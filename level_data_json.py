from util import *

QUESTIONNAIRE: str = "questionnaire"
GAME: str = "game"

class LevelData:
    def __init__(self):
        self.id: str = None
        self.name: str = None
        self.type: str = None
        self.rounds_list: list[str] = None
    
    def __dict__(self):
        return {
            "name": self.name,
            "type": self.type,
            "rounds_list": self.rounds_list
        }

level_data: LevelData = LevelData()
level_number =             input("Enter ID (number): ")
level_data.name =          input("Enter name: ")
level_data.type =          input("Enter type [questionnaire (0) / game(1)]: ")
level_data.type = QUESTIONNAIRE if level_data.type == "0" else GAME
level_data.rounds_list =   input("Enter 3 round IDs (comma-separated): ").split(",")
level_data.island_id = input("Enter island ID: ")
level_data.id = "l" + str(level_number)
json_string = dict_to_json_string(level_data.__dict__())
json_string_to_file(json_string, generate_folder() + level_data.id + ".json")