#must conclude with period
string = '   . .             .'
counter = 0
list = []

for character in string:
  if character == ' ':
    counter += 1
  if character == '.':
    list.append(counter)
    counter = 0

message = ''

for element in list:
  if element == 1:
    message += 'A'
  if element == 2:
    message += 'B'
  if element == 3:
    message += 'C'
  if element == 4:
    message += 'D'
  if element == 5:
    message += 'E'
  if element == 6:
    message += 'F'
  if element == 7:
    message += 'G'
  if element == 8:
    message += 'H'
  if element == 9:
    message += 'I'
  if element == 10:
    message += 'J'
  if element == 11:
    message += 'K'
  if element == 12:
    message += 'L'
  if element == 13:
    message += 'M'
  if element == 14:
    message += 'N'
  if element == 15:
    message += '0'
  if element == 16:
    message += 'P'
  if element == 17:
    message += 'Q'
  if element == 18:
    message += 'R'
  if element == 19:
    message += 'S'
  if element == 20:
    message += 'T'
  if element == 21:
    message += 'U'
  if element == 22:
    message += 'V'
  if element == 23:
    message += 'W'
  if element == 24:
    message += 'X'
  if element == 25:
    message += 'Y'
  if element == 26:
    message += 'Z'
  if element == 27:
    message += ' '

print(message)
