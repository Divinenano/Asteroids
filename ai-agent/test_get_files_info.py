from functions.get_files_info import get_files_info


def main():
    # 1. current directory
    print("Result for current directory:")
    print(get_files_info("calculator", "."))

    # 2. 'pkg' directory
    print("Result for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))

    # 3. '/bin' directory
    print("Result for '/bin' directory:")
    print(get_files_info("calculator", "/bin"))

    # 4. '../' directory
    print("Result for '../' directory:")
    print(get_files_info("calculator", "../"))


if __name__ == "__main__":
    main()
