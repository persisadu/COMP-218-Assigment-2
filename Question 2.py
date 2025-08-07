def gcd_recursive(a,b):
   ### Compute and return the greatest common divisor (GCD) of a and b using the recursive Euclidean algorithm. Handles zeroo and negative inputs by converting to absolute values. ###

   a, b = abs(a), abs(b)
   if b ==0:
       return a 
   return gcd_recursive(b, a % b)

def main():
   pairs = [(48, 18), (12, 14), (270, 192), (0, 5), (-36, 24)]
   for x, y in pairs:
       result = gcd_recursive(x,y)
       print(f"GCD({x}, {y} = {result})")

if __name__ == "__main__":
    main()