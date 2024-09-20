# class A:
#     def a(self):
#         print("This is a class A")

# class B(A):
#     def b(self):
#         print("This is a class B")

# obj = B()
# print(dir(obj))
# obj.a()
# obj.b()


# class A:
#     def a(self):
#         print("This is a class A")

# class B(A):
#     def b(self):
#         print("This is a class B")

# class C(B):
#     def c(self):
#         print("This is a class C")

# obj = C()
# print(dir(obj))
# obj.a()
# obj.b()
# obj.c()




# class A:
#     def a(self):
#         print("This is a class A")

# class B:
#     def b(self):
#         print("This is a class B")

# class C(A, B):
#     def c(self):
#         print("This is a class C")

# obj = C()
# print(dir(obj))
# obj.a()
# obj.b()
# obj.c()



# class Shape:
#     def shape(self):
#         print("From Shape class")

# class Shape2D(Shape):
#     def shape2D(self):
#         print("From Shape2D class")

# class Circle(Shape2D):
#     def circle(self):
#         print("From Circle class")

# class Square(Shape2D):
#     def square(self):
#         print("From Square class")

# class Shape3D(Shape):
#     def shape3D(self):
#         print("From Shape3D class")

# obj = Square()
# # obj.square()
# # obj.shape2D()
# # obj.shape()

# print(Square.mro())
# print(Square.__mro__)