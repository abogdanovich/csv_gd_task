import argparse
import json
import os
import sys
import gdown
import pandas as df
from pathlib import Path

arg_parser = argparse.ArgumentParser(
    description="CSV data parsing tool from some URL"
)
arg_parser.add_argument(
    "--csv-path",
    metavar="csv_path",
    required=False,
    type=str,
    help="the path to the CSV file",
)

arg_parser.add_argument(
    "--csv-url",
    metavar="csv_url",
    required=False,
    type=str,
    help="the path to the CSV file at Google Drive",
)

arg_parser.add_argument(
    "--csv-fields",
    metavar="csv_fields",
    required=True,
    type=str,
    help="the path to the CSV file",
)


class CSVParser:
    """Main class to handle CSV data from URL"""

    def __init__(self):
        self._url = None
        self._fields = ["date", "campaign", "clicks", "spend", "medium", "source"]
        self._filename = "test_task_data.csv"

    @property
    def fields(self):
        return self._fields

    @property
    def filename(self):
        return self._filename

    def parse_fields_params(self, fields_params: str):
        """Parse input fields"""
        fields = None
        try:
            # try to split input fields and decide what to do
            fields = fields_params.replace(" ", "").split(",")
            is_accessible, wrong_fields = self.check_available_input_params(fields)
            if not fields or not is_accessible:
                if wrong_fields:
                    print(f"Wrong input fields that will be skipped: {wrong_fields}")

                print(f"All available fields: {self.fields}\n"
                      f"For multi fields usage, split fields by ','\n"
                      f"Example: {Path(os.path.abspath(__file__))} --csv-fields {','.join(self.fields)}")

        except ValueError as e:
            print(f"Not ok input fields. Please verify: {e}")

        return [x for x in fields if x in self.fields]

    def load_csv_from_url(self, url: str, file_id=None):
        """Download file from url"""
        status = 0
        output_file = None
        try:
            print(f"Try to load url: {url}")
            if not file_id:
                # try to extract file id from the given url
                url = [x for x in url.split("/") if len(x) > 0]
                if len(url) > 5:
                    file_id = url[4]
                else:
                    raise ValueError(f"Can't properly parse the given Google Drive url!")
            output_file = gdown.download(id=file_id, quiet=False, verify=False)

        except Exception as e:
            print(f"ERROR: The given url has the wrong format or permissions! "
                  f"Please verify the input parameter --csv-url {e}")
            status = -1

        if not output_file:
            status = -2
        return status

    def load_csv(self, file_path: str):
        """Load data from file specified by user or default one"""
        data = df.DataFrame([])
        try:
            data = df.read_csv(file_path)
        except FileNotFoundError as e:
            print(f"The given file: {file_path} doesnt not exists! Details: {e}")
        return data

    def check_available_input_params(self, params):
        """Return False if at least on input params is not ok"""
        status = True
        _wrong_params = []
        for param in params:
            if param not in self._fields:
                status = False
                _wrong_params.append(param)
        return status, _wrong_params

    def load_fields_data(self, fields: list, data: dict):
        """Return the list of data for a specified fields"""
        json_serialization = None
        try:
            print(f"Print the requested fields: {fields}")
            requested_data = {
                "data": data[fields].to_dict()
            }
            json_serialization = json.dumps(requested_data)
        except KeyError as e:
            print(f"Something is not ok with data for fields: {fields}: {e}")

        return json_serialization


if __name__ == "__main__":
    args = arg_parser.parse_args()
    parser = CSVParser()
    csv_data = None

    # download csv file from Google Drive and dump into local file
    if args.csv_url:
        parser.load_csv_from_url(args.csv_url)

    csv_local_file = args.csv_path if args.csv_path else parser.filename
    # try to load CSV file from local file
    csv_data = parser.load_csv(csv_local_file)

    if csv_data.empty:
        print(f"Can't proceed with the specified file. Wrong format or file!")
        sys.exit(2)

    if args.csv_fields:
        print_fields = parser.parse_fields_params(args.csv_fields)
        if print_fields:
            requested_data = parser.load_fields_data(print_fields, csv_data)
            print(requested_data)