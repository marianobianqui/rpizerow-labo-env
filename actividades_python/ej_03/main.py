from gpiozero import LED
from gpiozero import Buzzer
rgb_red = LED(19)
rgb_green = LED(13)
rgb_blue = LED(26)
Buzzer = Buzzer(22)

# ejemplo de input

# hola = input("escribi comando: ")
# en hola se va a guardar lo que se escriba en la terminal
# si yo escribi buzz.on entonces es es lo que se guardo en hola
# usando if comparo lo que esta en hola con los comandos
# if hola == buzz.on:
# 	buzzer.on())
while True:
	prompt = input("prompt: ")
	if (prompt == "buzz on"):
		Buzzer.on()
	if prompt == ("buzz off"):
		Buzzer.off()
	if prompt ==  ("rgb red"):
		rgb_red.on()
	if prompt ==  ("rgb green"):
	 	rgb_green.on()
	if prompt == ("rgb blue"):
		rgb_blue.on()
	if prompt == ("rgb off"):
		rgb_red.off()
		rgb_blue.off()
		rgb_green.off()
# grahhh no sé si esto funciona
# tambien es terrible hacer que la página web se vea bien en todos los dispositivos
