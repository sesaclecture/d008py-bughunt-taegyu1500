# def is_valid_rating(r):
#     return 0 <= r <= 10

# is_valid_rating("2") # Error 상황, str <-> int 비교
from game_ratings_analyzer import *
# def test_is_valid_rating():
#     assert True == is_valid_rating("2")
    
# def test_fixed_is_valid_rating():
#     assert True == fixed_is_valid_rating("2")    
#print(fixed_is_valid_rating("2")) # True
# def test_generate_report():
#     assert True == generate_report({}, 10)
# def test_generate_report2():
#     assert True == generate_report({"game_1" : [10], "game_2": [5]}, 10)
    
# def test_fixed_generate_report():
#     assert False == fixed_generate_report({}, 10)

# def test_fixed_generate_report2():
#     assert True == fixed_generate_report({"game_1" : [10], "game_2": [5]}, 10)
    
# def test_is_tie():
#     assert True == is_tie([('game_1', 10), ('game_2', 5), ('game_3', 5), ('game_4', 10)])

# def test_fixed_is_tie():
#     assert False == fixed_is_tie([('game_1', 10), ('game_2', 5), ('game_3', 5), ('game_4', 10)])
    
# def test_main_error():
#     assert IndexError == main_logic(['main'])

# def test_fixed_main_error():
#     assert None == fixed_main_logic(['main'])

# def test_read():
#     assert 1 == len(read_ratings(normalize_path('sameName.csv')))
    
# def test_fixed_read():
#     assert 1 == len(fixed_read_ratings(normalize_path('sameName.csv')))

# def test_read():
#     assert TypeError == read_ratings(normalize_path('decimal.csv'))

# def test_fixed_read():
#     assert dict == type(fixed_read_ratings(normalize_path('decimal.csv')))

# def test_generate():
#     try:
#         generate_report({'Empty Game': []}, 1)
#         assert True
#     except ZeroDivisionError:
#         assert False

# def test_fixed_generate():
#     try:
#         fixed_generate_report({'Empty Game': []}, 1)
#         assert True
#     except ZeroDivisionError:
#         assert False


def test_wrong_file():
        assert 7 == len(read_ratings(normalize_path('sameScore.csv')))
def test_fixed_wrong_file():
        assert 7 == len(fixed_read_ratings(normalize_path('sameScore.csv')))
        