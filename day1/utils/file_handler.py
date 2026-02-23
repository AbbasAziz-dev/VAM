def read_file(filename):
    try:
        file = open(filename, "r")
        content = file.read()
        file.close()
        return content
    except FileNotFoundError:
        print("Error: File not found")
        return ""


def write_file(filename, content):
    try:
        file = open(filename, "w")
        file.write(content)
        file.close()
    except:
        print("Error: Unable to write to file")