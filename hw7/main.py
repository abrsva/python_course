import os


def subtract(a, b):
    return a - b


def unique_ascending(iterable):
    return sorted(set(iterable))


def write_something(dir, filename, content="abcdefgh"):
    os.makedirs(dir, exist_ok=True)
    with open(dir + "/" + filename, "w") as file:
        file.write(content)


if __name__ == "__main__":
    print(subtract(1, 2))
    print(unique_ascending([1, 2, 1, 1, 4, -1, -200]))
    write_something(r"C:\Users\anna2\PycharmProjects\programming_practice\python_course\hw7\res", "1.txt")
    write_something(r"C:\Users\anna2\PycharmProjects\programming_practice\python_course\hw7\res", "2.txt", "Barbariska")
