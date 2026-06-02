
users = []

for i in range(2):
    print(f"\nEnter information for User {i + 1}")

    name = input("Name: ")
    age = int(input("Age: "))
    height = float(input("Height (cm): "))

    user = {
        "name": name,
        "age": age,
        "height": height
    }

    users.append(user)

print("\nUser Information:")
for user in users:
    print(
        f"{user['name']} is {user['age']} years old and "
        f"{user['height']} cm tall."
    )

def calculate_total_height(user_list):
    total_height = 0

    for user in user_list:
        total_height += user["height"]

    return total_height

total_height = calculate_total_height(users)

print(f"\nThe total combined height of both users is {total_height} cm.")