total = list()while True:	value = raw_input('enter a num: ')		try:		value_float = float(value)   #this is the key, try this one# 		print value_float				total.append(value_float)# 		print total			except:		if value == 'done':			break					print 'please enter a numeric input'		#quit()     quit() means ending the program		continue		print 'Maximum: ', max(total)print 'Minimum: ', min(total)