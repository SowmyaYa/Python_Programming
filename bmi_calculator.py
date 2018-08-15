print("This is a program to calculate bmi")
name = input("Enter your name: ")
weight = float(input("Enter your weight in Kgs: "))
height = float(input("Enter your height in meters: "))
def bmi(a, b, c):
	bmi = b/(c**2)
	if bmi > 25:
		print(a+" is overweight. Your bmi is ", round(bmi))
	elif bmi < 18:
		print(a+" is underweight. Your bmi is ", round(bmi))
	else:
		print(a+", your BMI's perfect. Your bmi is ", round(bmi))
bmi(name, weight, height)
