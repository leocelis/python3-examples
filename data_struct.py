def get_intersection(list_a: list, list_b: list) -> list:
    """
    Link: https://stackoverflow.com/questions/3697432/how-to-find-list-intersection
    """
    intersection = list(set(list_a) & set(list_b))
    return intersection
