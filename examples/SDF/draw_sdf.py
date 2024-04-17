import pyLevelSet as pls

sf = pls.sphere(1) & pls.box(1.5)
cy = pls.cylinder(0.5)
sf -= cy.orient([1, 0, 0]) | cy.orient([0, 1, 0]) | cy.orient([0, 0, 1])
sf.grids(space=0.1).reset(False).save('sdf.stl', samples=90002)
sf.visualize()
