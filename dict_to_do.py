to_do = {
        "monday": ["lean python","read", "sport"],
        "tuesday": ["reading","lean python","read" ],
        "wednesday":["cooking"],
        "thursday":["Jogging","lean python","read"],
        "friday": ["laundry", "walk"],
        "saturday":["walk"],
        "sunday":["church"]
    }

for days in to_do.keys():
    print(days)
    for tasks in to_do[days]:
        print( to_do[days])
        #print(tasks)

'''for days in to_do.items():
    print(days)'''