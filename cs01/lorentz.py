s = float(input("Enter the velocity (m/s): "))
c = 3*10**8
inv_lorentz_squared = 1 - (s**2/c**2)
inv_lorentz = inv_lorentz_squared**(1/2)
lorentz = 1 / inv_lorentz
print(f'The Lorentz factor at {s:.1f} m/s is {lorentz:.4f}')
