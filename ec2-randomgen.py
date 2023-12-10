import uuid
import random
import string

def generate_unique_name(department):
    # Generate a random string of characters and numbers
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    # Generate a unique identifier using uuid
    unique_id = str(uuid.uuid4().hex)[:6]

    # Combine department name, random string, and unique identifier
    unique_name = f"{department}_{random_string}_{unique_id}"

    return unique_name

def main():
    try:
        num_instances = int(input("Enter the number of EC2 instances you want names for: "))
        department_name = input("Enter the name of your department: ")

        if num_instances <= 0:
            print("Please enter a valid number of instances.")
            return

        # Generate and print unique names for the specified number of instances
        for i in range(num_instances):
            unique_name = generate_unique_name(department_name)
            print(f"Instance {i+1}: {unique_name}")

    except ValueError:
        print("Please enter a valid number for the number of instances.")

if __name__ == "__main__":
    main()
