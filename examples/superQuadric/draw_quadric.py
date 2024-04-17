import pyLevelSet as pl

f = pl.polysuperquadrics(xrad1=0.35, yrad1=0.75, zrad1=0.65, xrad2=0.25, yrad2=0.65, zrad2=0.5, epsilon_x=1.8, epsilon_y=1.2, epsilon_z=0.7).grids(space=0.05)
f.save('ellipsoid.stl', samples=10002, sparse=False)
f.visualize()
