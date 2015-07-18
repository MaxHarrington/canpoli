import os

class ElectorNumber:
    def __init__(self):
        self.file_list = list()
        self.num_list = list()

        # pulls all the CSV file names in the 'data' directory

    def get_file_name(self, year, province):
        for file in os.listdir("data/" + year + "/" + province):
            if file.endswith(".csv"):
                self.file_list.append("data/" + year + "/" + province + "/" + file)
        return self.file_list