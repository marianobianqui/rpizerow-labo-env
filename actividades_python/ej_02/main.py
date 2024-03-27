#importo las bibliotecas de LED y sleep
from gpiozero import LED
from time import sleep
#configuro unas variables para r,g y b respectivamente para cada uno de los pines que les corresponden
led_r = LED(19)
led_g = LED(26)
led_b = LED(13)

#con este codigo siempre van a estar prendiendose y apagandose los leds y cada uno tiene un timer diferente de encendido
while True:    
	led_r.on()
	sleep(1)
	led_r.off()
	led_g.on()
	sleep(0.5)
	led_g.off()
	led_b.on()
	sleep(0.25)
	led_b.off()
