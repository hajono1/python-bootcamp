student_scores = [98, 75, 100, 86, 100, 3]

#
lowest_score = min(student_scores)
print("lowest score: ", lowest_score)

highest_score = max(student_scores)
print("highest score: ", highest_score)

average_score = sum(student_scores)/len(student_scores)
print(average_score)

print(sorted(student_scores, reverse = True))