#!/usr/bin/env python3
import os
import sys
try:
    import myokit
    import myokit.formats.axon as axon
except ImportError:
    print('This script requires Myokit to run ($ pip install myokit).')
    sys.exit(1)

if len(sys.argv) != 2:
    print('Syntax: csv2atf.py <csv_file_name>')
    sys.exit(1)

csv_file_name = sys.argv[1]
atf_file_name = os.path.splitext(csv_file_name)[0] + '.atf'
axon.save_atf(myokit.DataLog.load_csv(csv_file_name), atf_file_name)
