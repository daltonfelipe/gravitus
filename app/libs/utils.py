from app.libs.constants import Constants


def newton_gravity_law(mass1, mass2, distance):
    return Constants.G*(mass1*mass2)/(distance**2)
