players = ['charles', 'martin', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[2:])
print(players[-3:])
print("\n==================1=================")
players = ['charles', 'martin', 'michael', 'florence', 'eli']
print(f'Here are my three players on my team: ')
for player in players[:3]:
    print(player.title())
