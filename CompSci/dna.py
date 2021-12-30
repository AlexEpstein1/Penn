def nuc_counts(seq):

	list1 = [seq.count("A"),seq.count("C"),seq.count("G"),seq.count("T")]
	return "Counts: " + str(list1)

def total_helper(seq,mass_list):
	total = round(seq.count("A")*mass_list[0] + seq.count("C") * mass_list[1] + seq.count("G") * mass_list[2] + seq.count("T") * mass_list[3]+ seq.count("-") * mass_list[4],1) 
	return total

def mass(seq, mass_list):
	total = total_helper(seq,mass_list)
	list2 = [round(seq.count("A")*mass_list[0] / total *100,1), round(seq.count("C")*mass_list[1] / total *100,1),round(seq.count("G")*mass_list[2]/ total *100,1),round(seq.count("T")*mass_list[3] / total *100,1)]
	return "Mass %: " + str(list2) + " of " + str(total)

def codons(seq):
	seq = seq.replace("-", "")
	return [seq[i] + seq[i + 1] + seq[i + 2] for i in range(len(seq)) if i % 3 == 0]

def protein(seq,mass_list):
	total = total_helper(seq, mass_list)
	if seq[0:3] == "ATG" and seq[-3:] == "TAA" or seq[-3:] == "TAG" or seq[-3:] == "TGA" and int(len(seq)) >= 13 and (round(seq.count("C")*mass_list[1] / total *100,1) + round(seq.count("G")*mass_list[2]/ total *100,1)) >= 30:
		return "Protein: Yes"
	return "Protein: No"


def dna(tup):
	A = 135.128
	C = 111.103
	G = 151.128
	T = 125.107
	dash = 100
	mass_list = [A,C,G,T,dash] 
	dna = tup[1].upper()
	print("Region name: " + tup[0])
	print("Nucleotides: " + dna)
	print(nuc_counts(dna))
	print(mass(dna, mass_list))
	print("Codons: " + str(codons(dna)))
	print(protein(dna, mass_list))



def main():
	name = input("DNA Name: ")
	seq = input("DNA Sequence: ")
	tup = (name, seq)
	dna(tup)

	# seq1 = ('cure for cancer protein', 'ATGCCACTATGGTAG')
	# # seq2 = ('captain picard hair growth protein', 'ATgCCAACATGgATGCCcGATAtGGATTgA')
	# # seq3 = ('bogus protein', 'CCATt-AATgATCa-CAGTt')

main()
