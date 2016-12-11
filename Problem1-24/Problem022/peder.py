
def calc_name_scores(fname):
    with open(fname) as f:
        names = f.read().replace("\"", "").split(",")
    names_alphabetical = sorted(names)

    score = 0
    for index, name in enumerate(names_alphabetical):
        alph_score = sum(map(lambda letter: (ord(letter) - ord('A') + 1), name))
        score += alph_score * (index + 1)
    
    return score

if __name__ == "__main__":
    score = calc_name_scores("input.txt")
    print(score)
