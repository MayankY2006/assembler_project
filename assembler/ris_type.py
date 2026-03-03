R_TYPE = {
    "add":  ("0000000", "000", "0110011"),
    "sub":  ("0100000", "000", "0110011"),
    "sll":  ("0000000", "001", "0110011"),
    "slt":  ("0000000", "010", "0110011"),
    "sltu": ("0000000", "011", "0110011"),
    "xor":  ("0000000", "100", "0110011"),
    "srl":  ("0000000", "101", "0110011"),
    "or":   ("0000000", "110", "0110011"),
    "and":  ("0000000", "111", "0110011"),
}

I_TYPE = {
    "addi":  ("000", "0010011"),
    "sltiu": ("011", "0010011"),
    "lw":    ("010", "0000011"),
    "jalr":  ("000", "1100111"),
}

S_TYPE = {
    "sw": ("010", "0100011"),
}

def encode_r_type(instr, rd, rs1, rs2, REGISTER_MAP):

    funct7, funct3, opcode = R_TYPE[instr]

    rd_binary  = REGISTER_MAP[rd]
    rs1_binary = REGISTER_MAP[rs1]
    rs2_binary = REGISTER_MAP[rs2]

    binary = funct7 + rs2_binary + rs1_binary + funct3 + rd_binary + opcode
    return binary

def encode_i_type(instr, rd, rs1, imm, REGISTER_MAP, to_signed_binary):

    funct3, opcode = I_TYPE[instr]

    rd_binary  = REGISTER_MAP[rd]
    rs1_binary = REGISTER_MAP[rs1]

    imm_binary = to_signed_binary(imm, 12)

    binary = imm_binary + rs1_binary + funct3 + rd_binary + opcode
    return binary


def encode_s_type(instr, rs2, rs1, imm, REGISTER_MAP, to_signed_binary):

    funct3, opcode = S_TYPE[instr]

    rs2_binary = REGISTER_MAP[rs2]
    rs1_binary = REGISTER_MAP[rs1]

    imm_binary = to_signed_binary(imm, 12)

    imm_high = imm_binary[:7]   # imm[11:5]
    imm_low  = imm_binary[7:]   # imm[4:0]

    binary = imm_high + rs2_binary + rs1_binary + funct3 + imm_low + opcode
    return binary


def encode_instruction(instr, operands, REGISTER_MAP, to_signed_binary):

    if instr in R_TYPE:
        rd, rs1, rs2 = operands
        return encode_r_type(instr, rd, rs1, rs2, REGISTER_MAP)

    elif instr in I_TYPE:
        if instr == "lw":
            rd, imm, rs1 = operands
        else:
            rd, rs1, imm = operands
        return encode_i_type(instr, rd, rs1, int(imm), REGISTER_MAP, to_signed_binary)

    elif instr in S_TYPE:
        rs2, imm, rs1 = operands
        return encode_s_type(instr, rs2, rs1, int(imm), REGISTER_MAP, to_signed_binary)

    else:
        raise ValueError("Unsupported instruction for R/I/S module")

