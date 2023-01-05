from verilib import *

output_file = 'output.txt'

check_for_existing_solution_key()
assert_linecount(output_file, 12329)
assert_lines_match_regex(output_file, r'\d+ \d+')
assert_lines_sorted_by(output_file, lambda x: x.split(' ')[0])
assert_file_contents_hash_to(output_file, 'bbdc82b3189fe1d4e466e124830d55d6928fd51739cc7fa590e168e85cff1fde20a48d2d8528b2bd5ea3b8f5dad0d2ce8636cca6a3000088711bc659d985df50')
compute_code_for_file(output_file)
