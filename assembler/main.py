import sys
from core import read_assembly_file, first_pass, second_pass, write_output

def main():
    """
    Main assembler execution flow.
    """

    if len(sys.argv) != 3:
        print("Usage: python assembler.py input.asm output.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    lines = read_assembly_file(input_file)

    symbol_table = first_pass(lines)

    # Import encoding dispatcher here (after team integration)
    from ris_type import encode_instruction

    binary_output = second_pass(lines, symbol_table, encode_instruction)

    write_output(output_file, binary_output)

    print("Assembly successful!")


if __name__ == "__main__":
    main()