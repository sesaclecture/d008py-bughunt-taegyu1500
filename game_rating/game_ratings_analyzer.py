import sys
import csv


def normalize_path(path):
    return '/home/intel/Documents/py/d008py-bughunt-taegyu1500/game_rating/data/' + path


def is_valid_rating(r):
    return 0 <= r <= 10

def fixed_is_valid_rating(r):
    try:
        return 0 <= int(r) <= 10
    except:
        return False


def is_tie(games):
    games[0][1] == games[-1][1]


def fixed_is_tie(games):
    sorted_games = sorted(games, key=lambda x:x[1], reverse=True)
    return sorted_games[0][1] == sorted_games[-1][1]


def read_ratings(file_path):
    ratings = {}
    with open(file_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            title = row["title"]
            rating = int(row["rating"])
            
            if title in ratings:
                ratings[title].append(rating)
            else:
                ratings[title] = [rating]
    return ratings

def fixed_read_ratings(file_path):
    ratings = {}
    with open(file_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                title = row["title"]
                rating = int(row["rating"])
            except:
                print("잘못된 csv 파일입니다")
                return
            if(not is_valid_rating(rating)):
                continue
            
            if title in ratings:
                ratings[title].append(rating)
            else:
                ratings[title] = [rating]
    return ratings

# def fixed_read_ratings(file_path):
#     ratings = {}
#     with open(file_path) as f:
#         reader = csv.DictReader(f)
#         for row in reader:
#             title = row["title"]
#             try:
#                 rating = int(row["rating"])
#             except:
#                 if row["rating"].isdecimal:
#                     rating = int(round(float(row["rating"])))
#                 else:
#                     raise TypeError
#             if title in ratings:
#                 ratings[title].append(rating)
#             else:
#                 ratings[title] = [rating]
#     return ratings

# def compare(str1, str2):
#     return str1.upper().lower().replace(" ", "") == str2.upper().lower().replace(" ", "")

# def fixed_read_ratings(file_path):
#     ratings = {}
#     with open(file_path) as f:
#         reader = csv.DictReader(f)
#         for row in reader:
#             title = row["title"].upper().lower().replace(" ", "")
#             rating = int(row["rating"])
#             if title in ratings:
#                 ratings[title].append(rating)
#             else:
#                 ratings[title] = [rating]
#     return ratings


def generate_report(ratings, top_n):
    averages = {}

    for title, scores in ratings.items():
        averages[title] = sum(scores) / len(scores)

    sorted_games = sorted(averages.items(), key=lambda x: x[1], reverse=True)
    
    if is_tie(sorted_games):
        print("All games have the same average rating.")

    for i in range(top_n):
        title, avg = sorted_games[i]
        print(f"{i+1}. {title} - Avg Rating: {avg:.2f}")
    
    if is_tie(sorted_games):
        print("All games have the same average rating.")
    return True

def fixed_generate_report(ratings, top_n):
    if len(ratings) == 0:
        return False
    averages = {}

    for title, scores in ratings.items():
        if len(scores) == 0:
            print("잘못된 입력입니다") 
            return
        averages[title] = sum(scores) / len(scores)

    sorted_games = sorted(averages.items(), key=lambda x: x[1], reverse=True)
    if fixed_is_tie(sorted_games):
        print("All games have the same average rating.")
        return False
    edited_top_n = top_n if top_n < len(sorted_games) else len(sorted_games)
    for i in range(edited_top_n):
        title, avg = sorted_games[i]
        print(f"{i+1}. {title} - Avg Rating: {avg:.2f}")

    # if is_tie(sorted_games):
    #     print("All games have the same average rating.")
        
    return True


def main(path):
    file_path = normalize_path(path)
    ratings = read_ratings(file_path)
    generate_report(ratings, 10)


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print(f"사용법: {sys.argv[0]} <입력 CSV 파일>")
            exit()
        else:
            main(sys.argv[1])
    except IndexError:
        print("리스트 숫자가 잘못되었습니다")

# if __name__ == "__main__":
#     try:
#         main(sys.argv[1])
#     except IndexError:
#         print(f"사용법: {argv[0]} <입력 CSV 파일>")       

def main_logic(argv):
    try:
        main(argv[1])
    except IndexError:
        print(f"사용법: {argv[0]} <입력 CSV 파일>")
        
def fixed_main_logic(argv):
    try:
        if len(argv) < 2:
            print(f"사용법: {argv[0]} <입력 CSV 파일>")
            return None
        else:
            main(argv[1])
    except IndexError:
        print("리스트 숫자가 잘못되었습니다")

# if __name__ == "__main__":