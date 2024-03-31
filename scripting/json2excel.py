import pandas as pd

class JSON2Excel:
    def __init__(self, json_data):
        self.json_data = json_data

    def convert(self, output_file):
        df = pd.read_json(self.json_data)
        df = df.T
        df.to_excel(output_file, index=True, header=True)
        
# Testing the JSON2Excel class
historical_data = JSON2Excel('scripting/historical_data.json')
historical_data.convert('historical_data.xlsx')