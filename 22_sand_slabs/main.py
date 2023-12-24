from sand_simulation import SandSimulation

INPUT_FILE_PATH = './inputs/puzzle.txt'


def main():
    sim = SandSimulation.from_file(INPUT_FILE_PATH)
    sim.simulate_falling()

    # Part 1
    n_safe_to_disintegrate = sim.calc_safe_to_disintegrate()
    print(f'(Part 1) # of boxes that are safe to disintegrate: {n_safe_to_disintegrate}')

    # Part 2
    n_affected_by_unsafe = sim.sum_affected_for_each_block_disintegrated()
    print(f'(Part 2) Sum of affected boxes for each block disintegrated: {n_affected_by_unsafe}')


if __name__ == '__main__':
    main()
