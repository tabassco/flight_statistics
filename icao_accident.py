from typing import List

import json


class ICAOAccident:
    def __init__(self):
        self.date = None
        self.state_of_occurence = None
        self.location = None
        self.model = None
        self.registration = None
        self.operator = None

        self.incident_class = None


    def __str__(self):
        return \
            f"""{self.incident_class}: 
                On: {self.date}
                In: {self.location}
                By: {self.operator}
             """

    def read_accident_file(self, filename: str) -> List:
        with open(filename) as accident_list_file:
            accidents = json.load(accident_list_file)

        print(accidents[0])


        accident_list = []



        return accident_list


if __name__ == '__main__':
    accident = ICAOAccident()

    # accident.read_accident_file("data/accident.json")


    import pandas as pd

    data = pd.read_json("data/accident.json")

    print(data.Class.unique())

    print(data.head())

    print(list(data))
