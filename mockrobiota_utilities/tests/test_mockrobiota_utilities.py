#!/usr/bin/env python

# ----------------------------------------------------------------------------
# Copyright (c) 2016--, mockrobiota development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import click
import tempfile
from click.testing import CliRunner
from filecmp import cmp
from unittest import TestCase, main
from mockrobiota_utilities import database_identifiers, autoannotate


class MockrobiotaUtilitiesTests(TestCase):

    @classmethod
    def setUpClass(self):
        self.source_taxa = './data/taxonomy.tsv'
        self.identifiers_exact = './data/database-identifiers-exact.tsv'
        self.identifiers_notexact = './data/database-identifiers-notexact.tsv'
        self.ref_taxa = './data/99_otu_ref_taxonomy.tsv'

    def test_database_identifiers_exact(self):
        with tempfile.NamedTemporaryFile() as output:
            db_id.main(
                self.source_taxa, output.name, self.ref_taxa, exact=True)
            self.assertTrue(cmp(self.identifiers_exact, output.name))

    def test_database_identifiers_notexact(self):
        with tempfile.NamedTemporaryFile() as output:
            database_identifiers.main(
                self.source_taxa, output.name, self.ref_taxa, exact=False)
            self.assertTrue(cmp(self.identifiers_notexact, output.name))


if __name__ == "__main__":
    main()
