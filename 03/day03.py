def get_prios(i: str):
    if ord(i) > 90:
        return ord(i) - 96
    return ord(i) - 38


def get_backpack_item_priorities(backpacks):
    collection = []
    for rucksack in backpacks:
        content = rucksack.rstrip("\n")
        compartment_a = content[:int(len(content) / 2)]
        compartment_b = content[int(len(content) / 2):]
        collection.append(*get_duplicates(compartment_a, compartment_b))
    return sum([get_prios(x) for x in collection])


def get_group_priorities(backpacks):
    collection = []
    indexes = list(range(len(backpacks)))[0::3]
    for i in indexes:
        member_a = backpacks[i].rstrip("\n")
        member_b = backpacks[i+1].rstrip("\n")
        member_c = backpacks[i+2].rstrip("\n")
        duplicates_one = get_duplicates(member_a, member_b)
        duplicates_two = get_duplicates(member_c, member_b)
        duplicates_three = get_duplicates(member_a, member_c)
        collection.append(*(set(duplicates_one) & set(duplicates_two) & set(duplicates_three)))
    return sum([get_prios(x) for x in collection])


def get_duplicates(string_a, string_b):
    items_a = set([*string_a])
    items_b = set([*string_b])
    return list(items_a & items_b)


if __name__ == '__main__':
    with open("./input.txt") as file:
        rucksack_list = file.readlines()

    print(get_backpack_item_priorities(rucksack_list))
    print(get_group_priorities(rucksack_list))
