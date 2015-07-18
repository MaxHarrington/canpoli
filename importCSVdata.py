import csv

class Riding:
    def __init__(self, file_location):

        # pulls in CSV file from correct province folder
        results = csv.DictReader(open(file_location))

        # sets name and elector number of riding
        for row in results:
            self.elec_name = row["Electoral District Name_English/Nom de circonscription_Anglais"]
            self.elec_num = row["Electoral District Number/Numéro de circonscription"]

    def get_totals(self, file_location):

        first_candidate = None
        last_candidate = None
        started_checking = False
        candidate_list = list()
        vote_totals = list()
        counter = 0
        self.combined_totals = dict()

        # pulls in CSV file from correct province folder
        results = csv.DictReader(open(file_location))

        for row in results:

            # starts checking for the names of each party with a candidate in the riding
            if started_checking is False:

                # imports a new set of results to avoid conflict with old set of results
                sub_results = csv.DictReader(open(file_location))
                for subrow in sub_results:

                    # sets the last candidate if the first candidate has been set
                    if started_checking is True:
                        last_candidate = subrow["Political Affiliation Name_English/Appartenance politique_Anglais"]
                        temp = last_candidate

                    # sets the first candidate and sets checking Boolean to true
                    if first_candidate is None:
                        first_candidate = subrow["Political Affiliation Name_English/Appartenance politique_Anglais"]
                        started_checking = True
                        temp = first_candidate

                    # ends checking process if the last candidate is the same as the first one
                    # also does not include independents, as multiple independents can run in one riding
                    if first_candidate == last_candidate:
                        break

                    candidate_list.append(temp)

            # creates an empty voter tally list
            if len(vote_totals) == 0:
                for x in candidate_list:
                    vote_totals.append(0)

            # adds the voter tally to the spot set by the counter
            vote_totals[counter] += int(row["Candidate Poll Votes Count/Votes du candidat pour le bureau"])

            counter += 1

            # resets the counter, as it will match the ordering and length of the candidate list
            if counter is len(candidate_list):
                counter = 0

        # creates a dictionary, combining the values with party names
        for x in range(0, len(candidate_list)):
            self.combined_totals[candidate_list[x]] = vote_totals[x]

        return self.combined_totals