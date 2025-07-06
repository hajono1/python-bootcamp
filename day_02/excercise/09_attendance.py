attendee_names = []

attendee_count = int(input("Attendee count: "))

for names in range(attendee_count):
    attendee_name = input("Attendee name: ")
    attendee_names.append(attendee_name)

print(attendee_names.index("Hajime"))

if "Hajime" in attendee_names:
    attendee_names.remove("Hajime")

attendee_late = attendee_names.pop(-1)

print(attendee_late)
print(attendee_names)
