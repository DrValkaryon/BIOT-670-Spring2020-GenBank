
import os
from Bio import SeqIO
from Bio import Entrez
import CircularView
import LinearView


def Main():  
    CircularView.rec_it(open("working.gb"))
    LinearView.rec_itL(open("working.gb"))
    pass



def GB_Hunter (accession, email):
    
    Entrez.email = email  # Always tell NCBI who you are
    filename = accession + ".gb"
    if not os.path.isfile(filename):
        # Downloading...
        net_handle = Entrez.efetch(
            db="nucleotide", id=accession, rettype="gb", retmode="text"
        )
        out_handle = open(filename, "w+")
        out_handle.write(net_handle.read())
        out_handle.close()
        net_handle.close()
        print("Saved")

    print("Parsing...")
    record = SeqIO.read(filename, "genbank")
    record.features = [f for f in record.features if f.type not in ["gene", "source", "mRNA"]]
    SeqIO.write(record,"working.gb","genbank")
    try:
        f = open('record.txt', 'w')
        f.write(str(record))
        f.close()
        f = open('sequence.txt', 'w')
        seq1 = str(record.seq)
        f.write(seq1)
        f.close()
    except:
        print("This ain't it, chief.")
    

    return 
    
def export (fName):
    try:
        fName1 = fName + ".gb"
        record = SeqIO.read("working.gb", "genbank")
        SeqIO.write(record, fName1,"genbank")
    except Exception as e:
        print(e)
def seq_ann(seq):
    print("Placeholder")
    #annotate by sequence using a combination of regex and biopython's reference library for DNA sequences.

def seq_bp(start,end):
    print("placeholder")
    #take a pair of bp or a set of them, comma-delimited, to map features to the referenced sequence.

if __name__ == "__Main__":
   # stuff only to run when not called via 'import' here
   Main()
