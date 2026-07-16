import os

from create_problem_directory import slugify, create_problem

def test_slugify():
    assert slugify("Two Sum") == "two-sum"
    assert (
        slugify("Best Time to Buy and Sell Stock") == "best-time-to-buy-and-sell-stock"
    )

def test_create_problem_with_two_approaches(tmp_path):
    os.chdir(tmp_path)

    create_problem("arrays", "Kadane", 2)

    assert os.path.isdir("arrays/kadane")

    assert os.path.isdir("arrays/kadane/brute")
    assert os.path.isdir("arrays/kadane/optimal")

    assert not os.path.exists("arrays/kadane/optimized-brute")

def test_create_problem_with_three_approaches(tmp_path):
    os.chdir(tmp_path)

    create_problem("arrays", "three sum", 3)

    assert os.path.isdir("arrays/three-sum")

    assert os.path.isdir("arrays/three-sum/brute")
    assert os.path.isdir("arrays/three-sum/optimized-brute")
    assert os.path.isdir("arrays/three-sum/optimal")