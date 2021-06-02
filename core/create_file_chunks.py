import json
import sys
import heapq


def merge_multiple_files(filenames):

    files = [open(filename, 'r') for filename in filenames]
    data = []
    merged = heapq.merge(*files)
    for d in merged:
        data.extend(json.loads(d))

    filtered_users = sorted(data, key=lambda i: i["user_id"], reverse=True)
    with open("output/output.json", 'w') as f:
        json.dump(filtered_users, f, indent=4)


def create_file_chunks(filename, lines_per_file=100) -> "List[str]":
    lines = []  # Stores lines not yet written on a small file
    lines_counter = 0  # Same as len(lines)
    created_files = 0  # Counting how many small files have been created
    filenames = []

    with open(filename) as big_file:

        for line in big_file:  # Go through the whole big file
            lines.append(line)
            lines_counter += 1
            if lines_counter == lines_per_file:
                idx = lines_per_file * (created_files + 1)
                temp_filename = "input/small_file_%s.json" % idx
                filenames.append(temp_filename)
                with open(temp_filename, "w") as small_file:
                    # Write all lines on small file
                    json.dump(lines, small_file)
                lines = []  # Reset variables
                lines_counter = 0
                created_files += 1  # One more small file has been created
        # After for-loop has finished
        if lines_counter:  # There are still some lines not written on a file?
            idx = lines_per_file * (created_files + 1)
            temp_filename = "input/small_file_%s.json" % idx
            filenames.append(temp_filename)
            with open(temp_filename, "w") as small_file:
                # Write them on a last small file
                json.dump(lines, small_file)
            created_files += 1

    return filenames


if __name__ == "__main__":

    filesize = 1000  # make into kb
    filename = "customers.txt"
    create_file_chunks(filename)
