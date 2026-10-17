#!/usr/bin/bash
# This file creates a user for the PerfReportDB database
# Update with your own configuration information and rename to "user.sh"
#
# Author: Josh McIntyre
#

# This block creates the user and grants read privileges
mongosh --eval "db.getSiblingDB(\"PerfReportDB\").createUser( \

	{ \
		\"user\" : \"PerfReportUser\", \
		\"pwd\" : \"MyPassword\", \
		\"roles\" : [ \"readWrite\" ] \
	}\
)"
