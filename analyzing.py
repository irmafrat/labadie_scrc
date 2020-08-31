# For Ephemera Collection

def counting_headers(input_filename:str, output_filename:str):
    counter = {}
    with open (input_filename, "r") as handler:
        line=handler.readline()
        while line:
            split = line.split(" - ")
            first_column = split[0].strip(" ")
            if first_column in counter:
                counter[first_column] += 1
                # counter.update({first_column: counter[first_column]+1})
            else:
                counter.update({first_column: 1})
            line=handler.readline()

    # print(counter)
    with open(output_filename, "w") as handler:
        for value, count in counter.items():
            handler.write("{} = {}\n".format(value, count))
            # print("{} = {}".format(value, count))


if __name__== "__main__":
    counting_headers("potential_ephemera.txt", "ephemera_subject_headings_count.txt")
    counting_headers("potential_collections.txt", "collections_subject_headings_count.txt")