from pulse_module import PulseModule


def parse_input_file(file_path) -> dict[str, PulseModule]:
    with open(file_path) as f:
        lines = [line.strip() for line in f]

    modules = {}
    for line in lines:
        if not line:
            continue

        name, module = PulseModule.from_line(line)
        modules[name] = module

    for module_name in modules:
        outputs = modules[module_name].outputs
        for output_name in outputs:
            if output_name not in modules:
                continue
            
            modules[output_name].add_input_connection(module_name)

    return modules
