from typing import List

import pandas as pd

from  alertAndMonitoringChecks import Checks, Duplicate, CyclicHierarchy, YesterdayMissingCSN, ValidCSN, NotInSFDC
import sdh_common_utilities
import email_utiltiy

class AlertAndMonitoring:

    def __init__(self, check : str = None):
        self.check = check

    @property
    def check(self):
        return self.check
    @check.setter
    def check(self, check):
        self.check = check

    def action(self, result: dict, test: dict) -> None:

        for action in test["actions"]:
            # TODO
            # perform an action using test dict
            # And result of the test
            # Send Emails mostly

    def performCheck(self, checkName : str, df_key):

        checkClass = None

        if checkName == "duplicates":
            checkClass = Duplicate()
        elif checkName == "cyclic":
            checkClass = CyclicHierarchy()
        elif checkName == "notinsfdc":
            checkClass = NotInSFDC()
        elif checkName == "missingcsn":
            checkClass == YesterdayMissingCSN()
        elif checkName == "validcsn":
            checkClass = ValidCSN()
        else:
            throw Error "Please enter a valid Check"

        return Checks(checkClass).check(df_key)



if __name__ == '__main__':

    # List of checks possible
    # Add a new check every time there is any addition to the list
    list_of_checks = ["duplicates", "cyclic", "notinsfdc", "missingcsn", "validcsn"]

    # Read alertandmonitoring.json
    alertandmonitoring = read.json(alertandmonitoring.json)

    for project in alertandmonitoring:

        # Create Pandas DF for Pipeline Health Depiction
        df = pd.DataFrame()
        df = pd.concat([df, pd.DataFrame(columns=list_of_checks)])  # Add columns

        for datapoint in project:
            # Make Result as NA for all checks for current Data Point
            df2 = {test: "NA" for test in list_of_checks}
            df2["data_point"] = datapoint
            for test in project[datapoint]["tests"]:

                # Do the processing for a Check
                resultDict = AlertAndMonitoring(test["test_name"], DF_Key)
                df2[test["test_name"]] = resultDict["result"]

                # Actions if any required
                if resultDict["result"] == "Failed" and test["action_required"] == "YES":
                    # Do the required
                    # Send Email to stake holders
                    # Using test["actions"] pass into Class AlertAndMonitoring

            print(df2)

            df = df.append(df2, ignore_index=True)