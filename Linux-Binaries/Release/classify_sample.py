def classify(model_file, num_classes, pixels, bits_allocated = 16):
	print ">> Example classification on an array with ", num_classes, " classes" 
	print ">> Apply model_file ", model_file
	
	thresholds = [60, 120]
	print ">> Thresholds: "
	for threshold in thresholds:
		print threshold
		
	# simple loop classification
	class_count = [0] * num_classes
	new_pixels = [None] * len(pixels)
	
	for pixel_index in range(0, len(pixels)):
		pixel = pixels[pixel_index]
		classif = num_classes - 1
		
		for t_index in range(0, num_classes - 1):
			threshold = thresholds[t_index]
			if pixel < threshold:
				classif = t_index
				break
				
		new_pixels[pixel_index] = classif	
		class_count[classif] += 1
		
	for index in range(0, num_classes):
		print "Class: " , index, ": number of pixels: ", class_count[index]

	return new_pixels
	
# Test instructions	
original = [0, 200, 500, 1000, 800, 1500, 900, 150]

classified_pixels = classify("my_model.txt", 3, original, 16)
print len(classified_pixels)
#for index in range(0, len(classified_pixels)-1): 
#	print "Index: ", index , " Original" , original[index], " Classified: " , classified_pixels[index]