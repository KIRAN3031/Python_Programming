def calculate_notes(amount):
    denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    notes_count = {}
    total_notes = 0
    for denom in denominations:
        if amount >= denom:
            count = amount // denom
            notes_count[denom] = count
            total_notes += count
            amount %= denom
    return notes_count, total_notes

amount = int(input("Enter the amount: "))
notes, total = calculate_notes(amount)
print("Notes breakdown:")
for denom, count in notes.items():
    if count > 0:
        print(f"{denom} rupees notes: {count}")
print(f"Total number of notes: {total}")
