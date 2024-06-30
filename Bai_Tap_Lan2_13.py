from unidecode import unidecode

def remove_accent (input_str):
    no_accents = unidecode(input_str)
    no_no_spaces = no_accents.replace(" ","")
    return no_no_spaces
input_string = "Dieu Vy"
processed_string = remove_accent(input_string)
print(processed_string)