# Create Candidate

candidates = []

# Print candidates at the beginning

print('Candidates at the beginning:', candidates)

# Create employees

employees = ['Francis', 'Ann', 'Jacob', 'Claire']

# Print employees at the beginning

print('Employees at the beginning:', employees)

# Add new candidates
new_candidates = ['Bruno','Agnes']
candidates.append('Bruno')
candidates.append('Agnes')


# Print new candidates

print(f'New names added to candidates: {candidates}')

# Insert name

employees.insert(1, candidates[0])

# Print the employees list after entering a new name

print('New names added to employees: ',employees)