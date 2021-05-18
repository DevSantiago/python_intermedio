def read():
    numbers = []
    with open("./files/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)
        

def write():
    names = ["Pepe", "Fernando", "Alfonso", "Arturo", "Rocío"]
    with open("./files/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")
    print(f)
    append_name()

def append_name():
    names = ["Federico", "Leidy"]
    with open("./files/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    read()
    write()

if __name__ == "__main__":
    run()