from util import *

class IslandData:
    def __init__(self):
        self.id: str = None
        self.name: str = None
        self.description: str = None
        self.texture_id: str = None
        self.levels_list: list[str] = None
    
    def __dict__(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "texture_id": self.texture_id,
            "levels_list": self.levels_list
        }

island_data: IslandData = IslandData()
island_number =             input("Enter ID (number): ")
island_data.name =          input("Enter name: ")
island_data.description =   input("Enter description: ")
island_data.texture_id =    input("Enter texture ID: ")
island_data.levels_list =   input("Enter 3 level IDs (comma-separated): ").split(",")

island_data.id = "island_" + str(island_number)
json_string = dict_to_json_string(island_data.__dict__())
json_string_to_file(json_string, generate_folder() + "island_" + island_data.id + ".json")
