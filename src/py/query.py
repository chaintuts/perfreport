# A simple query configuration class
#
# Author: Josh McIntyre
#

class Query:

    def __init__(self, query_name, query_filename, query_outfile):

        self.query_name = query_name
        self.query_filename = query_filename
        self.query_outfile = query_outfile