



def traduction(seq, code):
    proteine=""
    i=0
    codon=seq[i:i+3]
    while (i<len(seq) and len(codon)==3): # On verrifie si la longueur du codon est de 3 pour chercher dans le code génétique
        acide_amine=code_genetique[codon]

        # print(codon, code_genetique[codon]) # On teste le fonctionnement
        
        proteine+=acide_amine
        i+=3
        codon=seq[i:i+3]
    return proteine




# Définition des variables à utiliser dans la fonction 
code_genetique = {"GCT" :"A","GCC":"A","GCA":"A","GCG":"A","TTA":"L","TTG":"L","CTT":"L","CTC":"L","CTA":"L","CTG":"L","CGT":"R","CGC":"R","CGA":"R","CGG":"R","AGA":"R","AGG":"R","AAA":"K","AAG":"K","AAT":"N","AAC":"N","ATG":"M","GAT":"D","GAC":"D","TTT":"F","TTC":"F","TGT":"C","TGC":"C","CCT":"P","CCC":"P","CCA":"P","CCG":"P","CAA":"Q","CAG":"Q","TCT":"S","TCC":"S","TCA":"S","TCG":"S","AGT":"S","AGC":"S","GAA":"E","GAG":"E","ACT":"T","ACC":"T","ACA":"T","ACG":"T","GGT":"G","GGC":"G","GGA":"G","GGG":"G","TGG":"W","CAT":"H","CAC":"H","TAT":"Y","TAC":"Y","ATT":"I","ATC":"I","ATA":"I","GTT":"V","GTC":"V","GTA":"V","GTG":"V","TAG":"*","TGA":"*","TAA":"*"}
sequence="ATGACCATGATTACGAATTCCCGGGGATCCGTCGACCTGCAGC"

# On appele la fonction traduction
resultat=traduction(sequence, code_genetique)

# On affiche le résultat
print(resultat)
# On doit obtenir 'MTMITNSRGSVDLQ'