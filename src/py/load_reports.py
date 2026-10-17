# This code loads existing performance reports from JSON documents,
# such as reports generated from SQL queries in PercPerf
# This will insert report collections for later queries
#
# Author: Josh McIntyre
#

import json
import pymongo

import auth.auth as auth
import reports_config

def load_report(database, report):

    with open(report.report_filename) as f:
        data = json.load(f)
        collection = database[report.report_collection]
        for datapoint in data:
            print(f"Load datapoint for {report.report_collection}: {datapoint}")
            collection.insert_one(datapoint)

# The main entry point for the program
def main():

    # This block generates a database connection
    conn_string = f"mongodb://{auth.USER}:{auth.PASSWORD}@localhost/{auth.DATABASE}"
    connection = pymongo.MongoClient(conn_string)
    database = connection[auth.DATABASE]

    for report in reports_config.reports:

        load_report(database, report)

if __name__ == "__main__":
    main()