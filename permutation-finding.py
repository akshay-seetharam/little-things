def intersperse(leader, perms: list) -> list:
    new_perms = []
    i = 0
    while i < len(perms):
        new_perms.append([*perms[:i], leader, *perms[i:]])
        i += 1
    new_perms.append([*perms, leader])
    return new_perms

def permutations(elements: list) -> list[list]:
    if len(elements) == 1:
        perms = [elements]
    else:
        perms = []
        for i in permutations(elements[1:]):
            perms.extend(intersperse(elements[0], i))

    return perms

def score_perm(l1, l2) -> int:
    diffs = []
    for i in l1:
        diffs.append(l2.index(i))

if __name__ == '__main__':
    print(permutations([1, 2, 3, 4]))