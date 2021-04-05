
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
    except:
        print("This ain't it, chief.")
    

    return 
    
def export (fName):
    
    SeqIO.write("working.gb", fName,"genbank")

if __name__ == "__Main__":
   # stuff only to run when not called via 'import' here
   Main()
