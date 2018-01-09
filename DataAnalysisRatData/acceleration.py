#Brandon Troisi
#April 2016
#acceleration.py

def accelmaleK():
	'''
	Reads data from the textfile MaleRatDataK, which contains the mass and force data
	for male rats in Ketawhack. From that data, this function calculates
	the acceleration of each male rat by dividing the impact force by its mass.  
	'''
	maledatak=open("MaleRatDataK.txt","r") 
	'''
	reads info from the MaleRatDataKetawhack file	
	'''
	contents=maledatak.read().split()
	'''
	Creats list where everything in file including words and numbers is split
	by a white space  
	'''
	data=contents[2:]
	'''
	Creates a new list with only data. However, the computer sees this data 
	as a sequence of characters called strings, not numbers.
	So these strings need to be converted to numbers with decimal points later on.
	'''
	maledatak.close() #Closes file
	
	for i in range(len(data)):
		data[i]=float(data[i])
		
	'''
	The above code converts the data from a string to a number with decimals. 
	'''
	mass=data[0::2]
	'''
	Creats a list of numbers that is the mass of each rat
	'''
	force=data[1::2]
	'''
	Creates a list of numbers that is the impact force each rat experienced
	'''
	
	
	accelM2=force[0]/mass[0] #Calculates acceleration of M2
	accelM4= force[1]/mass[1] #Calculates acceleration of M4
	accelM6=force[2]/mass[2] #Calculates acceleration of M6
	accelM8= force[3]/mass[3] #Calculates acceleration of M8
	accelM10= force[4]/mass[4] #Calculates acceleration of M10
	accelM12= force[5]/mass[5] #Calculates acceleration of M12
	accelM14= force[6]/mass[6] #Calculates acceleration of M14
	accelM16= force[7]/mass[7] #Calculates acceleration of M16
	accelM18= force[8]/mass[8] #Calculates acceleration of M18
	accelM20= force[9]/mass[9] #Calculates acceleration of M20
	avgaccelM=(accelM2+accelM4+accelM6+accelM8+accelM10+accelM12+accelM14+accelM16+
	accelM18+accelM20)/10
	'''
	Calculates the average acceleration of the male rats in Ketawhack.
	'''
	
	print ' '
	print 'The acceleration of M2 in Ketawhack is', accelM2, 'm/s^2'
	print 'The acceleration of M4 in Ketawhack is', accelM4, 'm/s^2'
	print 'The acceleration of M6 in Ketawhack is', accelM6, 'm/s^2'
	print 'The acceleration of M8 in Ketawhack is', accelM8, 'm/s^2'
	print 'The acceleration of M10 in Ketawhack is', accelM10, 'm/s^2'
	print 'The acceleration of M12 in Ketawhack is', accelM12, 'm/s^2'
	print 'The acceleration of M14 in Ketawhack is', accelM14, 'm/s^2'
	print 'The acceleration of M16 in Ketawhack is', accelM16, 'm/s^2'
	print 'The acceleration of M18 in Ketawhack is', accelM18, 'm/s^2'
	print 'The acceleration of M20 in Ketawhack is', accelM20, 'm/s^2'
	print 'The average acceleation of the males in Ketawhack is', avgaccelM, 'm/s^2' 
	print 'The above data was exported to the file MaleKetawhackAccelerationData.txt'
	'''
	These print the acceleration of each male rat and their average acceleration
	'''
	
	exportfile=open("MaleKetawhackAccelerationData.txt", "w")
	x=0
	for i in (accelM2,accelM4,accelM6,accelM8, accelM10, accelM12, accelM14, accelM16,
	accelM18,accelM20):
			x+=2
			exportfile.write("M"+str(x)+ " " +str(i)+ ' m/s^2'+'\n')
	
	exportfile.write("Avg " + str(avgaccelM) + ' m/s^2')
	'''
	This exports the male ketawhack data printed on the screen to the file
	MaleKetawhackAccelerationData.txt
	'''
		
def accelfemaleK():
	'''
	Reads data from the textfile FemaleRatDataK, which contains the mass and force data
	for female rats in Ketawhack. From that data, this function calculates 
	the acceleration of each female rat by dividing the impact force by its mass.  
	'''
	femaledatak=open("FemaleRatDataK.txt","r") 
	'''
	reads info from the FemaleRatDataKetawhack file
	'''
	contents=femaledatak.read().split()
	'''
	Creats list where everything in file including words and numbers is split
	by a white space  
	'''
	data=contents[2:]
	'''
	Creates a new list with only data. However, the computer sees this data 
	as a sequence of characters called strings, not numbers.
	So these strings need to be converted to numbers with decimal points later on.
	'''
	femaledatak.close() #Closes file
	
	for i in range(len(data)):
		data[i]=float(data[i])
		
	'''
	The above code converts the data from a string to a number with decimals. 
	'''
	mass=data[0::2]
	'''
	Creats a list of numbers that is the mass of each rat
	'''
	force=data[1::2]
	'''
	Creates a list of numbers that is the impact force each rat experienced
	'''
	accelF4=force[0]/mass[0] #Calculates acceleration of F2
	accelF6= force[1]/mass[1] #Calculates acceleration of F4
	accelF8=force[2]/mass[2] #Calculates acceleration of F6
	accelF10= force[3]/mass[3] #Calculates acceleration of F8
	accelF12= force[4]/mass[4] #Calculates acceleration of F10
	accelF14= force[5]/mass[5] #Calculates acceleration of F12
	accelF16= force[6]/mass[6] #Calculates acceleration of F14
	accelF18= force[7]/mass[7] #Calculates acceleration of F16
	accelF20=force[8]/mass[8] #Calculates acceleration of F18
	avgaccelF=(accelF4+accelF6+accelF8+accelF10+accelF12+accelF14+accelF16+
	accelF18+accelF20)/9
	'''
	Calculates the average acceleration of the male rats in Ketawhack.
	'''
	
	print ' '
	print 'The acceleration of F4 in Ketawhack is', accelF4, 'm/s^2'
	print 'The acceleration of F6 in Ketawhack is', accelF6, 'm/s^2'
	print 'The acceleration of F8 in Ketawhack is', accelF8, 'm/s^2'
	print 'The acceleration of F10 in Ketawhack is', accelF10, 'm/s^2'
	print 'The acceleration of F12 in Ketawhack is', accelF12, 'm/s^2'
	print 'The acceleration of F14 in Ketawhack is', accelF14, 'm/s^2'
	print 'The acceleration of F16 in Ketawhack is', accelF16, 'm/s^2'
	print 'The acceleration of F18 in Ketawhack is', accelF18, 'm/s^2'
	print 'The acceleration of F20 in Ketawhack is', accelF20, 'm/s^2'
	print 'The average acceleation of the females in Ketawhack is', avgaccelF, 'm/s^2' 
	print 'The above data was exported to the file FemaleKetawhackAccelerationData.txt'
	'''
	These print the acceleration of each female rat and their average acceleration
	'''
	
	
	exportfile=open("FemaleKetawhackAccelerationData.txt", "w")
	x=2
	for i in (accelF4,accelF6,accelF8, accelF10, accelF12, accelF14, accelF16,
	accelF18,accelF20):
			x+=2
			exportfile.write("F"+str(x)+ " " +str(i)+ ' m/s^2'+'\n')
	
	exportfile.write("Avg " + str(avgaccelF) + ' m/s^2')
	
	'''
	This exports the female ketawhack data printed on the screen to the file 
	FemaleKetawhackAccelerationData.txt
	'''
def accelmaleJ():
	'''
	Reads data from the textfile MaleRatDataJ which contains the mass and force data
	for male rats in Jim Beam. From that data, this function calculates
	the acceleration of each male rat by dividing the impact force by its mass.  
	'''
	maledataj=open("MaleRatDataJ.txt","r") 
	'''
	reads info from the MaleRatDataJ file	
	'''
	contents=maledataj.read().split()
	'''
	Creats list where everything in file including words and numbers is split
	by a white space  
	'''
	data=contents[2:]
	'''
	Creates a new list with only data. However, the computer sees this data 
	as a sequence of characters called strings, not numbers.
	So these strings need to be converted to numbers with decimal points later on.
	'''
	maledataj.close() #Closes file
	
	for i in range(len(data)):
		data[i]=float(data[i])
		
	'''
	The above code converts the data from a string to a number with decimals. 
	'''
	mass=data[0::2]
	'''
	Creats a list of numbers that is the mass of each rat
	'''
	force=data[1::2]
	'''
	Creates a list of numbers that is the impact force each rat experienced
	'''
	
	
	accelM2=force[0]/mass[0] #Calculates acceleration of M2
	accelM4= force[1]/mass[1] #Calculates acceleration of M4
	accelM6=force[2]/mass[2] #Calculates acceleration of M6
	accelM8= force[3]/mass[3] #Calculates acceleration of M8
	accelM10= force[4]/mass[4] #Calculates acceleration of M10
	accelM12= force[5]/mass[5] #Calculates acceleration of M12
	accelM14= force[6]/mass[6] #Calculates acceleration of M14
	accelM16= force[7]/mass[7] #Calculates acceleration of M16
	avgaccelM=(accelM2+accelM4+accelM6+accelM8+accelM10+accelM12+accelM14+accelM16)/8
	'''
	Calculates the average acceleration of the male rats in Jim Beam.
	'''
	
	print ' '
	print 'The acceleration of M2 in Jim Beam is', accelM2, 'm/s^2'
	print 'The acceleration of M4 in Jim Beam is', accelM4, 'm/s^2'
	print 'The acceleration of M6 in Jim Beam is', accelM6, 'm/s^2'
	print 'The acceleration of M8 in Jim Beam is', accelM8, 'm/s^2'
	print 'The acceleration of M10 in Jim Beam is', accelM10, 'm/s^2'
	print 'The acceleration of M12 in Jim Beam is', accelM12, 'm/s^2'
	print 'The acceleration of M14 in Jim Beam is', accelM14, 'm/s^2'
	print 'The acceleration of M16 in Jim Beam is', accelM16, 'm/s^2'
	print 'The average acceleation of the males in Jim Beam is', avgaccelM, 'm/s^2' 
	print 'The above data was exported to the file MaleJimBeamAccelerationData.txt'
	'''
	These print the acceleration of each male rat and their average acceleration
	'''
	
	exportfile=open("MaleJimBeamAccelerationData.txt", "w")
	x=0
	for i in (accelM2,accelM4,accelM6,accelM8, accelM10, accelM12, accelM14, accelM16):
			x+=2
			exportfile.write("M"+str(x)+ " " +str(i)+ ' m/s^2'+'\n')
	
	exportfile.write("Avg " + str(avgaccelM) + ' m/s^2')	
	
	'''
	This exports the male Jim Beam data to a file called 
	MaleJimBeamAccelerationData.txt
	'''

def accelfemaleJ():
	'''
	Reads data from the textfile MaleRatDataJ which contains the mass and force data
	for male rats in Jim Beam. From that data, this function calculates
	the acceleration of each male rat by dividing the impact force by its mass.  
	'''
	femaledataj=open("FemaleRatDataJ.txt","r") 
	'''
	reads info from the FemaleRatDataJ file	
	'''
	contents=femaledataj.read().split()
	'''
	Creats list where everything in file including words and numbers is split
	by a white space  
	'''
	data=contents[2:]
	'''
	Creates a new list with only data. However, the computer sees this data 
	as a sequence of characters called strings, not numbers.
	So these strings need to be converted to numbers with decimal points later on.
	'''
	femaledataj.close() #Closes file
	
	for i in range(len(data)):
		data[i]=float(data[i])
		
	'''
	The above code converts the data from a string to a number with decimals. 
	'''
	mass=data[0::2]
	'''
	Creats a list of numbers that is the mass of each rat
	'''
	force=data[1::2]
	'''
	Creates a list of numbers that is the impact force each rat experienced
	'''
	
	
	accelF2=force[0]/mass[0] #Calculates acceleration of M2
	accelF4= force[1]/mass[1] #Calculates acceleration of M4
	accelF6=force[2]/mass[2] #Calculates acceleration of M6
	accelF8= force[3]/mass[3] #Calculates acceleration of M8
	accelF10= force[4]/mass[4] #Calculates acceleration of M10
	accelF12= force[5]/mass[5] #Calculates acceleration of M12
	accelF14= force[6]/mass[6] #Calculates acceleration of M14
	accelF16= force[7]/mass[7] #Calculates acceleration of M16
	avgaccelF=(accelF2+accelF4+accelF6+accelF8+accelF10+accelF12+accelF14+accelF16)/8
	'''
	Calculates the average acceleration of the male rats in Jim Beam.
	'''
	
	print ' '
	print 'The acceleration of F2 in Jim Beam is', accelF2, 'm/s^2'
	print 'The acceleration of F4 in Jim Beam is', accelF4, 'm/s^2'
	print 'The acceleration of F6 in Jim Beam is', accelF6, 'm/s^2'
	print 'The acceleration of F8 in Jim Beam is', accelF8, 'm/s^2'
	print 'The acceleration of F10 in Jim Beam is', accelF10, 'm/s^2'
	print 'The acceleration of F12 in Jim Beam is', accelF12, 'm/s^2'
	print 'The acceleration of F14 in Jim Beam is', accelF14, 'm/s^2'
	print 'The acceleration of F16 in Jim Beam is', accelF16, 'm/s^2'
	print 'The average acceleation of the females in Jim Beam is', avgaccelF, 'm/s^2' 
	print 'The above data was exported to the file FemaleJimBeamAccelerationData.txt'
	'''
	These print the acceleration of each male rat and their average acceleration
	'''
	
	exportfile=open("FemaleJimBeamAccelerationData.txt", "w")
	x=0
	for i in (accelF2,accelF4,accelF6,accelF8, accelF10, accelF12, accelF14, accelF16):
			x+=2
			exportfile.write("M"+str(x)+ " " +str(i)+ ' m/s^2'+'\n')
	
	exportfile.write("Avg " + str(avgaccelF) + ' m/s^2')
	
	'''
	This exports the female Jim Beam data to a file called 
	FemaleJimBeamAccelerationData.txt
	'''
	

if __name__=='__main__':
	accelmaleK()
	accelfemaleK()
	accelmaleJ()
	accelfemaleJ()
'''
The above code tells the computer which parts of the program to run
'''
	