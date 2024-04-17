import pyLevelSet as pl

f = pl.polyhedron(file='/home/eleven/work/pyLevelSet/assets/sand.stl').grids(space=5)
f.save('sand.stl')
f.visualize()
