# message template
message = "Hello {}! Nice to meet you"
print(message)

#use template
formatted_message = message.format("Juan")
print(formatted_message)

# Use Template again
new_message = message.format("Jesse")
print(new_message)