# Branch instruction definitions (B-Type)
BRANCH_TYPE = {
    "beq":  ("000", "1100011"),
    "bne":  ("001", "1100011"),
    "blt":  ("100", "1100011"),
    "bge":  ("101", "1100011"),
    "bltu": ("110", "1100011"),
    "bgeu": ("111", "1100011"),
}

# Jump instruction definitions (J-Type)
J_TYPE = {
    "jal": "1101111"
}


def encode_branch(instr, rs1, rs2, imm, REGISTER_MAP, to_signed_binary):

    funct3, opcode = BRANCH_TYPE[instr]

    rs1_binary = REGISTER_MAP[rs1]
    rs2_binary = REGISTER_MAP[rs2]

    imm_binary = to_signed_binary(imm, 13)

    # Split immediate according to B-type format
    imm_12   = imm_binary[0]       # bit 12
    imm_10_5 = imm_binary[2:8]     # bits 10-5
    imm_4_1  = imm_binary[8:12]    # bits 4-1
    imm_11   = imm_binary[1]       # bit 11

    binary = (
        imm_12 +
        imm_10_5 +
        rs2_binary +
        rs1_binary +
        funct3 +
        imm_4_1 +
        imm_11 +
        opcode
    )

    return binary


def encode_jal(rd, imm, REGISTER_MAP, to_signed_binary):

    opcode = J_TYPE["jal"]

    rd_binary = REGISTER_MAP[rd]

    imm_binary = to_signed_binary(imm, 21)

    # Split immediate according to J-type format
    imm_20    = imm_binary[0]
    imm_10_1  = imm_binary[10:20]
    imm_11    = imm_binary[9]
    imm_19_12 = imm_binary[1:9]

    binary = (
        imm_20 +
        imm_10_1 +
        imm_11 +
        imm_19_12 +
        rd_binary +
        opcode
    )

    return binary
