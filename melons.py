"""Classes for melon orders."""
import random
import datetime

class AbstractMelonOrder(object):
    def __init__(self, species, order_type, qty, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

        if self.qty > 100:
            raise TooManyMelonErrors("Too many melons!")

    def get_base_price(self):
        base_price = 5
        if datetime.datetime.today().weekday() in range(0, 5) and datetime.datetime.now().hour in range(8, 12):
            base_price += 4

        return base_price

    def get_total(self):
        """Calculate price, including tax."""
        base_price = self.get_base_price()

        if self.species == "Christmas":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "International" and self.qty < 10:
            total += 3
        
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order"""

    passed_inspection = False

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super(GovernmentMelonOrder, self).__init__(species, 'Government', qty, 0)

    def mark_inspection(self, passed):
        if passed == True:
            self.passed_inspection = True
            #print passed_inspection


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super(DomesticMelonOrder, self).__init__(species, 'Domestic', qty, .08)



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        self.country_code = country_code
        super(InternationalMelonOrder, self).__init__(species, 'International', qty, .17)

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class TooManyMelonErrors(ValueError):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg