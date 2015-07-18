import importCSVdata, elec_num_importer, os

class Parliament:
    def __init__(self, year):
        self.provinces = [name for name in os.listdir("data/" + year + "/")]
        self.party_seats = dict()
        self.winning_candidates = list()
        self.elec_num = list()


    def get_party_seats(self, year):
        file_locator = elec_num_importer.ElectorNumber()

        for x in range(0, len(self.provinces)):
            file_names = file_locator.get_file_name(year, self.provinces[x])

        for files in file_names:
            election = importCSVdata.Riding(files)
            candidates_in_riding = election.get_totals(files)
            self.winning_candidates.append(max(candidates_in_riding, key=candidates_in_riding.get))
            self.elec_num.append(election.elec_num)

        for x in range(0, len(self.elec_num)):
            self.party_seats[self.elec_num[x]] = self.winning_candidates[x]

        print(self.party_seats)

        return self.party_seats