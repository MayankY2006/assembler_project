# List of all valid instructions supported by the assembler
VALID_INSTRUCTIONS = {
    "add","sub","sll","slt","sltu","xor","srl","or","and",
    "addi","lw","jalr","sltiu",
    "sw",
    "beq","bne","blt","bge","bltu","bgeu",
    "lui","auipc",
    "jal"
}


# Check if instruction is valid
def check_instruction(instr, line_no):

    if instr not in VALID_INSTRUCTIONS:
        raise Exception(
            f"Error at line {line_no}: Invalid instruction '{instr}'"
        )


# Check if register name exists in REGISTER_MAP
def check_register(reg, line_no, REGISTER_MAP):

    if reg not in REGISTER_MAP:
        raise Exception(
            f"Error at line {line_no}: Invalid register '{reg}'"
        )


# Check if immediate value fits within signed bit range
def check_immediate(value, bits, line_no):

    try:
        value = int(value)
    except:
        raise Exception(
            f"Error at line {line_no}: Immediate '{value}' is not a valid integer"
        )

    min_val = -(1 << (bits - 1))
    max_val = (1 << (bits - 1)) - 1

    if value < min_val or value > max_val:
        raise Exception(
            f"Error at line {line_no}: Immediate {value} out of range for {bits}-bit signed"
        )


# Check if virtual halt instruction exists and is last line
def check_virtual_halt(lines):

    halt = "beqzero,zero,0"

    cleaned_lines = []

    for line in lines:

        # remove spaces
        l = line.replace(" ", "").strip()

        # ignore empty lines
        if l == "":
            continue

        cleaned_lines.append(l)

    # Ensure halt instruction exists
    if halt not in cleaned_lines:
        raise Exception("Error: Missing Virtual Halt instruction")

    # Ensure halt is last instruction
    if cleaned_lines[-1] != halt:
        raise Exception("Error: Virtual Halt must be the last instruction")
