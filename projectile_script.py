from projectile_module import radian_conversion, projectile_height
# importing the module and new functions we made
# using the new functions to calculate the height of a projectile

# testing the radian conversions function
radians = radian_conversion(103)
print(radians)
print(type(radians))
# the output is a float

# the below function uses the radian_conversions function within it
test = projectile_height(v=44, deg=80, x=0.5, y=1)
print(test)
print(type(test))
# the output is a float