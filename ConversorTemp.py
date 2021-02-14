# Conversor de Temperatura Celsius, Kelvin e Fahrenheit

print('*********************** Conversor de temperatura ***************************')

# FUNÇÕES USADAS PARA A CONVERSÃO

#Celsius para Kelvin
def kel1(T):
	return (temp + 273.15)

# Celsius para Fahrenheit
def fah1(T):
	return (temp * 1.8 + 32)

# Fahrenheit para Kelvin
def kel2(T):
	return (((temp - 32) * (5/9)) + 273.15)

# Fahrenheit para Celsius
def cel1(T):
	return ((temp - 32) * 5/9)

# Kelvin para Celsius
def cel2(T):
	return (temp - 273.15)

# Kelvin para Fahrenheit
def fah2(T):
	return (temp - 273.15) * 9/5 + 32 


# Escolha Qual conversão de Temperatura você Gostaria de Fazer

print('Escolha abaixo qual Temperatura \nvocê gostaria de fezer a Conversão\n')
print("1 - CELSIUS => KELVIN \n2 - CELSIUS => FAHRENHEIT \n3 - FAHRENHEIT => KELVIN")
print('4 - FAHRENHEIT => CELSIUS \n5 - KELVIN => CELSIUS \n6 - KELVIN => FAHRENHEIT')

# Entrada da Informação Requerida

escolha = int(input('Ecolha uma Conversão [1/2/3/4/5/6]: '))

while (escolha == 0) or (escolha > 6) :
	
	print('ESCOLHA INCORRETA !!! \nPOR FAVOR, \nREINICIE O PROGRAMA E TENTE NOVAMENTE \n')
	

temp = float(input('Digite a Temperatura que será Convertida: '))

# Checagem das Condições

if(escolha == 1):
	print('A Temperatura convertida de CELSIUS para KELVIN é {:.2f} K'.format(kel1(temp)))

elif(escolha == 2):
	print('A Temperatura convertida de CELSIUS para FAHRENHEIT é {:.2f} °F'.format(fah1(temp)))

elif(escolha == 3):
	print('A Temperatura convertida de FAHRENHEIT para KELVIN é {:.2f} K'.format(kel2(temp)))

elif(escolha == 4):
	print('A Temperatura convertida de FAHRENHEIT para CELSIUS é {:.2f} °C'.format(cel1(temp)))

elif(escolha == 5):
	print('A Temperatura convertida de KELVIN para CELSIUS é {:.2f} °C'.format(cel2(temp)))

elif(escolha == 6):
	print('A Temperatura convertida de KELVIN para FAHRENHEIT é {:.2f} °F'.format(fah2(temp)))


