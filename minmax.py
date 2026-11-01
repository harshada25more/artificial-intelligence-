
coins = [8, 15, 3, 7, 12, 15, 4, 8, 10]

ai = 0
human = 0

def minimax(coins):
    if len(coins) == 0:
        return 0

    left = coins[0] - minimax(coins[1:])
    right = coins[-1] - minimax(coins[:-1])

    return max(left, right)


while coins:

    # AI Turn
    left = coins[0] - minimax(coins[1:])
    right = coins[-1] - minimax(coins[:-1])

    if left >= right:
        ai += coins.pop(0)
    else:
        ai += coins.pop()

    print("AI Score:", ai)

    if not coins:
        break

    # Human Turn
    print("Remaining coins:", coins)
    choice = input("Choose L or R: ").upper()

    if choice == 'L':
        human += coins.pop(0)
    elif choice == 'R':
        human += coins.pop()
    else:
        print("Invalid choice!")
        continue

    print("Human Score:", human)


print("\nAI Score:", ai)
print("Human Score:", human)

if ai > human:
    print("AI Wins!")
elif human > ai:
    print("Human Wins!")
else:
    print("Draw!")
