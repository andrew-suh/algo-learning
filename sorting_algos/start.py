# Import all algo files
import bubblesort

# Get problems to sort
def get_problems(file_location):
    with open(file_location) as r:
        diff_lines = r.read().splitlines()

    return diff_lines

# Get the function from the imported file and run with list of strings
def solve_problem(problems, algo_name):
    getattr(bubblesort, algo_name)(problems)

if __name__ == "__main__":
    list_of_problems = get_problems("../problem_bank/sorting.txt")
    solve_problem(list_of_problems, "bubblesort")
