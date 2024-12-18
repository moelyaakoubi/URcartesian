import CartesianPoint_class


point1 = CartesianPoint_class.CartesianPoint(10, 20, 30, 40, 50, 60)
point2 = CartesianPoint_class.CartesianPoint(11, 22, 33, 44, 55, 66)
point3 = CartesianPoint_class.CartesianPoint(13, 23, 43, 45, 56, 67)
point4 = CartesianPoint_class.CartesianPoint(13, 23, 43, 45, 56, 67)
point5 = CartesianPoint_class.CartesianPoint(13, 23, 43, 45, 56, 67)
point6 = CartesianPoint_class.CartesianPoint(13, 23, 43, 45, 56, 67)
point7 = CartesianPoint_class.CartesianPoint(13, 23, 43, 45, 56, 67)
point8 = CartesianPoint_class.CartesianPoint(13, 23, 43, 45, 56, 67)





for i in range(6):
    print(f"trajectoire {i+1}:")
    print(f"Point 1: {CartesianPoint_class.generate_point_with_margin(point1, x=5, y=5, z=5, w=5, p=5, r=5)}")
    print(f"Point 2: {CartesianPoint_class.generate_point_with_margin(point2, x=5, y=5, z=5, w=5, p=5, r=5)}")
    print(f"Point 3: {CartesianPoint_class.generate_point_with_margin(point3, x=5, y=5, z=5, w=5, p=5, r=5)}")
    print("\n")

