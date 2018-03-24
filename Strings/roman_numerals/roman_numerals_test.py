""" Generating a number in range [1, 3999], converting it to Roman numeral,
generating number from Roman numeral and comparing it with original number.
"""
import random
from integer_to_roman import Solution as SolIntRom
from roman_to_integer import Solution as SolRomInt


sol_int_rom = SolIntRom()
sol_rom_int = SolRomInt()


while True:
    # generate random number from 1 to 3999
    original_number = random.randrange(1, 4000)

    # convert number to roman numeral
    roman_number = sol_int_rom.int_to_roman(original_number)

    # convert roman numeral back to integer
    converted_number = sol_rom_int.roman_to_int(roman_number)

    # compare with original number
    if converted_number == original_number:
        print("OK")
        print(f"original number: {original_number}")
        print(f"roman number: {roman_number}")
        print()
    else:
        print("Conversion results are different.")
        print(f"original number: {original_number}")
        print(f"roman number: {roman_number}")
        print(f"converted number: {converted_number}")
        break
