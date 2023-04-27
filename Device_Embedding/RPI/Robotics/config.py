def read(key, config_file="config.txt"):
    config = open(config_file, "r")
    config_lines = config.readlines()
    for line in config_lines:
        split_line = line.split(" ")
        if split_line[0] == key:
            val = split_line[1]
    config.close()
    return val

def write(key, val, config_file="config.txt"):
    config = open(config_file, "r")
    config_lines = config.readlines()
    config.close()
    config = open("config.txt", "w")
    for i in range(len(config_lines)):
        split_line = config_lines[i].split(" ")
        if split_line[0] == key:
            split_line[1] = str(val) + "\n"
            config_lines[i] = " ".join(split_line)
    config.write("".join(config_lines))
    config.close()
