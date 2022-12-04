from pathlib import Path

def part1(input: str):
    return max([sum(map(int, elf.split('\n'))) for elf in input.split('\n\n')])

def part2(input: str):
    return sum(sorted([sum(map(int, elf.split('\n'))) for elf in input.split('\n\n')])[-3:])

if __name__ == "__main__":
    current_path = Path(__file__).parent.absolute()
    with open(current_path / "input.txt", "r") as f:
        input = f.read()
    print(part1(input))
    print(part2(input))
