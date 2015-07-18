import os

class ElectorNumber:
    def __init__(self):
        self.file_list = list()
        self.num_list = list()

    def get_file_names(self, year, province):
        for file in os.listdir("data/" + year + "/" + province):
            if file.endswith(".csv"):
                self.file_list.append("data/" + year + "/" + province + "/" + file)
        return self.file_list
        self.file_list.clear()