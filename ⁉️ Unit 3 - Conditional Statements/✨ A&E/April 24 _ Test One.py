triangle1 = int(input("What is the measure of the first triangle? ")) #gets measurement for triangle 1
triangle2 = int(input("What is the measure of the second triangle? ")) #gets measurement for triangle 2
triangle3 = int(input("What is the measure of the third triangle? ")) #gets measurement for triangle 3

if (triangle1 == 60) and (triangle2 == 60) and (triangle3 == 60):
    print("Valid Triangle, 180 degrees") #outputs valid triangle if sum equals 180 degrees

    elif (triangle1 and triangle2 and triangle3 < 180):
        print("Not a valid triangle") #outputs if it is not a valid triangle, aka if it does not equal 180

elif (triangle1 == triangle2) or (triangle2 == triangle3) or (triangle1 == triangle3):
    print("Equilateral triangle, all angles are equal") #outputs equilateral triangle if all of the angles are equal

elif (triangle1 == triangle2) or (triangle2 == triangle3):
    print("Isosceles Triangle, exactly two angles are equal") #outputs isosceles triangle if exatly two triangles are equal

elif (triangle1 != triangle2) or (triangle2 != triangle3) or (triangle3 != triangle1):
    print("Scalene Triangle, no angles are equal")  #outputs scalene triangle if no angles re equal

elif (triangle1 == 90) or (triangle2 == 90) or (triangle3 == 90):
    print("Right Triangle") #outputs right triangle if only one angle is 90 degrees

else:
    print("N/A") #outputs else
