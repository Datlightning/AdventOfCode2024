from heapq import heappop, heappush
def display(path, l, w):
    for y in range(w):
        string =""
        for x in range(l):
            if (y,x) in path:
                string += "#"
            else:
                string += "."
        print(string)
def eval_instructions(A, registers, instructions,p2 = False):
    
    if not p2:
        A = registers["A"]
    
    B = registers["B"]
    C = registers["C"]
    i = 0
    output = []
    output_length = 0
    while True:
            if i >= len(instructions):
                break
            if p2 and output_length > 0 and instructions[output_length-1] != output[output_length - 1]:
                output_length -= 1
                break
            v = instructions[i]
            literal_operand = instructions[i+1]
            combo_operand = instructions[i+1] 
            i += 2
            if combo_operand <= 3:
                pass
            elif combo_operand == 4:
                combo_operand = A
            elif combo_operand == 5:
                combo_operand = B
            elif combo_operand == 6:
                combo_operand = C
            if v == 0:
                num = A
                A = num//(2**combo_operand)
            elif v == 1:
                B = literal_operand ^ B
            elif v == 2:
                B = combo_operand % 8
            elif v == 3:
                if A != 0:
                    i = literal_operand
            elif v == 4:
                B = C ^ B
            elif v == 5:
                if p2:
                    output.append(combo_operand % 8)
                    output_length += 1
                else:
                    output.append(str(combo_operand % 8))
            elif v == 6:
                num = A
                B = num//(2**combo_operand)
            elif v == 7:
                num = A
                C = num//(2**combo_operand)
    if p2:
        # print(output[0:output_length])
        return output[0:output_length]
    return ",".join(output)

def solve():
    sum1 = 0  
    sum2 = 0
    
    registers = dict() 
    with open("day17/input.txt", "r") as file:
        registers, instructions =   file.read().split("\n\n")
        A,B,C = registers.split("\n")
        registers = {
            "A":0,
            "B":0,
            "C":0
        }
        registers["A"] = int(A.split(":")[1].strip())
        registers["B"] = int(B.split(":")[1].strip())
        registers["C"] = int(C.split(":")[1].strip())
        instructions = list(map(int, instructions.split(":")[1].strip().split(",")))
    sum2 = 0
    A = 0
    sum1 = eval_instructions(registers["A"], registers, instructions)
    print(sum1)
    sum3 = eval_instructions(53898069715858, registers, instructions, p2 = True)
    print(sum3) 
    # while output != instructions:
    #     registers["A"] = int(A.split(":")[1].strip())
    #     registers["B"] = int(B.split(":")[1].strip())
    #     registers["C"] = int(C.split(":")[1].strip())
    #     i = 0
    #     v = 0
    #     output = []
    #     output_length = 0
    #     if number == -1:
    #         pass
    #     else:
    #         registers["A"] = number
    Ast = 0
    best = 0
    while True:
        Ast += 1
        A = Ast * 8**9 + 0o723125622
        out = eval_instructions(A, registers, instructions, p2 = True)
        if out == instructions:
            sum2 = A
            break
        elif len(out) > best:
            best = len(out) 
            print(A, oct(A), best, len(instructions))
    print(A, oct(A), best, len(instructions))

    return f"Sum 1: {sum1}\nSum 2: {sum2}"



# B = A % 8 
# B = B ^ 6
# C = A // 2**B
# B = C ^ B
# B = B ^ 7

# A = A // 8
# print(B % 8)
# if A == 0:
#     win
# else:
    # cry