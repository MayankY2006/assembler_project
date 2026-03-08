import sys
from core import read_assembly_file, first_pass, second_pass, write_output
from error_handler import check_virtual_halt

def main():

    try:
        if len(sys.argv) != 3:
            print("Usage: python assembler.py input.asm output.txt")
            sys.exit(1)
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        lines = read_assembly_file(input_file)
        check_virtual_halt(lines)
        symbol_table = first_pass(lines)
        from ris_type import encode_instruction
        binary_output = second_pass(lines, symbol_table, encode_instruction)
        write_output(output_file, binary_output)
        print("Assembly successful!")

    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
