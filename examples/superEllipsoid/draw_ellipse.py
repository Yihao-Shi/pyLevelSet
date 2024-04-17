import pyLevelSet as pl

f = pl.polysuperellipsoid(xrad1=0.5, yrad1=0.25, zrad1=0.75, xrad2=0.25, yrad2=0.75, zrad2=0.5, epsilon_e=1.5, epsilon_n=1.5).grids(space=0.05)
f.save('ellipsoid.stl', samples=2502, sparse=False)
f.visualize()
