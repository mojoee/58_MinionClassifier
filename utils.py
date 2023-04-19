def get_classes(filepath="./classes.txt"):
    classes=[]
    with open(filepath, "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            classes.append(line)
    return classes
