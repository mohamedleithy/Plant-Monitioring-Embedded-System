import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine
import _thread 
from machine import UART, Pin
import utime

ssid = 'Leithy'
mois = 3
moisture = 2



def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, '12345678')
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print(wlan.ifconfig())
    ip = wlan.ifconfig()[0]
    return ip
    
def open_socket(ip, soc):
    # Open a socket
    address = (ip, soc)
    connection = socket.socket()
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind(address)
    connection.listen(1)
    # connection.setblocking(0)
    print(connection)
    return connection

def webpage(temperature, state):
    #Template HTML
    html = f"""
 <!DOCTYPE html>
<html>
<head>
<title>EZ Plant</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>
<body>


<!-- Navbar (sit on top) -->
<div class="w3-top">
  <div class="w3-bar w3-white w3-wide w3-padding w3-card">
    <a href="#home" class="w3-bar-item w3-button"><b></b> </a>
    <!-- Float links to the right. Hide them on small screens -->
    <div class="w3-right w3-hide-small">
      <img class="navbarlogo" src="https://i.ibb.co/cxWfqD8/EZPlant-Logo.png" alt="Ezlogo">
    </div>
  </div>
</div>

<!-- Header -->
<!-- "w3-jumbo w3-animate-top" -->
<!-- w3-xxxlarge w3-text-white -->
<div class="mainpage">
<div class="TopPage">
<div class="w3-display-container w3-content w3-wide"  id="home">
    <div class="PageContent">
    <img class="mainimg" src="https://i.ibb.co/5kLJ3nm/EzLogo.png" alt="Ezlogo">
    <!-- <div class = "imagegreen">
      <img class="green" src="https://i.ibb.co/MGb03w0/1.jpg" width="30%" height="30%">
      </div> -->
    <div class = "TextSection">
    <h1 class="w3-jumbo w3-animate-top"><b>Grow your plants</b></h1>
    <h1 class=" w3-jumbo w3-animate-top"><b>with EzPlant</b></h1>
  </div>
</div>
</div>

<!-- Page content -->

<div class="w3-content w3-padding" style="max-width:1564px">




  <!-- Configure Section -->
  <div class="main">
  <div class="w3-container w3-padding-32" id="Configure">
    <h3 class="w3-border-bottom w3-border-light-grey w3-padding-16">Data Section</h3>
    <h1>Plants data</h1>

        <!-- <form action="./lighton">
        <input type="submit" value="Light on" />
        </form>
        <form action="./lightoff">
        <input type="submit" value="Light off" />
        </form> -->
        <!-- <p>LED is {state}</p> -->
        <p class="Temp">Temperature is {temperature}</p>

        <p class = "Moisture">Moisture for the first plant is {moisture}%</p>
        <p> choose the type of your first plant: </p>
        <div>
          <!-- <label for="plants">Select the type of the plant:</label>
          <div class = "dropdownClass"> 
           <form method="POST" action = "./plants_id=" >
          <select name="plants_id=" id="plants_id">
            <option value="11">Wildflowers</option>
            <option value="12">Thistle</option>
            <option value="13" >Flowers</option>
            <option value="14" selected>Herbs</option>
          </select> -->

          <form class = "plants_id" name="plants_id" action="./plants_id" method="GET">
            <select name="plants_id">
              <option value="11">Wildflowers</option>
              <option value="12">Thistle</option>
              <option value="13" >Flowers</option>
              <option value="14" selected>Herbs</option>
            </select>
            <input class="w3-button w3-black w3-section" type="submit" id="submit" value="Send">
           </form>

        <p class = "Moisture">Moisture for the second plant is {mois}%</p>
        <p> choose the type of your second plant: </p>
        <div>
          <!-- <label for="plants">Select the type of the plant:</label>
          <div class = "dropdownClass"> 
           <form method="POST" action = "./plants_id=" >
          <select name="plants_id=" id="plants_id">
            <option value="21">Wildflowers</option>
            <option value="22">Thistle</option>
            <option value="23" >Flowers</option>
            <option value="24" selected>Herbs</option>
          </select> -->

          <form class = "plants_id" name="plants_id" action="./plants_id" method="GET">
            <select name="plants_id">
              <option value="21">Wildflowers</option>
              <option value="22">Thistle</option>
              <option value="23" >Flowers</option>
              <option value="24" selected>Herbs</option>
            </select>
            <input class="w3-button w3-black w3-section" type="submit" id="submit" value="Send">
           </form>






          <!-- <form action="./lighton">
            <input type="submit" value="Light on" />
          </form>
          <form action="./lightoff">
            <input type="submit" value="Light off" />
          </form>
          <form action="./lighton">
            <input type="submit" value="Light on" />
          </form>
          <form action="./lightoff">
            <input type="submit" value="Light off" />
          </form> -->



        </form>
          </div>
          </div>

  </div>
</div>


  </div>
</div>
<!-- Image of location/map -->

<!-- End page content -->
</div>


</body>

<style>





.dropdownClass{{
  display: inline-block;
  /* border: 1px solid #ccc; */
  /* border-radius: 4px; */
  /* box-sizing: border-box; */
  width: 200px;
  height: 34px;


}}

.plants{{
  width: 100%;
  height: 100%;

  box-sizing: border-box;
  background-color: white;

}}

.navbarlogo{{
  width: 200px; 
   height: 50px;
   margin-right: 80%;
}}
.mainimg{{
  position: relative;

  width: 600px;
    height: 600px;
  margin-left: 550px;
   margin-top: 100px;
}}

.TextSection{{
  margin-left: -180px;
  margin-top: -400px;
}}


.imagegreen{{
  position: absolute;
  margin-left: 700px;
  margin-top:  -400px;


}}

.main{{
  background-color: #51862c84;
  margin-top:  170px;
}}

p {{
  font-size: 25px;
}}

.mainpage{{
  background-color: #5ab71784;
  
}}
.PageContent{{
  background-color: #83be5a84;
  
  border-radius: 1200px;
}}

.plants_id{{
  width: 100%;
  height: 100%;
  box-sizing: border-box;
  border-radius: 4px;
  margin-left: 100px;
  margin-top: 20px;
  margin-bottom: 20px;
  padding: 10px;
  font-size: 20px;
  color: black;
  font-weight: bold;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  padding: 16px 32px;
  margin: 4px 2px;

}}

.Moisture{{
  font-weight: bold;
}}

.Temp{{
  font-weight: bold;
}}
</style>



</html>

            """
    return str(html)

def serve(connection):
    #Start a web server
    state = 'OFF'
    pico_led.off()
    temperature = 0
    while True:
        
        try:
            client = connection.accept()[0]
            request = client.recv(1024)
            request = str(request)
            request = request.split()[1]
        except IndexError:
            pass
       
        if request =='/plants_id?plants_id=11':
            uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
            uart0.write('11')
        elif request =='/plants_id?plants_id=12':
            uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
            uart0.write('12')
        elif request =='/plants_id?plants_id=13':
            uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
            uart0.write('13')
        elif request =='/plants_id?plants_id=14':
            uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
            uart0.write('14')
        elif request =='/plants_id?plants_id=21':
            uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
            uart0.write('21')
        elif request =='/plants_id?plants_id=22':
            uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
            uart0.write('22')
        elif request =='/plants_id?plants_id=23':
            uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
            uart0.write('23')
        elif request =='/plants_id?plants_id=24':
            uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
            uart0.write('24')
            
        print(request)  
        temperature = pico_temp_sensor.temp   
        html = webpage(temperature, state)
        client.send(html)
        client.close()


# uart0_irq = UART.irq(trigger=UART.RX_ANY, handler=readUart)

def readUart():
    global moisture
    global mois
    uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1), timeout=100)
        
    uart0.write('20')
    while(1): 
        uartBuf = uart0.read(10)
        if uartBuf is not None:
          #  uartBuf.decode("utf-8") 
            if '<' in uartBuf and '>' in uartBuf:

                temperature = pico_temp_sensor.temp
                stringBuf = str(uartBuf)
                moistureValues = stringBuf[(stringBuf.find('<')+1):stringBuf.find('>')]
                moisture = moistureValues[:moistureValues.find(' ')]
                mois = moistureValues[(moistureValues.find(' ')+1):]
                mois = mois[:mois.find(' ')]
                print(moisture)
                print(mois)
 

try:
    ip = connect()
    connection = open_socket(ip,80)
    t1 = _thread.start_new_thread(readUart,())
    
    serve(connection)

except KeyboardInterrupt:
    machine.reset()
