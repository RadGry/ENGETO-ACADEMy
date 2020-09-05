# Save name
name = str(input('Please enter you name:'))

# Print name

print("Saving '",name,"' into the name...")
print("Saving" + " '" + name + "' " + "into name... ")

# Save surname

surname = str(input('Please enter your surname:'))
# Print surname

print("Saving '",surname,"' into the surname...")
print("Saving" + " '" + surname + "' " + "into surname... ")

# Create and print variable full_name

full_name = name + ' ' + surname

print(full_name)

# Create and print variable name_length

name_length = len(full_name)
print('The length of full name is:', name_length)

# Print bounded variable full_name

print('='*int(name_length))
print(full_name)
print('='*int(name_length))
