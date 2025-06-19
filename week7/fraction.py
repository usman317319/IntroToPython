class Fraction:
    def __init__(self, numerator, denominator):
        self.validate_data(numerator, denominator)

        self.fraction = [numerator, denominator]

    def validate_data(self, numerator, denominator):
        for num in [numerator, denominator]:
            if isinstance(num, int):
                pass
            else:
                raise Exception(f"{num} is of type {type(num)}. Whereas it must be an integer.")

    def simplify(self, update = False):
        """
        This function simplifies the fraction.
        return:
          returns simplified Fraction if update is False
          updates self.fraction if update is True
        """
        temp_fraction = self.fraction
        # Apply all of the simplification algorithm to temp_fraction
        #
        #
        #

        if update:
            self.fraction = temp_fraction
            return
        return temp_fraction

    def lcm(self, dem1, dem2):
        """
        Function accepts two numbers to find their Least Common Multiple
        """
        # Write code to find the least common multiple of two numbers
        # return the result

    def new_numerator(self, old_fraction, new_denominator):
        """
        Function accepts the old_numerator and new_denominator.
        Calculates the new numerator
        """
        # Write code to Transform numerator from one fraction to new fraction
        # return the new numerator

    def add(self, other_fraction):
        if isinstance(other_fraction, Fraction):
            pass
        else:
            raise Exception(f"Only Fraction can be added to Fraction. Not {type(other_fraction)}")

        lcm = self.lcm(self.fraction[1], other_fraction.fraction[1])
        return Fraction(self.new_numerator(self.fraction, lcm) + self.new_numerator(other_fraction.fraction, lcm), lcm)

    def sub(self, other_fraction):
        if isinstance(other_fraction, Fraction):
            pass
        else:
            raise Exception(f"Only Fraction can be subtracted to Fraction. Not {type(other_fraction)}")

        lcm = self.lcm(self.fraction[1], other_fraction.fraction[1])
        return Fraction(self.new_numerator(self.fraction, lcm) - self.new_numerator(other_fraction.fraction, lcm), lcm)