import sys
def DNA_strand(dna):
    complement_map = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    complementary_letters = [complement_map[a] for a in dna]
    result="".join(complementary_letters)
    sys.stdout.write(result + '\n')
    return result    
letter=input('Enter : ').upper()
DNA_strand(letter)