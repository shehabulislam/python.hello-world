def lbs_to_kg(weight):
    return weight * 0.45359237


def kg_to_lbs(weight):
    return weight * 2.20462262184877


def find_max(lists):
    max = 0
    for i in lists:
        if i > max:
            max = i
    return max