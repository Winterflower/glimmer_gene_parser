#program design: give the program a list of correctly formatted files for all genes 
# program performs operations for each file and outputs them to another file




#python script for analyzing manually adjusted exon ranges

from Bio import SeqIO

column_file=open('removed_output.txt','r')

per_row=[]
gene_dictionary={}

for line in column_file:
    per_row.append(line.strip().split())

print per_row[2][0][0]

#get the number of genes and print them in an array 

gene_numbers=[]

for element in per_row:
	gene_numbers.append(element[0][0])
print '###################################'


#make a method to find the unique numbers in a list

def unique_filter(array):
	unique_list=[]
	for element in array:
		if element not in unique_list:
			unique_list.append(element)
	return unique_list

unique_gene_numbers=unique_filter(gene_numbers)
print unique_gene_numbers
#confirmed that unique_filter works as expected 

#make a dictionary with the unique_gene_numbers as keys 

for gene_number in unique_gene_numbers:
	gene_dictionary[gene_number]=[]

for element in per_row:
	gene=element[0]
	gene_dictionary[gene].append(element[4:6])

#confirm that the gene dictionary stores the gene positions for each individual gene
print gene_dictionary['6']


#import the haggis genome as a single string using Biopython 

haggis_sequence=SeqIO.read('haggis.fna','fasta')
haggis_string=str(haggis_sequence.seq)

#test to see that this was successful 

print haggis_string[0:10]

#try to get the positions of the first gene

#make a dictionary to store he concatenated positions of the genes

final_genes={} 

#get the positions of the first gene 
for element in gene_dictionary.keys():
#for every gene make an entry into the final genes dictionary
	final_genes[element]=[]
	for position_list in gene_dictionary[element]:
		final_genes[element].append(haggis_string[int(position_list[0])-1:int(position_list[1])])
	print "######################"
		

print gene_dictionary.keys()
#print final_genes['1']		

#copy final_genes

final_concatenated_genes=dict.copy(final_genes)

for element in final_concatenated_genes.keys():
	final_concatenated_genes[element]="".join(final_concatenated_genes[element])
print final_concatenated_genes['1']


#now we have all of the final exons in the file 


#now the task is to print all of the genes into a single file separated by fasta headers 

fasta_header=">gene1_hypsibius \n"
gene_1_haggis = open('gene_1_haggis', 'w')
gene_1_haggis.write(fasta_header)

gene_1_haggis.write("ACACACACTTGGCCGGCGCGCGCG")


#dynamically set local variables in python
#next we should copy the dictionary and concatenate the exons in the file 
print "#######################################"
print per_row[2][4:6]
#source http://stackoverflow.com/questions/15585011/reading-columns-as-lists


