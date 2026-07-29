def caesar(text, shift):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  shifted_alphabet = alphabet[shift:] + alphabet[0:shift]
  translation_table = str.maketrans(alphabet, shifted_alphabet)
  return text.translate(translation_table)
  
encrypted_text = caesar("freeCodeCamp", 3)
print(encrypted_text)