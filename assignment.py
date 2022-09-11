from caesar_cipher import Caesar

encrypted_message = "TYMXKTLMHKFVHFXLTVTEF"
result_arr = []

for i in range(26):
    result_arr.append((str(i).zfill(2), Caesar.shift_with_stats(encrypted_message, i), Caesar.shift(encrypted_message, i)))

result_arr.sort(key=lambda v: v[1], reverse=True)

for (key, propability, decoded) in result_arr:
    print(f"Key: {chr(int(key)+65)} | {propability:.6f} | {decoded}")
