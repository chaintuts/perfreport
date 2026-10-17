# This file contains code to query the MongoDB document database using the pre-configured query schemas
#
# Author: Josh McIntyre
#
import json
import pymongo
import tabulate

import auth.auth as auth
import query_config

# The query generator logic will parse the query JSON configuration,
# query the database, then perform combination and final projections
# The final projection data will be written out in HTML documents specified in the query config
def generate_query(database, query):

    # Load the query config from file
    with open(query.query_filename) as f:
        query_procedure = json.load(f)

    # Query the database, combining all specified main queries into a final list
    # This will include the find() filtering from the database query and projection (which columns to include/remove)
    # In addition, this will apply custom mappings between keys in the database to final mapped keys specified in the config
    data = []
    for q in query_procedure["queries"]:
        collection = q["collection"]
        find = q["find"]
        projection = q["projection"]
        mappings = q.get("mappings", None)
        sub_data = database[collection].find(find, projection)

        # Iterate over the items in the returned base dataset and perform key mappings
        # Append the final item to the list
        for item in sub_data:
            if mappings:
                # Look up the new key in mappings
                # If there is no new mapping, just use the original key as the default value
                mapped_item = { mappings.get(orig_key, orig_key) : value for orig_key, value in item.items() }
            else:
                mapped_item = item

            # Perform any configured sub queries and add data to the item in the configured manner
            # These will often have filters in the find to "join" based on items in the main query
            # Construct the find dict with the item from the main query
            # Then combine the final sub query data in the specified manner (such as a string join)
            # And add to the main item dictionary
            sub_query = q.get("sub_query", None)
            if sub_query:
                for k,v in sub_query["find"].items():
                    sub_find = { k: item.get(k) }
                sub_name = sub_query["name"]
                sub_collection = sub_query["collection"]
                sub_projection = sub_query["projection"]
                sub_action = sub_query["sub_query_action"]

                sub_query_data_raw = database[sub_collection].find(sub_find, sub_projection)

                sub_query_data = list(sub_query_data_raw)

                # For joins, grab the key for the items with wish to join
                # Construct a list of the actual values for the datapoints
                if sub_action == "join":
                    join_on = sub_query["sub_query_join_on"]
                    sub_query_list = [ v[join_on] for v in sub_query_data ]
                    sub_str = ", ".join(sub_query_list)
                item[sub_name] = sub_str

            # Append the final formatted item to the data list
            data.append(mapped_item)

    # Perform a final flattening of the data into tabular format
    # Use the specified column names from the config
    # For each column name, iterate over each item dict in data
    # Compile a list of values from each item dict using the column name as the key
    # Use the column name as the key in the final dict
    column_names = query_procedure["table_columns"]
    table_data = { colname : [ item[colname] for item in data ] for colname in column_names }

    table_formatted = generate_html_table(table_data, query)

    # Write the final query to file
    print(f"Generated query report for: {query.query_name}, writing to file: {query.query_outfile}")

    with open(query.query_outfile, "w") as f:
        f.write(table_formatted)

# Generate an HTML table using the table data in the format
# { key: [list of values] }
# We'll use the tabulate module, and apply some simple additional HTML formatting
def generate_html_table(table_data, query):

    base_table_formatted = tabulate.tabulate(table_data, headers="keys", tablefmt="html")
    base_table_formatted = base_table_formatted.replace("<table>", "<table border=\"1\">")

    header_formatted = f"<h3>{query.query_name}</h3>"

    table_formatted = f"{header_formatted}{base_table_formatted}"

    return table_formatted

# The main entry point for the program
def main():

    # This block generates a database connection
    conn_string = f"mongodb://{auth.USER}:{auth.PASSWORD}@localhost/{auth.DATABASE}"
    connection = pymongo.MongoClient(conn_string)
    database = connection[auth.DATABASE]

    for query in query_config.queries:

        generate_query(database, query)

if __name__ == "__main__":

    main()