def caesar(text, shift, encrypt = True):
  
  if not isinstance(shift, int):
    return "Shift must be an integer value."

  if shift < 1 or shift > 25:
    return "Shift must be an integer between 1 and 25"

  alphabet = "abcdefghijklmnopqrstuvwxyz"
  
  if not encrypt:
    shift = -shift
  shifted_alphabet = alphabet[shift:] + alphabet[0:shift]
  translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
  return text.translate(translation_table)

def encrypt(text, shift):
  return caesar(text, shift)
def decrypt(text, shift):
  return caesar(text, shift, False)

encrypted_text = encrypt("freeCodeCamp", 3)
print("Encrypted text:", encrypted_text)

encrypted_text_new = "Pbhentr vf sbhaq va hayvxryl cynprf."
decrypted_text = decrypt(encrypted_text_new, 13)
print("Decrypted text:", decrypted_text)