
batu_dydziai = [("Jonas", 44), ("Petras", 42), ("Rokas", 39), ("Danas", 42), ("Martynas", 46), ("Laura", 44), ("Laura", 44), ("Jonas", 44), ("Petras", 44), ("Laura", 44)]

def most_common_size(sizes):
    new = []
    for size in sizes:
       new.append(size[1])
    counter = 0
    num = sizes[0]
    for i in new:
        curr_frequency = new.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num


def most_common_name_for_size(sizes):
    new = []
    for size in sizes:
        if size[1] == most_common_size(sizes):
            new.append(size[0])
    counter = 0
    num = sizes[0]
    for i in new:
        curr_frequency = new.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num


print(most_common_size(batu_dydziai))
print(most_common_name_for_size(batu_dydziai))