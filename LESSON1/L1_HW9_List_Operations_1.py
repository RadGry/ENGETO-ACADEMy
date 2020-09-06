# # Create Candidate
#
# candidates = []
#
# # Print candidates at the beginning
#
# print('Candidates at the beginning:', str(candidates))
#
# # Create employees
#
# employees = ['Francis', 'Ann', 'Jacob', 'Claire']
#
# # Print employees at the beginning
#
# print('Employees at the beginning:', str(employees))
#
# # Add new candidates
# new_candidates = ['Bruno','Agnes']
# candidates.append('Bruno')
# candidates.append('Agnes')
#
#
# # Print new candidates
#
# print(f'New names added to candidates: {candidates}')
#
# # Insert name
#
# employees.insert(1, candidates[0])
#
# # Print the employees list after entering a new name
#
# print('New names added to employees: ',str(employees))

# Results from previous task
candidates = ['Bruno', 'Agnes']
employees = ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire']


# Delete names from candidates

candidates.remove('Bruno')

# Print remaining candidates

print('Bruno removed from candidates:', str(candidates))

# Repeat element

candidates = candidates*3

# Print repeating element in list candidates

print('Repetition of Agnes in the candidate list: ', str(candidates))

# Join lists

employees.extend(candidates)

# Print joined lists

print('Joined candidates and employees: ',str(employees))

# Index 2

print('At index 2 is: ', employees[2])

# Find out last index and assign it to variable

last_index = str(len(employees) - 1)

# Last index

print('At index', str(last_index), 'is: ', employees[-1])