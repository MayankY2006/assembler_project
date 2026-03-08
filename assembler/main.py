import sys

from core import read_assembly_file, first_pass, second_pass, write_output
from error_handler import check_virtual_halt


def main():
    """
    Main assembler execution flow.
    """

    try:

        # Check command line arguments
        if len(sys.argv) != 3:
            print("Usage: python assembler.py input.asm output.txt")
            sys.exit(1)

        input_file = sys.argv[1]
        output_file = sys.argv[2]

        # Read assembly file
        lines = read_assembly_file(input_file)

        # Check virtual halt instruction
        check_virtual_halt(lines)

        # First pass → build symbol table
        symbol_table = first_pass(lines)

        # Import encoding dispatcher
        from ris_type import encode_instruction

        # Second pass → generate binary
        binary_output = second_pass(lines, symbol_table, encode_instruction)

        # Write output file
        write_output(output_file, binary_output)

        print("Assembly successful!")

    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
