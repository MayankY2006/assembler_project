import sys

# Member 4: import error checks
from error_handler import check_instruction, check_register


REGISTER_MAP = {
    "zero": "00000", "ra": "00001", "sp": "00010", "gp": "00011",
    "tp": "00100", "t0": "00101", "t1": "00110", "t2": "00111",
    "s0": "01000", "fp": "01000", "s1": "01001",
    "a0": "01010", "a1": "01011", "a2": "01100", "a3": "01101",
    "a4": "01110", "a5": "01111", "a6": "10000", "a7": "10001",
    "s2": "10010", "s3": "10011", "s4": "10100", "s5": "10101",
    "s6": "10110", "s7": "10111", "s8": "11000", "s9": "11001",
    "s10": "11010", "s11": "11011",
    "t3": "11100", "t4": "11101", "t5": "11110", "t6": "11111",
}


def to_signed_binary(value, bits):
    """
    Converts integer to signed binary of given bit width.
    """
    if value < 0:
        value = (1 << bits) + value

    binary = format(value, f'0{bits}b')

    # Truncate if overflow (Member 4 should check bounds)
    return binary[-bits:]


def read_assembly_file(filepath):
    """
    Reads assembly file and returns list of lines.
    """
    with open(filepath, 'r') as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def first_pass(lines):

#returns symbol_table(dictonary)
    pc = 0
    symbol_table = {}

    for line in lines:

        # Ignore empty lines
        if not line:
            continue

        # If label exists
        if ':' in line:
            label = line.split(':')[0].strip()
            symbol_table[label] = pc

            # If label-only line, don't increment PC
            if line.endswith(':'):
                continue

        # Every instruction increases PC by 4
        pc += 4

    return symbol_table



def second_pass(lines, symbol_table, encode_instruction):
# returns list of 32 bit binary strings

    pc = 0
    output_binary = []

    for line in lines:

        if not line:
            continue

        # Remove label if present
        if ':' in line:
            parts = line.split(':')
            if len(parts) > 1:
                line = parts[1].strip()
            else:
                continue

        if not line:
            continue

        # Basic parsing (Member 4 will improve validation)
        tokens = line.replace(',', ' ').replace('(', ' ').replace(')', ' ').split()

        instr = tokens[0]
        operands = tokens[1:]

        # Member 4 validation
        line_no = pc // 4 + 1
        check_instruction(instr, line_no)

        for op in operands:
            if op in REGISTER_MAP:
                check_register(op, line_no, REGISTER_MAP)

        binary = encode_instruction(instr, operands, REGISTER_MAP, to_signed_binary)

        output_binary.append(binary)

        pc += 4

    return output_binary



def write_output(filepath, binary_lines):
    """
    Writes binary instructions to output file.
    """
    with open(filepath, 'w') as f:
        for line in binary_lines:
            f.write(line + '\n')