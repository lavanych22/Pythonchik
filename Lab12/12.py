import re

if __name__ == "__main__":

    pattern = r"\S+\s-\s-\s\[(?:2[2-9]\/Mar\/2009|30\/Mar\/2009)\S+\s\S+\s\S(?:GET)\s\S+(?:style.css)\s\S+(?:[A-za-z\s\d\S]+)"
    number_of_matched_requests = 0  # Оголошення змінної
    read_lines = 0  # Оголошення змінної

    with open("access_log") as file:  # try with resources
        size = 0  # Оголошення змінної
        for line in file:
            read_lines += 1
            if re.match(pattern, line):
                number_of_matched_requests += 1
                print(re.findall(pattern, line))

    print("\nNumber of all read lines: %d" % read_lines)
    print("\nSize of all successfully requested css between 22/Mar/2009 and 30/Mar/2009: %d" % number_of_matched_requests)
