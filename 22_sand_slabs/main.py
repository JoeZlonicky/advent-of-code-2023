from sand_simulation import SandSimulation

INPUT_FILE_PATH = './inputs/puzzle.txt'


def main():
    sim = SandSimulation.from_file(INPUT_FILE_PATH)
    sim.simulate_falling()
    n = sim.count_safe_to_disintegrate()
    print(n)


if __name__ == '__main__':
    main()
