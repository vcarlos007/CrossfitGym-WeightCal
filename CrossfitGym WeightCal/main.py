def calculate_total_weight(bar_weight, right_plates, left_plates):
    total_weight = bar_weight + sum(right_plates) + sum(left_plates)
    return total_weight

def input_plates(side):
    plates = []
    while True:
        try:
            weight = float(input(f"Enter plate weight for {side} side (or 0 to finish): "))
            if weight == 0:
                break
            plates.append(weight)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return plates

def main():
    print("Weight Tracking for Barbell")

    # Bar selection
    while True:
        bar_choice = input("Select bar weight (35 or 45 lbs): ")
        if bar_choice in ['35', '45']:
            bar_weight = int(bar_choice)
            break
        else:
            print("Invalid choice. Please enter 35 or 45.")

    # Input plates for right side
    print("\nEnter plates for the right side:")
    right_plates = input_plates("right")

    # Input plates for left side
    print("\nEnter plates for the left side:")
    left_plates = input_plates("left")

    # Calculate and display total weight
    total_weight = calculate_total_weight(bar_weight, right_plates, left_plates)

    # Display results
    print(f"\nBar weight: {bar_weight} lbs")
    print(f"Right side plates: {right_plates}")
    print(f"Left side plates: {left_plates}")
    print(f"Total weight: {total_weight} lbs")

if __name__ == "__main__":
    main()