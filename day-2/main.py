from pathlib import Path

values = {
    "A": 1,
    "X": 1,
    "B": 2,
    "Y": 2,
    "C": 3,
    "Z": 3,
}

ans1 = 0
ans2 = 0

def _calculate_score(opponent: str, yours: str) -> None:
    global ans1, ans2
    
    ans1 += yours
    ans1 += (yours - opponent + 1) % 3 * 3

    ans2 += (opponent + yours) % 3 + 1
    ans2 += (yours - 1) * 3

def main(input: str):
    games = input.split('\n')
    for game in games:
        opponent, me = list(map(lambda x: values.get(x), game.split(' ')))
        _calculate_score(opponent, me)

if __name__ == "__main__":
    current_path = Path(__file__).parent.absolute()
    with open(current_path / "input.txt", "r") as f:
        input = f.read()
    main(input)

    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")
