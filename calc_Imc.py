peso = float(input('Qual é o seu peso?')) # define a variável "peso" como o valor inserido no terminal
altura_cm = int(input('Qual é a sua altura?')) # define a variável "altura_cm" como o valor inserido no terminal
altura_m = altura_cm/100 # define a variável "altura_m" como o resultado de "altura_cm/100" (transforma "cm" em "m")

imc = peso/(altura_m**2) # define a variável "imc", que é o cálculo do IMC
imcf = f'{imc:.2f}' # cria a variável "imcf", que é a versão formatada de "imc" (para mostrar apenas as duas primeiras casas decimais)

print('seu IMC é', imcf) # mostra o imc no terminal

# calcula o IMC e responde de acordo com o imc 
if imc <= 18.5: 
    print('Você está abaixo do peso.')
    print('Você deve comer mais calorias por dia!')

elif 18.5 < imc <= 25:
    print('Você está com o peso normal.')
    print('Continue assim!')

elif 25 < imc <= 30:
    print('Você está acima do peso.')
    print('Coma mais salada e vá para a academia!')

else:
    print('Você está obeso.')
    print('Se exercitar é uma ótima ideia!')
