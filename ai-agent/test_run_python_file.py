from functions.run_python_file import run_python_file


def main():
    # 1) Usage instructions
    result = run_python_file("calculator", "main.py")
    print(result)

    # 2) Run calculator with an expression (this will produce STDERR in the rendered JSON)
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result)

    # 3) Run calculator tests (will produce STDOUT and probably some STDERR)
    result = run_python_file("calculator", "tests.py")
    print(result)

    # 4) Outside working directory
    result = run_python_file("calculator", "../main.py")
    print(result)

    # 5) Nonexistent file
    result = run_python_file("calculator", "nonexistent.py")
    print(result)

    # 6) Not a Python file
    result = run_python_file("calculator", "lorem.txt")
    print(result)
if __name__ == "__main__":
    main()
