# A class for managing report details for loading into a database
#
# Author: Josh McIntyre
#

class Report:

    def __init__(self, report_name, report_collection, report_filename):

        self.report_name = report_name
        self.report_collection = report_collection
        self.report_filename = report_filename