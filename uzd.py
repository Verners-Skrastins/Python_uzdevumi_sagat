# Funkcija, kas atgriež atšķirību starp divām virknēm
def find_string_difference(a, b):
  return f"Atšķirība starp '{a}' un '{b}': {a} - {b}"



# Sākotnējie saraksti ar virknēm
saraksts1 = ["apple", "banana", "cherry", "date", "elderberry"]
saraksts2 = ["banana", "date", "fig", "grape", "honeydew"]



# Izmantojot map(), izveidojam jaunu sarakstu ar atšķirībām
atšķirības = list(map(find_string_difference, saraksts1, saraksts2))



# Izdrukājam rezultātu
for atšķirība in atšķirības:
  print(atšķirība)