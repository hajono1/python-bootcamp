attendee_names = set()

attendee_count = int(input("Attendee count: "))

for names in range(attendee_count):
    attendee_name = input("Attendee name: ")
    attendee_names.add(attendee_name)

attendee_names.discard("Hajime")

print(attendee_names)

raffle_winner = attendee_names.pop()
print("RAFFLE WINNER:", raffle_winner)