import CartesianPoint_class


point1 = CartesianPoint_class.CartesianPoint(10, 20, 30, 40, 50, 60)
point2 = CartesianPoint_class.CartesianPoint(11, 22, 33, 44, 55, 66)
point3 = CartesianPoint_class.CartesianPoint(13, 23, 43, 45, 56, 67)
point4 = CartesianPoint_class.CartesianPoint(13, 23, 43, 45, 56, 67)
point5 = CartesianPoint_class.CartesianPoint(13, 23, 43, 45, 56, 67)
point6 = CartesianPoint_class.CartesianPoint(13, 23, 43, 45, 56, 67)
point7 = CartesianPoint_class.CartesianPoint(13, 23, 43, 45, 56, 67)
point8 = CartesianPoint_class.CartesianPoint(13, 23, 43, 45, 56, 67)


points=[point1,point2,point3,point4,point5,point6,point7,point8]

#nombre de trajectoires
for i in range(6):
    print(f"trajectoire {i+1}:")
    print(f"Point1: {CartesianPoint_class.generate_point_with_margin( point1, x=5, y=5, z=5, w=5, p=5, r=5)}")
    print(f"Point2: {CartesianPoint_class.generate_point_with_margin( point2, x=5, y=5, z=5, w=5, p=5, r=5)}")
    print(f"Point3: {CartesianPoint_class.generate_point_with_margin( point3, x=5, y=5, z=5, w=5, p=5, r=5)}")
    print(f"Point4: {CartesianPoint_class.generate_point_with_margin( point4, x=5, y=5, z=5, w=5, p=5, r=5)}")
    print(f"Point5: {CartesianPoint_class.generate_point_with_margin( point5, x=5, y=5, z=5, w=5, p=5, r=5)}")
    print(f"Point6: {CartesianPoint_class.generate_point_with_margin( point6, x=5, y=5, z=5, w=5, p=5, r=5)}")
    print(f"Point7: {CartesianPoint_class.generate_point_with_margin( point7, x=5, y=5, z=5, w=5, p=5, r=5)}")
    print(f"Point8: {CartesianPoint_class.generate_point_with_margin( point8, x=5, y=5, z=5, w=5, p=5, r=5)}")


