# This file contains a make script for the PerfReport application
#
# Author: Josh McIntyre
#

# This block defines makefile variables
SRC_FILES=src/py/*.py 
AUTH_FILES=src/auth/*.py
DB_FILES=src/storage/user.sh
MONGODB_QUERY_FILES=src/storage/*.json
RES_FILES=res/reports/*.json

BUILD_DIR=bin/perfreport
AUTH_DIR=bin/perfreport/auth
DATA_DIR=bin/data

# This rule builds the application
build: $(SRC_FILES) $(RES_FILES)
	mkdir -p $(BUILD_DIR)
	cp $(SRC_FILES) $(RES_FILES) $(BUILD_DIR)
	cp $(MONGODB_QUERY_FILES) $(BUILD_DIR)
	mkdir -p $(AUTH_DIR)
	cp $(AUTH_FILES) $(AUTH_DIR)

# This rule cleans the build and data directories
clean: $(BUILD_DIR) $(DATA_DIR)
	rm $(BUILD_DIR)/* $(DATA_DIR)/*
	rmdir $(BUILD_DIR) $(DATA_DIR) 
