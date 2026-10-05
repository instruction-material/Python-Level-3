"""Incomplete search experiment. Read README.md; references remain separate."""


def linear_search(list1, item):
    """Implement the original Boolean linear membership function."""
    raise NotImplementedError("Implement linear_search.")


def bin_search_iter(lst, item):
    """Implement Boolean membership on sorted input with index bounds."""
    raise NotImplementedError("Implement bin_search_iter.")


def bin_search_recur(lst, item):
    """Optional: retain and explain the original recursive slice-based version."""
    raise NotImplementedError("Implement bin_search_recur.")


def make_workload(size=2000, queries=50, seed=0):
    """Prepare the bounded seeded data and one shared query list before timing."""
    raise NotImplementedError("Implement make_workload.")


def compare_searches(nums, targets, repeats=3, clock=None):
    """Verify shared search results and return the documented measured-median rows."""
    raise NotImplementedError("Implement compare_searches.")


def main(size=2000, queries=50, repeats=3, seed=0):
    """Run a bounded experiment and report environment, boundaries and measured data."""
    raise NotImplementedError("Implement main.")


if __name__ == "__main__":
    print("Implement the five core tasks in README.md before running main(); recursion is optional.")
