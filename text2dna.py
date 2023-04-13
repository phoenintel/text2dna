#ANSI colors codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
END = '\033[0m'

#title screen
print(YELLOW + "\n\n\n\n\n****************************\n**********TEXT2DNA**********\n****************************\n\n" + END)
print(RED + "\nThis work is licensed under a CC BY-NC-SA 4.0 License. Read it here: https://creativecommons.org/licenses/by-nc-sa/4.0/\n" + END + GREEN + "source code: https://github.com/phoenintel/text2dna\n" + END)
# ask user for text to convert to DNA sequence or DNA to text
conversion_type = input(BLUE + "Enter '1' to convert text to DNA or '2' to convert DNA to text: " + END)

if conversion_type == '1':
    #text to dna

    # ask user for text to convert to DNA sequence
    original_str = input(BLUE + "Please enter the text value to convert: " + END)

    # convert text to binary
    binary_str = ''.join(format(x, '08b') for x in bytearray(original_str, 'utf-8'))

    binary_list = [binary_str[i: i+2] for i in range(0, len(binary_str), 2)]

    # binary values to nucleotide sequence values
    # 00 = "A" (adenine)
    # 01 = "G" (guanine)
    # 10 = "C" (cytosine)
    # 11 = "T" (thymine)

    # DNA encoding
    DNA_encoding = {
        "00": "A",
        "01": "G",
        "10": "C",
        "11": "T"
    }

    DNA_list = []
    for num in binary_list:
        for key in list(DNA_encoding.keys()):
            if num == key:
                DNA_list.append(DNA_encoding.get(key))

    DNA_str = "".join(DNA_list)

    # convert DNA sequence to RNA sequence
    RNA_str = DNA_str.replace("T", "U")

    # nucleotide to amino acid translation
    codon_table = {
        "ATA":"I", "ATC":"I", "ATT":"I", "ATG":"M",
        "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
        "AAC":"N", "AAT":"N", "AAA":"K", "AAG":"K",
        "AGC":"S", "AGT":"S", "AGA":"R", "AGG":"R",
        "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
        "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
        "CAC":"H", "CAT":"H", "CAA":"Q", "CAG":"Q",
        "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R",
        "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
        "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
        "GAC":"D", "GAT":"D", "GAA":"E", "GAG":"E",
        "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G",
        "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S",
        "TTC":"F", "TTT":"F", "TTA":"L", "TTG":"L",
        "TAC":"Y", "TAT":"Y", "TAA":"*", "TAG":"*",
        "TGC":"C", "TGT":"C", "TGA":"*", "TGG":"W",
    }

    codon_list = [RNA_str[i:i+3] for i in range(0, len(RNA_str), 3)]

    amino_acid_list = []
    for codon in codon_list:
        amino_acid_list.append(codon_table.get(codon, "X"))

    amino_acid_str = "".join(amino_acid_list)

    # print all results
    print(YELLOW + "\n--- RESULTS ---\n" + END)

    print(BLUE + "\nOriginal text :" + END + "\n" + RED + original_str + END + "\n")
    print(BLUE + "Text to binary conversion :" + END + "\n" + RED + binary_str + END + "\n")

    print(BLUE + "DNA sequence :" + END + "\n" + GREEN + DNA_str + END + "\n")

    # add spaces every three nucleotides
    DNA_spaced_str = ' '.join([DNA_str[i:i+3] for i in range(0, len(DNA_str), 3)])

    print(BLUE + "DNA nucleotides sequence :" + END + "\n" + YELLOW + DNA_spaced_str + END + "\n")

    print(BLUE + "RNA sequence :" + END + "\n" + GREEN + RNA_str + END + "\n")

    # add spaces every three RNA values
    RNA_spaced_str = ' '.join([RNA_str[i:i+3] for i in range(0, len(RNA_str), 3)])

    print(BLUE + "RNA spaced sequence :" + "\n" + YELLOW + RNA_spaced_str + END + "\n")

    print(BLUE + "amino acid sequence :" + END + "\n" + GREEN + amino_acid_str + END + RED + "\n(x represents indeterminate amino acids) \n" + END)

    input(BLUE + "Press Enter to exit..." + END)


    print(YELLOW + "\n\n\n\n\n****************************\n**********TEXT2DNA**********\n****************************\n\n" + END + GREEN + "source code: https://github.com/phoenintel/text2dna" + END + YELLOW + "\n\nThank you for using this program!"+ END)
else:
    #dna to text
    dna_seq = input(BLUE + "Please enter the DNA sequence to convert: " + END)

    # nucleotide sequence to binary conversion
    binary_str = ""
    for nucleotide in dna_seq:
        if nucleotide == "A":
            binary_str += "00"
        elif nucleotide == "G":
            binary_str += "01"
        elif nucleotide == "C":
            binary_str += "10"
        elif nucleotide == "T":
            binary_str += "11"
        else:
            print(RED + "Invalid DNA sequence. Please try again." + END)
            exit()

    # binary to text conversion
    text_str = ""
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        text_str += chr(int(byte, 2))

    # print result
    print(BLUE + "Text converted from DNA sequence:" + END + "\n" + GREEN + text_str + END + "\n")

    input(BLUE + "Press Enter to exit..." + END)

    print(YELLOW + "\n\n\n\n\n****************************\n**********TEXT2DNA**********\n****************************\n\n" + END + GREEN + "source code: https://github.com/phoenintel/text2dna" + END + YELLOW + "\n\nThank you for using this program!"+ END)
