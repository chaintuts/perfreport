# This file contains a configuration for reports to load into the database
# Configure with your own desired report files config
#
# Author: Josh McIntyre
#
import report

REPORT_ACCURACY_PER_MODEL_FILENAME = "res/reports/accuracy_per_model.json"
REPORT_INVALID_STRINGS_DATASET_COUNT_FILENAME = "res/reports/invalid_strings_dataset_count.json"
REPORT_VALID_STRINGS_DATASET_COUNT_FILENAME = "res/reports/valid_strings_dataset_count.json"
REPORT_MODEL_INACCURATE_VALID_STRINGS_FILENAME = "res/reports/model_inaccurate_valid_strings.json"
REPORT_VALID_STRINGS_INACCURATE_ALL_FILENAME = "res/reports/valid_strings_inaccurate_all.json"

report_accuracy_per_model = report.Report("Accuracy Percentage Per Model", 
                                          "accuracyPerModel", 
                                          REPORT_ACCURACY_PER_MODEL_FILENAME)
report_invalid_strings_dataset = report.Report("Invalid Strings Count In Training Dataset", 
                                               "invalidStringsDataset", 
                                               REPORT_INVALID_STRINGS_DATASET_COUNT_FILENAME)
report_valid_strings_dataset = report.Report("Valid Strings Count In Dataset", 
                                             "validStringsDataset", 
                                             REPORT_VALID_STRINGS_DATASET_COUNT_FILENAME)
report_model_inaccurate_valid_strings = report.Report("Per Model Inaccurately Predicted Valid Strings", 
                                                      "modelInaccurateValidStrings", 
                                                      REPORT_MODEL_INACCURATE_VALID_STRINGS_FILENAME)
report_valid_strings_inaccurate_all = report.Report("Per All Valid String Inaccurately Predicted for All Models",
                                                    "validStringsInaccurateAll",
                                                    REPORT_VALID_STRINGS_INACCURATE_ALL_FILENAME)

reports = [ report_accuracy_per_model, 
            report_invalid_strings_dataset, 
            report_valid_strings_dataset, 
            report_model_inaccurate_valid_strings, 
            report_valid_strings_inaccurate_all ]
