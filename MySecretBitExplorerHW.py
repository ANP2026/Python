secret_code = 13
access_key = 9


def bits(number, width=4):
    return format(number & ((1 << width) - 1), f"0{width}b")

print("Secret Code:", secret_code, "Bin:", bits(secret_code))
print("Access Key:", access_key, "Bin:", bits(access_key))
print("Secret Code Bin:", bits(secret_code))
print("Access Key Bin:", bits(access_key))

and_result = secret_code & access_key
or_result = secret_code | access_key

print("AND:", and_result, "Bin:", bits(and_result))
print("OR:", or_result, "Bin:", bits(or_result))
print("AND: 1 where both bits are 1.")
print("OR: 1 where at least one bit is 1.")


not_result = (~secret_code) & 0b1111
xor_result = secret_code ^ access_key

print("NOT (4-bit):", not_result, "Bin:", bits(not_result))
print("XOR:", xor_result, "Bin:", bits(xor_result))
print("XOR: 1 when bits differ.")



left_shift = secret_code << 1
right_shift = secret_code >> 1


print("Left shift:", left_shift, "Bin:", bits(left_shift, 5))
print("Right shift:", right_shift, "Bin:", bits(right_shift))
print("Shifts: left/right move bits accordingly.")



xor_check = secret_code ^ 1

print("Secret Code XOR 1:", xor_check)

if xor_check == secret_code - 1:
    print("Secret Code is odd.")
else:
    print("Secret Code is even.")

bit_count = secret_code.bit_count()
print("1 bits in Secret Code:", bit_count)


print("Secret Code:", secret_code, "Bin:", bits(secret_code))
print("Access Key:", access_key, "Bin:", bits(access_key))
print("AND:", and_result)
print("OR:", or_result)
print("NOT (4-bit):", not_result)
print("XOR:", xor_result)
print("Left Shift:", left_shift)
print("Right Shift:", right_shift)
print("1 Bits Count:", bit_count)
