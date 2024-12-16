"""
DMath is a class that expands complex numbers functions
implemented in cmath c module.
"""
import cmath, math

class DMath:

    roots: list[float]
    n: int
    z: complex

    def __init__(self, z):
        """
        Initializes z as complex number in an instance attribute.-
        if z is in polar format then it converts z into binomial format.
        Also, n and roots instance variables takes default values.
        :param z: the complex number
        """
        if type(z) == tuple:
            z = self.binomial(z[0], z[1])
        self.z = z
        self.n = 0
        self.roots = []

    def n_roots(self, n):
        """
        It calculates the n number of roots of a z complex number.
        It illustrates the The Moivre theorem.
        :param n: the number of roots
        :return: a tuple of roots
        """
        if type(n) != int:
            n = int(n)
        if n == 0:
            raise ValueError('Missing n as number of roots')
        
        self.n = abs(n)
        polar = self.polar()
        fi = polar[1]
        k = 0
        while k < n:
            zeta = (fi + 2 * k * self.pi()) / self.n
            self.roots.append(zeta)
            k += 1
        return tuple(self.roots)

    def format_roots(self, degrees=False):
        """
        It formats the founded roots
        :param degrees: By default is False
        :return: a tuple of angles
        """
        if degrees:
            t = tuple((math.degrees(r) for r in self.roots))
        else:
            t = tuple(self.roots)
        return t

    def n(self):
        """
        Returns the n number of roots
        """
        return self.n

    def polar(self):
        """
        if z is in binomial format then it converts z into polar format.
        :return: a tuple with ro and fi in polar format
        """
        if type(self.z) == complex:
            return cmath.polar(self.z)
        return self.z

    @staticmethod
    def binomial(mod, ang):
        """
        if module and angle are set then returns the binomial format of a polar complex number
        :param mod: module of a complex polar
        :param ang: angle of a complex polar
        :return: the complex in binomial format
        """
        if mod and ang:
            return cmath.rect(mod, ang)
        return None

    @staticmethod
    def pi():
        """
        Searches for a pi value
        :return: the cmath.pi value
        """
        return cmath.pi

    def __str__(self):
        pass

    def __repr__(self):
        pass

