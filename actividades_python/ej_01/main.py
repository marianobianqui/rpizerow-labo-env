#importo de librerias codigo de LED y Button
from gpiozero import LED, Button
#esto sirve para que despues de que cuando se deje de dar la señal al led este se apague
from signal import pause
#establezco el pin de GPIO 13 como el LED
led = LED(13)
#eztablezco el pin de GPIO 18 como el boton
button= Button(18)
#cuando presione el boton el estara prendido y cuando no este presionado estara apagado
button.when_pressed = led.on
button.when_released = led.off

pause() 
