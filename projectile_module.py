from math import pi, tan, cos
# importing math module and the methods we'll need to use in our functions

# first make a function to convert degrees to radians
# we'll use this in the projectile function
# the return is a float, so we used the float function to convert the answer to a float
def radian_conversion(deg):
    """
    This function converts degrees into radians\n
    Input is a float\n
    Return is a float\n
    :param deg: float
    :return: float
    """
    radians = float(deg * (pi/180))
    return radians

# projectile function to calculate the height of a projectile
# the parameters are
# g is acceleration due to gravity m/s
# v is the initial velocity m/s
# deg is elevation angle in degrees - it will be converted into radians using the function above
# x is the horizontal distance travelled m
# y is the height of the barrel m

# the default value of g is given as 9.81 (acceleration due to gravity)
# any parameters that follow * to the right must be passed in by their name, not their position
# the return is a float, so we used the float function to convert the answer to a float
def projectile_height(*, g=9.81, v, deg, x, y):
    """
This function calculates the height of a projectile\n
g is acceleration due to gravity m/s\n
v is the initial velocity m/s\n
deg is the elevation angle in degrees\n
x is the horizontal distance travelled m\n
y is the height of the barrel m\n
    :param g: float
    :param v: float
    :param deg: float
    :param x: float
    :param y: float
    :return: float
    """
    answer = float((y + (x * (tan(radian_conversion(deg))))) - ((g * x ** 2) / (2 * (v * cos(radian_conversion(deg))) ** 2)))
    return answer

# define main
def main():
    test = projectile_height(v=44, deg=80, x=0.5, y=1)
    print(test)

if __name__ == '__main__':
    main()