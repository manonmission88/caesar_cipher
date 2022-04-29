
import sys
def printing_message(output):
    final = ""
    line = ""
    counter = 0
    for character in output:
        final += character 
        if len(final) == 5 and counter < 9:
            final += " "
            line += final
            counter += 1
            final = ""
        elif len(final) == 5 and counter == 9:
            line += final +"\n"
            counter = 0
            final = ""
    return(line + final + "\n")
#encryptions 
def caesar_encrypt(message, key):
    upper_message = message.upper()
    alphabets = ""
    for char in upper_message:
      if char.isalpha():
        alphabets += char
    encoded_text = ""
    for element in alphabets:
      ascii = ord(element)
      final_ascii = ascii + key
      if final_ascii > ord("Z"):
        final = (final_ascii - ord("Z")) % 26
        if final == 0:
          final = 26
        final_ascii = final + 64
      encoded_text += chr(final_ascii)
    result = printing_message(encoded_text)
    return result

for line in sys.stdin:
    output = caesar_encrypt(line.strip(), int(sys.argv[1]))
    sys.stdout.write(output)