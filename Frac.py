def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a
  
class Frac:
    def __init__(self, n, d=1):
        self.num = n
        self.den = d

    def __add__(self, other):
        if isinstance(other, int):
            other = Frac(other)

        n = self.num * other.den + self.den * other.num
        d = self.den * other.den
        common = gcd(n, d)
        return Frac(n//common, d//common)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Frac(other)

        n = self.num * other.den - self.den * other.num
        d = self.den * other.den
        common = gcd(n, d)
        return Frac(n//common, d//common)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Frac(other)

        n = self.num * other.num
        d = self.den * other.den
        common = gcd(n, d)
        return Frac(n//common, d//common)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Frac(other)
        
        n = self.num * other.den
        d = self.den * other.num
        common = gcd(n, d)
        return Frac(n//common, d//common)

    def __rmul__(self, n):
        num = self.num * n
        den = self.den
        common = gcd(num, den)
        return Frac(num//common, den//common)

    def __lt__(self, other):
        return self.num * other.den < self.den * other.num
    
    def __str__(self):
        return f'{self.num}/{self.den}'
