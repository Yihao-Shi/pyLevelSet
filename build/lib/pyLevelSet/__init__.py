# Copyright (c) 2023, multiscale geomechanics lab, Zhejiang University
# This file is from the GeoTaichi project, released under the GNU General Public License v3.0

__author__ = "Shi-Yihao, Guo-Ning"
__version__ = "0.2.0"
__license__ = "GNU License"


from .BasicShape import pointcloud, arbitrarily, polyhedron, surfacefunction, polysuperquadrics, polysuperellipsoid

from .SDFs2D import (
    circle, line, slab,
    rectangle, rounded_rectangle, equilateral_triangle,
    hexagon, rounded_x, cross, polygon
)

from .SDFs3D import (
    sphere, plane, slab, 
    box, rounded_box, box_frame, torus, capped_torus,
    link, hexagonal_prism, capsule, cylinder, capped_cylinder, rounded_cylinder,
    cone, capped_cone, rounded_cone, revolved_vesica, octahedron,
    pyramid, rhombus, tetrahedron, dodecahedron, icosahedron
)

from .text import (
    image,
    text,
)

from .ease import (
    linear,
    in_quad, out_quad, in_out_quad,
    in_cubic, out_cubic, in_out_cubic,
    in_quart, out_quart, in_out_quart,
    in_quint, out_quint, in_out_quint,
    in_sine, out_sine, in_out_sine,
    in_expo, out_expo, in_out_expo,
    in_circ, out_circ, in_out_circ,
    in_elastic, out_elastic, in_out_elastic,
    in_back, out_back, in_out_back,
    in_bounce, out_bounce, in_out_bounce,
    in_square, out_square, in_out_square,
)

print('# =================================================================== #')
print('#', "".center(67), '#')
print('#', "Welcome to pyLevelSet Version 0.1 ".center(67), '#')
print('#', "".center(67), '#')
print('#', "Description: A Level-set particles generator".ljust(67), '#')
print('#', "Author: Yihao Shi".ljust(67), '#')
print('#', "Institute: Zhejiang University".ljust(67), '#')
print('#', "Release: April 5, 2024".ljust(67), '#')
print('#', "Email: syh-1999@outlook.com".ljust(67), '#')
print('#', "".center(67), '#')
print('# =================================================================== #', '\n')