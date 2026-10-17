# This file configures the desired queries to run
# Configure with your own final queries if desired
#
# Author: Josh McIntyre
#
import query

QUERY_DATASET_STRING_COUNT_FILENAME = "src/storage/query_dataset_string_count.json"
QUERY_MODEL_ACCURACY_WITH_STRINGS = "src/storage/query_model_accuracy_with_strings.json"

query_dataset_string_instances = query.Query("Instance Count of All Valid/Invalid Strings in Training Dataset", 
                                             QUERY_DATASET_STRING_COUNT_FILENAME, 
                                             "bin/queries/dataset_string_count.html")

query_model_accuracy_with_strings = query.Query("Per Model Accuracy with Inaccurately Predicted Valid Strings",
                                                QUERY_MODEL_ACCURACY_WITH_STRINGS,
                                                "bin/queries/model_accuracy_strings.html")

queries = [ query_dataset_string_instances,
            query_model_accuracy_with_strings
          ]
