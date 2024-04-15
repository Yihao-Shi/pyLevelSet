import sys
sys.path.append('/home/eleven/work/pyLevelSet')

import pyLevelSet as pl

f = pl.polysuperellipsoid(xrad1=0.005, yrad1=0.0025, zrad1=0.0025, epsilon_e=1., epsilon_n=1.).grids(space=0.00025)
f.save('ellipsoid.stl', samples=2502, sparse=False)
f.visualize()
