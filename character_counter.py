# simple game that takes a sentence as an input and outputs the number of time each character appears as a dictionary

message = input('Input any sentence you want: ')

count = {}
for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
