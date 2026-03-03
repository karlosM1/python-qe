class Microwave:
  def __init__ (self, brand: str, power_rating: str):
    self.brand = brand
    self.power_rating = power_rating
    self.turned_on: bool  = False

  def turn_on(self) -> None:
    if not self.turned_on:
      self.turned_on = True
      print(f"{self.brand} microwave is now on.")

  def turn_off(self) -> None:
    if self.turned_on:
      self.turned_on = False
      print(f"{self.brand} microwave is now off.")

  def run(self, seconds: int) -> None:
    if not self.turned_on:
      print(f"{self.brand} microwave is off. Please turn it on first.")
    else:
      print(f"{self.brand} microwave is running for {seconds} seconds.")

  def __add__(self,other):
    return f"{self.brand} and {other.brand} microwaves are now a combo!"
  
  def __mul__(self,other):
    return f"{self.brand} and {other.brand} microwaves are now a combo!"
  
  def __str__ (self, other) -> str:
    return f"{self.brand} microwave with {self.power_rating} power rating."
  
  def __repr__(self):
    return f"Microwave(brand='{self.brand}', power_rating='{self.power_rating}')"

smeg: Microwave = Microwave("Smeg", "800W")
bosch: Microwave = Microwave("Bosch", "800W")
print(smeg.brand)
print(smeg.power_rating)

smeg.turn_on()
smeg.run(30)
smeg.turn_off()
smeg.run(30)
smeg.turn_on()
print(smeg + bosch)
print(repr(smeg))