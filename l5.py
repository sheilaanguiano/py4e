
def computepay(h, r):
    h = float(hrs)
    r = float(rate)
    if h <= 40:
        return ( h * r )
    else: 
        base = 40 * r
        # print(base)
        extra_h = h - 40
        extra_r = r * 1.5
        # print(extra_h)
        # print(extra_r)
        return (base + extra_h * extra_r) 


hrs = input("Enter Hours:")
rate = input("Enter Rate:")



print("Pay", computepay( hrs, rate))