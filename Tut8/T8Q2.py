class Vector3D:
    def __init__(self,a,b,c):
        self.x=a
        self.y=b
        self.z=c
    def __add__(self,other):
        return Vector3D(self.x+other.x,self.y+other.y,self.z+other.z)
    def __mul__(self,other):
        return (self.x*other.x)+(self.y*other.y)+(self.z*other.z)
    def __str__(self):
        return "[X=%.2f,Y=%.2f,Z=%.2f]" %(self.x,self.y,self.z)

v1=Vector3D(1,2,3)
v2=Vector3D(4,5,6)
v3=v1+v2
print(v3)
dot=v1*v2
print(dot)