## General
____________

### Author
* Josh McIntyre

### Website
* jmcintyre.net

### Overview
* PerfReport is a database application for further processing pre-compiled perceptron performance data

## Development
________________

### Git Workflow
* master for releases (merge development)
* development for bugfixes and new features

### Building
* make build
Build the application
* make clean
Clean the build and data directories

### Features
* Load database and userdata from shell scripts with mongosh
* Load the database with performance data from Perceptron machine learning models, like that from PercPerf JSON reports
* Generate further performance queries from the MongoDB database
* Write performance reports as HTML files for simple table viewing
* Uses custom Python logic and JSON configuration files to query MongoDB collections and combine data into final result/format

### Requirements
* Requires Python and MongoDB
* Requires performance report JSON files like those from the `PercPerf` repository

### Platforms
* Windows
* Linux
* MacOSX

## Usage
____________

### Initial Database Configuration
* Configure database users and authentication in files `auth.py` and `user.sh`
* Run `user.sh` to load the user configuration into MongoDB and generate the base database

### Command Line - Load Performance Database
* Update any necessary configuration in `reports_config.py` for your own usage
* Run `load_reports.py` to load the database with the JSON performance report data

### Command Line - Generate Queries
* Configure `query_config.py` with your own report usage
* Run `generate_queries.py`
* This will output HTML query files for viewing with a web browser or other HTML viewer
