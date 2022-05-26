def transcribe(dna_strand):

    if dna_strand == "G":
        return "C"

    elif dna_strand == "C":
        return "G"

    elif dna_strand == "T":
        return "A"
        
    elif dna_strand == "A":
        return "U"

    return transcribe(dna_strand[0]) + transcribe(dna_strand[1:])
