"""A simple checker for functions in wonderland.py."""

import checker_generic

FILENAME = 'wonderland.py'
PYTA_CONFIG = 'pyta/a2_pyta.txt'
TARGET_LEN = 79
SEP = '='

print(''.center(TARGET_LEN, SEP))
print(' Start: checking coding style '.center(TARGET_LEN, SEP))
checker_generic.run_pyta(FILENAME, PYTA_CONFIG)
print(' End checking coding style '.center(TARGET_LEN, SEP))

print('\nScroll up to see ALL RESULTS:')
print('  - checking coding style')
print('  - checking type contract\n')
