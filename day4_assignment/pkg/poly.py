class Poly:
    def __init__(self, *coeffs):
        self.coeffs = tuple(coeffs)

    def __add__(self, other):
        a = list(self.coeffs)
        b = list(other.coeffs)
        if len(a) < len(b):
            a = [0] * (len(b) - len(a)) + a
        elif len(b) < len(a):
            b = [0] * (len(a) - len(b)) + b
        result_coeffs = [x + y for x, y in zip(a, b)]
        return Poly(*result_coeffs)

    def __repr__(self):
        coeffs_str = ",".join(str(c) for c in self.coeffs)
        return f"Poly({coeffs_str})"