"""
DMath is a class that expands complex numbers functions
implemented in cmath c module.
"""
import cmath, math

class DMath():

    def __init__(self, z):        
        """
        Initializes z as complex number in an instance attribute.-
        if z is in polar format then it converts z into binomial format.
        Also, ro and roots instance variables takes default values.
        """
        if type(z) == tuple:
            z = cmath.rect(z)
        self.z = z
        self.ro = None
        self.roots = []

    def n_roots(self, n, degrees=False):
        """
        It calculates the n number of roots of a z complex number.
        It ilustrates the The Moivre theorem.

        """
        if type(n) != int:
            n = int(n)
        if n == 0:
            raise ValueError('Missing n as number of roots')
        
        n = abs(n)
        polar = cmath.polar(self.z)
        self.ro = polar[0] ** (1/n)
        fi = polar[1]
        k = 0
        while k < n:
            zeta = (fi + 2 * k * cmath.pi) / n
            if degrees:
                zeta = math.degrees(zeta)
            self.roots.append(zeta)
            k += 1

        return (self.ro,) + tuple(self.roots)

    def __str__(self):
        pass

    def __repr__(self):
        pass


