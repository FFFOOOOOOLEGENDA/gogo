print("Выберите в чём будите вводить размеры , если в милиметрах то (mm) или в сантиметрах (cm)")
q = input("Еденицы измеренрия >>")
if q == "mm":
	asd = 1
elif q == "cm":
	asd = 2
else:
	print("Вы ввели неправильное число , повторите попытку")
if asd == 1:
	a = int(input("a mm >> "))
	b = int(input("b mm >> "))
	c = int(input("c mm >> "))
	d = int(input("d mm >> "))
	if c >= a + 1 and d >= b + 1:
		print(True)
	else:
		print(False)
elif asd == 2:
	a = int(input("a cm >> "))
	b = int(input("b cm >> "))
	c = int(input("c cm >> "))
	d = int(input("d cm >> "))
	if c > a and d > b :
		print(True)
	else:
		print(False)

#a b : c d :1mm
