class Pizza:
    def __init__(self, naam, grootte, toppings):
        self.naam = naam
        self.grootte = grootte
        self.toppings = toppings
        self.prijs = self.bereken_prijs()

    def bereken_prijs(self):
        basisprijs = 0.00
        if self.grootte == "klein":
            basisprijs = 8.99
        elif self.grootte == "medium":
            basisprijs = 10.99
        elif self.grootte == "groot":
            basisprijs = 12.99

        topping_prijs = len(self.toppings) * 1.50

        return basisprijs + topping_prijs

    def toon_informatie(self):
        print(f"\nNaam: {self.naam}")
        print(f"Grootte: {self.grootte}")
        print("Toppings:", ", ".join(self.toppings))
        print(f"Prijs: ${self.prijs:.2f}")


# Maak een paar pizza's met verschillende toppings
pizza1 = Pizza("Margherita", "medium", ["kaas", "tomatensaus"])
pizza2 = Pizza("Pepperoni", "groot", ["kaas", "tomatensaus", "pepperoni"])
pizza3 = Pizza("Hawaï", "klein", ["kaas", "tomatensaus", "ham", "ananas"])

# Toon informatie over de pizza's
pizza1.toon_informatie()
pizza2.toon_informatie()
pizza3.toon_informatie()