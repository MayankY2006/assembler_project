VALID_INSTRUCTIONS={
    "add","sub","sll","slt","sltu","xor","srl","or","and",
    "addi","lw","jalr","sltiu",
    "sw",
    "beq","bne","blt","bge","bltu","bgeu",
    "lui","auipc",
    "jal"
}

def check_instruction(instr, line_no):
    if instr not in VALID_INSTRUCTIONS:
        raise Exception(
           f"Error at line {line_no}: Invalid instruction '{instr}'"
        )

def check_register(reg, line_no, REGISTER_MAP):
    if reg not in REGISTER_MAP:
        raise Exception(
            f"Error at line {line_no}: Invalid register '{reg}'"
        )

def check_immediate(value, bits, line_no):
    try:
        value=int(value)
    except:
        raise Exception(
            f"Error at line {line_no}: Immediate '{value}' is not a valid integer"
        )
    min_val=-(1 << (bits - 1))
    max_val=(1 << (bits - 1)) - 1
    if value < min_val or value > max_val:
        raise Exception(
            f"Error at line {line_no}: Immediate {value} out of range for {bits}-bit signed"
        )

def check_virtual_halt(lines):
    halt_found=False
    for line in lines:
        cleaned=line.replace(" ", "").strip()
        if cleaned=="beqzero,zero,0":
            halt_found=True
    if not halt_found:
        raise Exception("Error: Missing Virtual Halt instruction")
    for line in reversed(lines):
        cleaned = line.replace(" ", "").strip()
        if cleaned == "":
            continue
        if cleaned != "beqzero,zero,0":
            raise Exception("Error: Virtual Halt must be the last instruction")
        break
