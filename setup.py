#!/usr/bin/env python

# ----------------------------------------------------------------------------
# Copyright (c) 2014--, mockrobiota development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import find_packages, setup

setup(
    name='mockrobiota-utilities',
    version='0.0.0-dev',
    license='BSD-3-Clause',
    packages=find_packages(),
    install_requires=['click'],
    author="Nicholas Bokulich",
    author_email="nbokulich@gmail.com",
    description="Mockrobiota Utilities",
    url="https://github.com/nbokulich/mockrobiota-utilities",
    entry_points={
        'console_scripts':
        ['autoannotate=mockrobiota_utilities.autoannotate:main',
         'database_identifiers='
         'mockrobiota_utilities.database_identifiers:main',
         'annotate_sequence_ids='
         'mockrobiota_utilities.autoannotate:annotate_sequence_ids']
        }

)
