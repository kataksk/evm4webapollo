import sys

evm_gff3_input = sys.argv[1]

def feature_converter(feature, type):
    if type == 'mRNA':
        feature_split = feature.split(';')
        output = feature_split[0]
        return output
    elif type == 'CDS':
        return feature

with open(evm_gff3_input, 'r') as f:
    for line in f:
        if line == '\n':
            continue
        else:
            line = line.rstrip('\n').split('\t')
            if line[2] == 'mRNA' or line[2] == 'CDS':
                output = '\t'.join(line[0:8]) + '\t' + str(feature_converter(line[8], line[2]))
                print(output)