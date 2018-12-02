def load_input(day):
    with open(f'./input/input_{day:02}.txt') as f:
        input_data = f.read().splitlines()
    return input_data