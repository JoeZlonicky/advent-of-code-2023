from pulse_module import PulseModule, PulseModuleType


def parse_input_file(file_path) -> dict[str, PulseModule]:
    with open(file_path) as f:
        lines = [line.strip() for line in f]

    modules = {}
    for line in lines:
        if not line:
            continue

        name, module = PulseModule.from_line(line)
        modules[name] = module

    dummy_modules = {}

    for module_name in modules:
        outputs = modules[module_name].outputs
        for output_name in outputs:
            if output_name not in modules:
                if output_name not in dummy_modules:
                    dummy_modules[output_name] = PulseModule(PulseModuleType.DUMMY, [])
                dummy_modules[output_name].add_input_connection(module_name)
                continue

            modules[output_name].add_input_connection(module_name)

    for module_name in dummy_modules:
        modules[module_name] = dummy_modules[module_name]

    return modules
