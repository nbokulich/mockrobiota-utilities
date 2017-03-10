#!/usr/bin/env python

# ----------------------------------------------------------------------------
# Copyright (c) 2016--, mockrobiota development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import click
from collections import defaultdict


def genus_slice(t):
    '''Slices off the deepest-level taxonomy label from semicolon-delimited
    taxonomy string and returns genus-level taxonomy string. This assumes that
    the input taxonomy string contains species-level label as the deepest
    taxonomic level and genus as second-deepest, but will still function
    appropriately if all taxonomy strings contain an even number of levels and
    the user understands what taxonomy level is second-deepest.
    '''
    return ';'.join(t.split(';')[:-1])


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
              'seqID   taxonomy\n'
              '0001    kingdom;phylum;class;order;family;genus;species')
@click.option('-e', '--exact', default=True,
              help='If true, perform exact match to species. If false, find '
              'all database identifiers that match at genus level.')
def main(infile, outfile, ref, exact):
    '''Generate database identifiers that match a list of expected taxonomies
    at species level (when exact==True). Expected taxonomies must be
    full-length taxonomy strings that match the given reference database, e.g.,
    should be generated using autoannotate.py.
    '''
    # parse input file
    infile.readline()
    source_taxa = [l.strip().split('\t')[0] for l in infile]

    ref_taxa = defaultdict(list)
    genera = defaultdict(list)
    # parse ref taxonomy
    for l in ref:
        i, t = l.strip().split('\t')
        ref_taxa[t].append(i)
        # store genus-level ref taxonomy for last-resort "near matching"
        if exact is not True:
            genera[genus_slice(t)].append(i)

    # Pull identifiers from ref_taxa and write out
    for t in source_taxa:
        if t in ref_taxa.keys():
            outfile.write('{0}\t{1}\n'.format(t, '\t'.join(ref_taxa[t])))
        # find genus-level matches if species match not found and exact==False
        elif exact is not True:
            g = genus_slice(t)
            if g in genera.keys():
                outfile.write('{0}\t{1}\n'.format(t, '\t'.join(genera[g])))


if __name__ == "__main__":
    main()
