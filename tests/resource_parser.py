def parse_resource_file(source_file_path):
    msg_idxs = []
    with open(source_file_path, "rb") as f:
        while True:
            line = f.read(4)
            if not line:
                break
            line_str = [i for i in line]
            print(line)


if __name__ == "__main__":
    # source_file_path = "resource/desc.dat"
    source_file_path = "resource/test.msg"
    parse_resource_file(source_file_path)
