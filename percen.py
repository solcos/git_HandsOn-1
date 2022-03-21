import sys, re
from argparse import ArgumentParser 

parser = ArgumentParser(description = 'computes the percentage of each nucleotide from a DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence") 

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)
    
args = parser.parse_args()
args.seq = args.seq.upper()  
if re.search('^[ACGTU]+$', args.seq):
    a= args.seq.count("U") #this counts the number of U inside the sequence
    b= args.seq.count("A") #this counts the number of A inside the sequence
    c= args.seq.count("C") #this counts the number of C inside the sequence
    d= args.seq.count("T") #this counts the number of T inside the sequence
    e= args.seq.count("G") #this counts the number of G inside the sequence
    #the percentages of each ones.
    print ("Percentage of U's in sequence:", (a / len(args.seq)) * 100)
    print ("Percentage of A's in sequence:", (b / len(args.seq)) * 100)
    print ("Percentage of C's in sequence:", (c / len(args.seq)) * 100)
    print ("Percentage of T's in sequence:", (d / len(args.seq)) * 100)
    print ("Percentage of G's in sequence:", (e / len(args.seq)) * 100)
else:
    print ('The sequence is not DNA nor RNA')


