def pyramid(rows):
    """Centered pyramid: row i shows 1..i..1."""
    lines = []
    for i in range(1, rows + 1):
        line = " " * (rows - i)
        for n in range(1, i + 1):
            line += str(n)
        for n in range(i - 1, 0, -1):
            line += str(n)
        lines.append(line)
    return lines


def right_triangle(rows):
    """Row i shows 1..i."""
    lines = []
    for i in range(1, rows + 1):
        line = ""
        for n in range(1, i + 1):
            line += str(n)
        lines.append(line)
    return lines


def inverted_triangle(rows):
    """Row i shows 1..(rows-i+1)."""
    lines = []
    for i in range(rows, 0, -1):
        line = ""
        for n in range(1, i + 1):
            line += str(n)
        lines.append(line)
    return lines


def repeat_triangle(rows):
    """Row i shows the number i repeated i times."""
    lines = []
    for i in range(1, rows + 1):
        line = ""
        for _ in range(i):
            line += str(i)
        lines.append(line)
    return lines


def floyd_triangle(rows):
    """Consecutive numbers 1, 2, 3, ... filling a triangle."""
    lines = []
    counter = 1
    for i in range(1, rows + 1):
        nums = []
        for _ in range(i):
            nums.append(str(counter))
            counter += 1
        lines.append(" ".join(nums))
    return lines


PATTERNS = {
    "1": ("Number pyramid", pyramid),
    "2": ("Right triangle (1..i)", right_triangle),
    "3": ("Inverted triangle", inverted_triangle),
    "4": ("Repeated-number triangle", repeat_triangle),
    "5": ("Floyd's triangle", floyd_triangle),
}


def verify(choice, rows, lines):
    """Check the generated pattern against the rules of the chosen type."""
    assert len(lines) == rows, "wrong number of rows"
    for idx, line in enumerate(lines, start=1):
        body = line.strip()
        if choice == "1":
            assert len(body) == 2 * idx - 1, f"row {idx}: wrong length"
            assert body == body[::-1], f"row {idx}: not symmetric"
            assert body[idx - 1] == str(idx), f"row {idx}: wrong peak"
            assert len(line) - len(line.lstrip()) == rows - idx, f"row {idx}: bad indent"
        elif choice == "2":
            assert body == "".join(str(n) for n in range(1, idx + 1)), f"row {idx}: wrong"
        elif choice == "3":
            k = rows - idx + 1
            assert body == "".join(str(n) for n in range(1, k + 1)), f"row {idx}: wrong"
        elif choice == "4":
            assert body == str(idx) * idx, f"row {idx}: wrong"
        elif choice == "5":
            assert len(body.split()) == idx, f"row {idx}: wrong count"
    if choice == "5":
        flat = [int(x) for line in lines for x in line.split()]
        assert flat == list(range(1, len(flat) + 1)), "numbers not consecutive"
    print("Verification passed.")


def show_menu():
    print("\n===== Number Pattern Menu =====")
    for key, (name, _) in PATTERNS.items():
        print(f"  {key}. {name}")
    print("  0. Exit")


def main():
    while True:
        show_menu()
        choice = input("Select a pattern (0-5): ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        if choice not in PATTERNS:
            print("Invalid choice, please try again.")
            continue

        try:
            rows = int(input("Number of rows: ").strip())
            if rows < 1:
                raise ValueError
        except ValueError:
            print("Please enter a positive whole number.")
            continue

        name, func = PATTERNS[choice]
        lines = func(rows)

        print(f"\n{name} ({rows} rows):\n")
        for line in lines:
            print(line)
        print()
        verify(choice, rows, lines)

        again = input("\nChange pattern? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
