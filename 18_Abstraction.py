#Abstraction---> Data hiding
# ekta car er break press korlam break hoilo but vetorer mechanism janar tw tomar dorkar nai etai abstraction  
class shape:
    def area(self, a, b = 10):
        return a*b

p = shape()
print(p.area(12)) #area ke call korlam but vetore ki kaj hocche eta dekha jay na etai Abstraction
print(p.area(12,10))