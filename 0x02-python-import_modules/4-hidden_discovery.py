#!/usr/bin/python3
import dis

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as file:
        bytecode = file.read()

    instructions = dis.get_instructions(bytecode)
    names = set()

    for instruction in instructions:
        if instruction.opname == "LOAD_CONST" and isinstance(instruction.argval, str):
            name = instruction.argval
            if not name.startswith("__"):
                names.add(name)

    sorted_names = sorted(names)
    for name in sorted_names:
        print(name)
