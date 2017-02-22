#!/usr/bin/env python

# ----------------------------------------------------------------------------
# Copyright (c) 2016--, mockrobiota development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import click

@click.command()
@click.option('-i', '--infile', type=click.File('r'), required=True,
              help='tab-separated list of taxonomy strings in first column. '
              'Assumes that a header line exists, i.e., will skip first line '
              'of file.')
@click.option('-o', '--outfile', type=click.File('w'), required=True,
              help='destination in which to write database identifiers file')
@click.option('-r', '--ref', type=click.File('r'), required=True,
              help='tab-separated list of semicolon-delimited taxonomy '
              'strings associated with reference sequences. In format:\n'
              'seqID   taxonom\n'
              '0001    kingdom;phylum;class;order;family;genus;species')
def main(infile, outfile, ref):
    '''Generate database identifiers that match a list of expected taxonomies at
    species level. Expected taxonomies must be full-length taxonomy strings
    that match the given reference database, e.g., should be generated
    using autoannotate.py.
    '''
    # parse input file
    infile.readline()
    source_taxa = [l.strip().split('\t')[0] for l in infile]

    ref_taxa = dict()
    # parse ref taxonomy
    for l in ref:
        i, t = l.strip().split('\t')
        if t not in ref_taxa.keys():
            ref_taxa[t] = [i]
        else:
            ref_taxa[t].append(i)

    # Pull identifiers from ref_taxa and write out
    for t in source_taxa:
        if t in ref_taxa.keys():
            outfile.write('{0}\t{1}\n'.format(t, '\t'.join(ref_taxa[t])))


if __name__ == "__main__":
    main(sys.argv[1:])
