import os


def gen_summary(reviewer, filename, folder_name):
    folder = f"{folder_name}/{reviewer}"
    file = open(filename, "w")
    file.write("[")
    for artifact in os.listdir(folder):
        basename = artifact.split(".")[0]
        #file.write(f"\"{basename}\" = import \"{folder}/{artifact}\",")
        file.write(f"import \"{folder}/{artifact}\",")
    file.write("]")
    file.close()
    return 0

def main():
    reviewers = [d for d in os.listdir("artifacts") if os.path.isdir(f"artifacts/{d}")]
    data = {}

    for reviewer in reviewers:
        filename = f"{reviewer}.ncl"
        gen_summary(reviewer, filename, "artifacts")

    return 0


if __name__ == "__main__":
    main()
