"""Convert RIS to CSV."""

import os
import csv
import re


def test_ris_file_exists(ris_path):
    """Test if an RIS file exists.

    Returns:
        True -- if file can be opened
        False -- if file cannot be opened

    """
    try:
        open(ris_path, 'r')
        return True
    except IOError:
        return False

def blank_row():
    """Create and return a blank, 80 item long list."""
    row = []
    for i in range(0, 81, 1):  # pylint: disable=W0612
        row.append(None)
    return row

def main(): # pylint: disable=R0914
    """Open RIS file, take data, convert to CSV using REGEX."""
    print("""
    Please enter the relative or full path to the RIS file you would 
    like to convert to a CSV file.
          """)
    ris_path = input("> ")

    if test_ris_file_exists(ris_path) is False:
        print("That path appears invalid. Please try again.\n")
        main()
        exit(0)


    print("""
    Please enter the relative or full path to the location you would like your 
    new csv saved, as well as the filename for the new csv file. 
    
    Eg. "~/Documents/ris_report.csv" (without the quotation marks)
          """)
    csv_path = input("> ")

    ris_std = open("./RIS_stds.csv", 'r')
    csv_file = open(csv_path, 'w')
    writer = csv.writer(csv_file, dialect='excel')
    column_num = {}
    row = blank_row()
    for i, line in enumerate(ris_std):
        line_token_list = line.split(",")
        column_num[line_token_list[0]] = int(line_token_list[2]) - 1
        row[i] = "{0} ({1})".format(line_token_list[1], line_token_list[0])
    ris_std.close()
    writer.writerow(row)
    row = blank_row()


    ris_file = open(ris_path, 'r')
    ris_text = ris_file.read()
    ris_text = ris_text.replace("\n", " ")
    ris_file.close()
    regex = re.compile(
        r'(?<=([A-Z][A-Z0-9]  - ))(.*?)(?=([A-Z][A-Z0-9]  - ))')
    # ^ This uses a "positive lookbehind" [(?<=...)] to start the match after
    # '...', then uses a non-greedy (?) wildcard to iteratively move forward
    # until BEFORE the final matched expression , which is done with a
    # positive lookahead [(?=...)]
    matches = re.findall(regex, ris_text)  # Create a list with .findall()
    print("Here are all the matches for your regex: ")
    for match in matches:
        ris_id = match[0][0] + match[0][1]
        ris_data = match[1]
        row[column_num[ris_id]] = ris_data
        print("""
        ris_id = {0}
        ris_data = {1}
              """.format(ris_id, ris_data))
        if ris_id == "ER":
            writer.writerow(row)
            row = blank_row()
    csv_file.close()
    print("""
    Conversion process complete. 
    
    Your new file is located here: {0}""".format(os.path.abspath(csv_path)))
    return


if __name__ == "__main__":
    print("Welcome to the RIS>CSV Converter.")
    main()
