import importCSVdata, elec_num_importer, os

class Parliament:
    def __init__(self, year):
        self.provinces = [name for name in os.listdir("data/" + year + "/")]
        self.party_seats = dict()
        self.winning_candidates = list()
        self.elec_num = list()

    # pulls a combined list of elector numbers and the party name
    def get_party_seats(self, year):

        # creates an instance of the electoral number importer
        file_locator = elec_num_importer.ElectorNumber()

        # fetches the file names and file paths of the CSV files for the importer
        for x in range(0, len(self.provinces)):
            file_names = file_locator.get_file_names(year, self.provinces[x])

        # creates the list of parties to win each seat
        for files in file_names:
            election = importCSVdata.Riding(files)
            candidates_in_riding = election.get_totals(files)
            self.winning_candidates.append(max(candidates_in_riding, key=candidates_in_riding.get))
            self.elec_num.append(election.elec_num)

        # creates a dict of the winner of each seat with the elector number as a key
        for x in range(0, len(self.elec_num)):
            self.party_seats[self.elec_num[x]] = self.winning_candidates[x]


        return self.party_seats