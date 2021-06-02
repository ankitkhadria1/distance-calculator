import os
import json

from .calculate_distance import CalculateDistance
from .create_file_chunks import create_file_chunks, merge_multiple_files


class GetUserDataByDistance(CalculateDistance):
    """
    Class to break customers data file into smaller chunks and filter out on the basis of distance and save it into smaller chunks
    and later using external merge sort combine them into one.

    """

    def __init__(
        self, starting_pos_lat, starting_pos_long, max_distance, customers_data_filename
    ):
        super(GetUserDataByDistance, self).__init__(starting_pos_lat, starting_pos_long)
        self.max_distance = max_distance
        self.customers_data_filename = customers_data_filename
        self.filenames = []
        self.output_filenames = []

    def break_largefile(self, lines_per_small_files):
        self.filenames = create_file_chunks(
            self.customers_data_filename, lines_per_file=lines_per_small_files
        )

    def read_customers_data(self):
        for filename in self.filenames:
            filtered_users = []
            with open(filename) as file:
                data = json.load(file)
                for line in data:
                    entry = json.loads(line)
                    distance = self.caluate_distance(
                        entry["longitude"], entry["latitude"]
                    )
                    if distance <= self.max_distance:
                        filtered_users.append(
                            {"name": entry["name"], "user_id": entry["user_id"]}
                        )

                filtered_users = sorted(filtered_users, key=lambda i: i["user_id"])

            # Save the data into files
            self.save_output(filename, filtered_users)

    def save_output(self, filename, filtered_users):
        # Save the data into files
        new_filename = filename.split(".")
        new_filename = new_filename[0].split("/")[1]
        output_filename = f"output/{new_filename}.json"
        self.output_filenames.append(output_filename)

        with open(output_filename, "w") as file:
            json.dump(filtered_users, file)
        

    def filter_customers(self):
        self.read_customers_data()

        merge_multiple_files(self.output_filenames)

        self.clear_temp_files()
    
    def clear_temp_files(self):

        for filename in self.output_filenames:
            os.remove(filename)

        for filename in self.filenames:
            os.remove(filename)

    

if __name__ == "__main__":

    home_office_lat = "53.339428"
    home_office_long = "-6.257664"

    user_data_obj = GetUserDataByDistance(home_office_lat, home_office_long)
    user_data_obj.get_customers()
