import random


def menu():
	menu = """
Bienvenido al generador de contraseñas, creado por Martin Martinez

Como consejo te recuerdo que entre más larga sea una contraseña más segura es.
	"""
	print(menu)


def generador():
	mayus = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z')
	minus = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z')
	num = ('1','2','3','4','5','6','7','8','9','0')

	caracteres = mayus + minus + num
	contraseña = []

	largo_cont = int(input('\nIngresa la cantidad de caracteres que deseas tener en tu contraseña: '))

	i = 0

	while i < largo_cont:
		contraseña.append(random.choice(caracteres))
		i += 1

	contraseña = ''.join(contraseña)	
	
	return contraseña


def main():
	menu()
	contraseña_generada = generador()

	print('\nTú contraseña nueva es : ',contraseña_generada)

	generar_otra = input('\n¿Deseas generar otra contraseña? (s/n)  ').lower()

	if generar_otra == 's' or generar_otra == 'si':
		main()
	else:
		print('\nAdiós humano')


if __name__ == '__main__':
	main()
