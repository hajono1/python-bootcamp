invited = {"Ana", "Ben", "Carlo", "Dani"}
attended = {"Ben", "Carlo", "Ely"}

print("Involved Members: ", invited.union(attended))

print("Absent:", invited - attended)

print("Not enrolled but attended:", attended - invited)

print("Attended properly:", invited.intersection(attended))