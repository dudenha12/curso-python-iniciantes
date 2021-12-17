idade = int(input("Idade: "))

if idade >= 18:
	print("Você é um adulto")
elif idade > 12 and idade < 18:
	print("Você é um adolescente")
else:
	print("Você é uma criança")
