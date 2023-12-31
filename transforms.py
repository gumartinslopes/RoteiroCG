import math

def translation(x, y, x_factor, y_factor):
    new_x = x + x_factor
    new_y = y+ y_factor
    return new_x, new_y

def rotation(x, y, theta):
    radians = math.radians(theta)
    new_x = x * math.cos(radians) - y * math.sin(radians)
    new_y = x * math.sin(radians) + y * math.cos(radians)
    return new_x, new_y

def mirroring(x, y,center, axis):
    if axis == "both":
        return -x + 2*center[0], -y + 2*center[1]
    elif axis == "x":
        return x, -y + 2 * center[1]
    else:
        return -x + 2*center[0], y 
    
def scaling(x, y, factor):
    return x * factor, y * factor

def shear(x, y, factor, axis, center):
    if axis == "x":
        return x + factor * y - center[0]//2, y
    else:
        return x, y + factor * x - center[1]//2 #+ center[1]//2