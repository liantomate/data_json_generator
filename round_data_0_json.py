from util import *

MULTIPLE_CHOICES: str = "multiple_choices"
MULTIPLE_SELECTION: str = "multiple_selection"
ARTICLE: str = "article"

class RoundData:
    def __init__(self):
        self.id: str = None
        self.type: str = None
        self.question: str = None
        self.options: list[str] = None
        self.points: list[int] = None
    
    def __dict__(self):
        return {
            "type": self.type,
            "question": self.question,
            "options": self.options,
            "points": self.points
        }

def call():
    round_data = RoundData()
    round_data.id = input("Enter id: ")
    round_data.type = input("Enter type [multiple_choices (0) / multiple_selection (1) / article (2)]: ")
    round_data.type = round_data.type == "0" and MULTIPLE_CHOICES or round_data.type == "1" and MULTIPLE_SELECTION or ARTICLE

    if round_data.type in [MULTIPLE_CHOICES, MULTIPLE_SELECTION]:
        round_data.question = input("Enter question: ")
        round_data.options = []
        round_data.points = []
        for i in range(4):
            option = input("Enter option: ")
            round_data.options.append(option[:-6].strip())
            round_data.points.append(int(option[-6:].replace("(", "").replace(")", "")
                                        .replace("pts", "").replace("pt", "")))

    round_data.id = "r" + round_data.id
    json_string = dict_to_json_string(round_data.__dict__())
    json_string_to_file(json_string, generate_folder() + round_data.id + ".json")