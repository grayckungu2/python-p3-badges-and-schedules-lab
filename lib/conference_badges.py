def badge_maker(name):
    return "Hello, my name is {}.".format(name)

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(badge_maker(name))
    return badges

def assign_rooms(names):
    rooms = []
    for i, name in enumerate(names):
        rooms.append("Hello, {}! You'll be assigned to room {}!".format(name, i+1))
    return rooms

def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)
    for badge in badges:
        print(badge)
    for room in rooms:
        print(room)