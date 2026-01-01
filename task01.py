people = [("Ali", 24), ("Laylo", 30), ("Jasur", 39)]


def find_oldest_person(people: list[tuple[str, int]]) -> tuple[str, int] | None:
    if len(people) == 0:
        return None
    
    oldest_person = people[0]
    for person in people:
        if person[1] > oldest_person[1]:
            oldest_person = person

    return oldest_person

print(f"{find_oldest_person(people)}")
