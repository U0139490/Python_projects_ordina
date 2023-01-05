from verilib import *

output_file = 'output.txt'

check_for_existing_solution_key()
assert_linecount(output_file, 991)
assert_lines_match_regex(output_file, r'.* (Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)')
assert_file_contents_hash_to(output_file, '39ab452d9ccfd510dd9e5c83a8c8dd3b1322e8cbdfac478995441248c53cffd2e6345671f886829a03d14ee569c3ac09a3c13c6fda9959e86e05c39997738e6c')
compute_code_for_file(output_file)
