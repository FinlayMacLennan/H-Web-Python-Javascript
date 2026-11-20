#Scenario 2

#Develop a program that converts temperatures between Celsius and Fahrenheit. 
#The user should be able to input a temperature value and specify whether it's 
#in Celsius or Fahrenheit, and the program should output the converted temperature 
#in the other unit.


#Top-level Design

#Display welcome message and instructions
#Get temperature value and unit from user (OUT: temp, unit)
#Validate input (IN: temp, unit; OUT: isValid)
#Convert temperature (IN: temp, unit; OUT: convertedTemp, convertedUnit)
#Display result (IN: temp, unit, convertedTemp, convertedUnit)

#Wireframe 1:

#Welcome to the temprerature converter
#Please select your tempreure unit (option 1 or 2) and enter your tempreture value:
#Select Celcius (1) or Fahrenheit (2): ________
#Enter tempreture value: _______

#Wireframe 2 (Error screen):
#Error!
#Your entered tempreture value was not vaild
#Make sure your input is between -100 and 100
#Please select your tempreure unit (option 1 or 2) and enter your tempreture value:
#Select Celcius (1) or Fahrenheit (2): ________
#Enter tempreture value: _______

#Wireframe 3:
#Here is your converted tempreture:
#ConvertedUnit
#convertedTemp