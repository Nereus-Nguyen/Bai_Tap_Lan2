def ma_hoa_caesar (plaintext, shift):
    cipher_text = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            cipher_text += chr((ord(char) - shift_base + shift) % 26 +  shift_base)
        else:
            cipher_text += char
    return cipher_text
text = "Dai Hoc Cong Nghiep"
number = 18
zzz = ma_hoa_caesar(text, number)
print(f"ma hoa: {zzz}")