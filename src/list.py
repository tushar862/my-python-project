# Initialize a list with a fixed size of 100 (filled with None initially)
candidate_names = [None] * 100

# Function to add a name to the list
def add_candidate_name(name):
    for i in range(len(candidate_names)):
        if candidate_names[i] is None:  # Find the first empty slot
            candidate_names[i] = name
            print(f"Name '{name}' added at position {i}.")
            return
    print("The list is full. Cannot add more names.")

# Accept the full name of the candidate
full_name = input("Enter the full name of the candidate: ")

# Add the name to the list
add_candidate_name(full_name)

# Print the list to confirm (excluding None values)
print("Candidate names list:", [name for name in candidate_names if name is not None])