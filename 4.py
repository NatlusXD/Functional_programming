n = int(input("Number of cards: "))

expected_sum = n * (n + 1) // 2

actual_sum = 0

for i in range(n - 1):
    card_number = int(input("Number of remaining cards: "))
    actual_sum += card_number

missing_card = expected_sum - actual_sum

print("Lost card: ", missing_card)
