# python program to take in input from users and put unique words from the input in a list

user_input = []
print("Enter a paragraph narrating your trip to Nigeria: \n")
user = input()
list_input = user.split()

# Loop through the words in the user's input
for word in list_input:
    if word not in user_input:
        user_input.append(word)

print(user_input)
