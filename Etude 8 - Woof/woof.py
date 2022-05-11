import re


def woof(line):
    while True:
        original_line = line

        line = re.sub("(?<!e)[pqrs]", "woof", line)
        line = re.sub("Nwoof", "woof", line)
        line = re.sub("[CAKE]", "leader", line)
        line = re.sub("leaderwoofwoof", "woof", line)

        if line == original_line:
            break

    if line == "woof":
        print(line)
    else:
        print("not woof")


if __name__ == "__main__":
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        lines.append(line)

    for i in range(len(lines)):
        woof(lines[i])
