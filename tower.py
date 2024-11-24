def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Move top n-1 disks from source to auxiliary using destination as a buffer
    tower_of_hanoi(n - 1, source, destination, auxiliary)

    # Move the nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")

    # Move the n-1 disks from auxiliary to destination using source as a buffer
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# Run the function
if __name__ == "__main__":
    num_disks = int(input("Enter the number of disks: "))
    print("\nSteps to solve Tower of Hanoi:")
    tower_of_hanoi(num_disks, 'Source', 'Auxiliary', 'Destination')
