import os
import sys


def slugify(problem_name):
    return "-".join(problem_name.lower().split())


def create_problem(topic, problem_name, approaches):
    problem_folder = slugify(problem_name)
    problem_path = os.path.join(topic, problem_folder)

    os.makedirs(problem_path, exist_ok=True)

    approach_folders = ["brute", "optimal"]

    if approaches == 3:
        approach_folders.insert(1, "optimized-brute")

    for folder in approach_folders:
        folder_path = os.path.join(problem_path, folder)
        os.makedirs(folder_path, exist_ok=True)

        with open(os.path.join(folder_path, "README.md"), "w"):
            pass

        with open(os.path.join(folder_path, "solution.cpp"), "w"):
            pass

    with open(os.path.join(problem_path, "README.md"), "w"):
        pass

    print(f"Successfully created '{problem_name}'.")


def main():
    if len(sys.argv) != 4:
        print("Usage:")
        print("python create_problem_directory.py <topic> <problem_name> <approaches>")
        sys.exit(1)

    topic = sys.argv[1]
    problem_name = sys.argv[2]

    try:
        approaches = int(sys.argv[3])

        if approaches not in (2, 3):
            raise ValueError

    except ValueError:
        print("Error: <approaches> must be either 2 or 3.")
        sys.exit(1)

    create_problem(topic, problem_name, approaches)


if __name__ == "__main__":
    main()