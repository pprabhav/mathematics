# imports mpmath module
import mpmath

# THis module has basic math functions like addition, subtraction, multiplication, division, modulus, 
# trig functions including sin, cos, tan, sec, csc, cot, constants like e, pi, exponentials, square, 
# cube,  inverse, root, cube root, logarithms and natural logs.

pi=3.14159265359
e=2.71828182845

# Adds a and b
def add(a, b, digits=12):
        mpmath.mp.dps=digits
        return (mpmath.mpf(a)+mpmath.mpf(b))

# Subtracts b from a
def subtract(a, b, digits=12):
        mpmath.mp.dps=digits
        return (mpmath.mpf(a)-mpmath.mpf(b))

# Multiplies a and b
def multiply(a, b, digits=12):
        mpmath.mp.dps=digits
        return (mpmath.mpf(a)*mpmath.mpf(b))

# Divides a by b
def divide(a, b, digits=12):
        mpmath.mp.dps=digits
        return (mpmath.mpf(a)/mpmath.mpf(b))

# Returns a mod b
def mod(a, b):
        return (a%b)

#Calculates pi to a given number of digits with a given number of iterations 
def piCalc(digits=12, iterations=10):
        mpmath.mp.dps = digits
        piP = mpmath.mpf(0)

        for n in range(0, iterations):
                term1 = mpmath.mpf(4) / (mpmath.mpf(8*n+1) * mpmath.power(mpmath.mpf(16), n))
                term2 = mpmath.mpf(2) / (mpmath.mpf(8*n+4) * mpmath.power(mpmath.mpf(16), n))
                term3 = mpmath.mpf(1) / (mpmath.mpf(8*n+5) * mpmath.power(mpmath.mpf(16), n))
                term4 = mpmath.mpf(1) / (mpmath.mpf(8*n+6) * mpmath.power(mpmath.mpf(16), n))
                iteration = term1 - term2 - term3 - term4
                piP += iteration

                return piP
        
# Returns factorial
def factorial(a):
        factorial=1
        for n in range(1, a+1):
                factorial*=n
        
        return factorial

# Returns the alternating factorial of a number
def alternatingFactorial(a, even=True):
        af=1
        if (even):
                af=1
                for i in range(2, (a-1)*2+1, 2):
                        af*=i
                            
        else:
                af=1
                for i in range(1, (a-1)*2+1, 2):
                         af*=i
        return af


#Calculates e to a given number of digits with a given number of iterations 
def eCalc(digits=12, iterations=20):
        mpmath.mp.dps=digits
        term=mpmath.mpf(0)
        for n in range(0, iterations+1):
                print(n)
                term+=mpmath.mpf(1/factorial(n))
        eP=term
        return eP

# Converts from degrees to radians
def degToRad(degree, digits=12, iterations=10):
        mpmath.mp.dps=digits
        piC=piCalc(iterations, digits)
        rads=mpmath.mpf(degree*piC/mpmath.mpf(180))

        return rads

# Converts an angle so that it lies between 0 and 2 pi radians
def getToDomain(rad, digits=12, iterations=10):
        mpmath.mp.dps=digits
        radians=mpmath.mpf(rad)
        piC=piCalc(iterations, digits)
        while(True):
                if (radians<=0):
                        radians+=mpmath.mpf(2*piC)
                elif (radians>=mpmath.mpf(2*piC)):
                        radians-=mpmath.mpf(2*piC)
                else:
                        break
        
        return radians

#Calculates the sine of an angle
def sin(rad, digits=12, iterations=10):
        mpmath.mp.dps=digits
        radians=mpmath.mpf(getToDomain(rad))
        piC=piCalc(iterations, digits)
        sin=mpmath.mpf(0)
        for i in range(0, iterations):
                loopTerm=1
                for n in range(2*i+1):
                        loopTerm*=radians
                loopTerm=mpmath.mpf(loopTerm/factorial(2*i+1))
                if(i%2==0):
                        sin+=loopTerm
                else:
                        sin-=loopTerm
        
        return sin


#Calculates the cosine of an angle
def cos(rad, digits=12, iterations=10):
        mpmath.mp.dps=digits
        radians=mpmath.mpf(getToDomain(rad))
        piC=piCalc(iterations, digits)
        cos=mpmath.mpf(0)
        for i in range(0, iterations):
                loopTerm=1
                for n in range(2*i):
                        loopTerm*=radians
                loopTerm=mpmath.mpf(loopTerm/factorial(2*i))
                if(i%2==0):
                        cos+=loopTerm
                else:
                        cos-=loopTerm
        
        return cos

#Calculates the tangent of an angle
def tan(rad, digits=12, iterations=20):
        mpmath.mp.dps=digits
        radians=mpmath.mpf(getToDomain(rad))
        tan=mpmath.mpf(sin(radians, digits, iterations)/cos(radians, digits, iterations))

        return tan

#Calculates the cosecant of an angle
def csc(rad, digits=12, iterations=20):
        return (mpmath.mpf(1/sin(rad, digits, iterations)))

#Calculates the secant of an angle
def sec(rad, digits=12, iterations=20):
        return (mpmath.mpf(1/cos(rad, digits, iterations)))

#Calculates the cotangent of an angle
def cot(rad, digits=12, iterations=20):
        return (mpmath.mpf(1/tan(rad, digits, iterations)))

#Calculates the exponential of a number (e to the power of the number)
def exp(a, digits=12, iterations=100):
        mpmath.mp.dps=digits
        ex=mpmath.mpf(0)
        x=mpmath.mpf(a)
        for i in range(iterations):
                ex+=mpmath.mpf(x**i/factorial(i))
        
        return ex 

#Calculates the natural logarith of a number using an improved method
def ln(a, digits=12, iterations=100):
        mpmath.mp.dps=digits
        ln=mpmath.mpf(a-1)
        for i in range(1, iterations+1):
                root=mpmath.mpf(a**(mpmath.mpf(1/(2**i))))
                term=mpmath.mpf(2/(1+root))
                ln=mpmath.mpf(ln*term)
        return ln

#Calculates a to the power of b
def power(a, b, digits=12, iterations=100):
        mpmath.mp.dps=digits
        p=mpmath.mpf(ln(a, digits, iterations)*b)

        return exp(p, digits, iterations)

# Calculates log b to the base a. Works for 0<a,b<1000.
def log(a, b, digits=12, iterations=300):
        return (mpmath.mpf(ln(b, digits, iterations)/ln(a, digits, iterations)))

# Calculates log to the base 10. Works for 0<a<1000.
def log10(a, digits=12, iterations=300):
        return (mpmath.mpf(ln(a, digits, iterations)/ln(10, digits, iterations)))

#Calculates the inverse of a number
def inverse(a, digits=12):
        mpmath.mp.dps=digits
        return(mpmath.mpf(1/a))

#Calculates the square of a number
def square(a, digits=12, iterations=100):
        mpmath.mp.dps=digits
        return mpmath.mpf(a)**2

#Calculates the square root of a number
def sqrt(a, digits=12, iterations=100):
        mpmath.mp.dps=digits
        return power(a, 0.5, digits, iterations)

#Calculates the cube of a number
def cube(a, digits=12, iterations=100):
        mpmath.mp.dps=digits
        return mpmath.mpf(a)**3

#Calculates the cube root of a number
def cbrt(a, digits=12, iterations=100):
        mpmath.mp.dps=digits
        athird=mpmath.mpf(1/3)
        return power(a, mpmath.mpf(athird), digits, iterations)
