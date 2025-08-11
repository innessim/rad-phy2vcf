from __future__ import print_function

from phylip import Phylip
from popmap import Popmap

import collections
import operator

class VCF():
    """Class for working with VCF files"""

    def __init__(self, phy, popmap, outfile):
        lookup = {
            'Y': 'C,T', 'R': 'A,G', 'W': 'A,T', 'S': 'G,C',
            'K': 'T,G', 'M': 'C,A', 'A': 'A,A', 'T': 'T,T',
            'C': 'C,C', 'G': 'G,G'
        }

        with open(outfile, 'w') as f:
            # Write VCF headers
            f.write("##fileformat=VCFv4.1\n")
            f.write("##fileDate=20170603\n")
            f.write("##source=pyRAD.v.3.0.66\n")
            f.write("##reference=common_allele_at_each_locus\n")
            f.write("##INFO=<ID=NS,Number=1,Type=Integer,Description=\"Number of Samples With Data\">\n")
            f.write("##INFO=<ID=DP,Number=1,Type=Integer,Description=\"Total Depth\">\n")
            f.write("##INFO=<ID=AF,Number=A,Type=Float,Description=\"Allele Frequency\">\n")
            f.write("##INFO=<ID=AA,Number=1,Type=String,Description=\"Ancestral Allele\">\n")
            f.write("##FORMAT=<ID=GT,Number=1,Type=String,Description=\"Genotype\">\n")
            f.write("##FORMAT=<ID=GQ,Number=1,Type=Integer,Description=\"Genotype Quality\">\n")
            f.write("##FORMAT=<ID=DP,Number=1,Type=Integer,Description=\"Read Depth\">\n")
            f.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT")

            od = collections.OrderedDict(sorted(phy.alignment.items()))
            for key in od.keys():
                f.write("\t" + key)
            f.write("\n")

            # Continuous genome coordinates
            chrom = 1
            poscount = 1

            for i in range(0, phy.alignLength):
                d = collections.defaultdict(int)
                NS = 0  # number of samples with non-missing data

                # Count alleles for this site
                for ind, seq in od.items():
                    base = seq[i].upper()
                    if base in lookup:
                        NS += 1
                        alleles = lookup[base].split(',')
                        for a in alleles:
                            d[a] += 1

                # Keep all sites, including invariant ones
                sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
                temp = collections.defaultdict(int)
                nuclist = []
                counter = 0
                for key, value in sorted_d:
                    nuclist.append(key)
                    temp[key] = counter
                    counter += 1

                if len(nuclist) == 0:
                    # all samples missing at this site
                    poscount += 1
                    continue

                ref = nuclist.pop(0)
                alt = ",".join(nuclist) if nuclist else "."

                # Write VCF line
                f.write(f"{chrom}\t{poscount}\t.\t{ref}\t{alt}\t20\tPASS\tNS={NS};DP=15\tGT")

                for ind, seq in od.items():
                    base = seq[i].upper()
                    f.write("\t")
                    if base not in lookup:
                        f.write("./.")
                    else:
                        a1, a2 = lookup[base].split(',')
                        g1 = str(temp.get(a1, '.'))
                        g2 = str(temp.get(a2, '.'))
                        if '.' in (g1, g2):
                            f.write("./.")
                        else:
                            f.write(f"{g1}|{g2}")

                f.write("\n")
                poscount += 1

