# You have 8 slices of pizza and 3 friends
#Splitting Pizza Among Friends (Arithmetic + Modulus)
slices = 8
friends = 3

# Each friend gets equal slices
equal_share = slices // friends   # Division
remainder = slices % friends      # Modulus

print("Each friend gets:", equal_share, "slices")
print("Remaining slices:", remainder)
