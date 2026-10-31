angle1_in_degrees=float(input("enter angle1 in degrees:"))
angle2_in_degrees=float(input("enter angle2 in degrees:"))
angle3_in_degrees=float(input("enter angle3 in degrees:"))
if angle1_in_degrees>0 and angle2_in_degrees>0 and angle3_in_degrees>0 and angle1_in_degrees+angle2_in_degrees+angle3_in_degrees==180:
        print(f"The triangle with angles {angle1_in_degrees}, {angle2_in_degrees}, and {angle3_in_degrees} is valid")
else:
        print(f"The triangle with angles {angle1_in_degrees}, {angle2_in_degrees}, and {angle3_in_degrees} is not valid")



