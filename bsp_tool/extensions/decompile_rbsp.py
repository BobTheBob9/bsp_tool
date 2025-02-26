from typing import List

from ..branches.vector import vec3


def triangle_for(plane: (vec3, float), scale: float = 64) -> List[vec3]:
    """returns a clockwise facing triangle on plane"""
    normal, distance = plane
    # NOTE: normal is assumed to be normalised
    non_parallel = vec3(**{"z" if abs(normal.z) != 1 else "y": -1})
    local_y = (non_parallel * normal).normalised()
    local_x = (local_y * normal).normalised()
    A = normal * distance
    B = A + local_x * scale
    C = A + local_y * scale
    return (A, B, C)


def fstr(x: float) -> str:
    """str(float) without trailing zeroes"""
    x = round(x, 2)
    if x % 1.0 == 0.0:
        return str(int(x))
    return str(x)


# NOTE: only TrenchBroom & J.A.C.K. seem to like Valve220
# -- J.A.C.K. can convert to other formats including .vmf
# TODO: why are all exported maps inverted?
# https://quakewiki.org/wiki/Quake_Map_Format
def decompile(bsp) -> List[str]:
    """Converts a Titanfall .bsp into a Valve 220 .map file"""
    out = ["// Game: Generic\n// Format: Valve\n",
           '// entity 0\n{\n"classname" "worldspawn"\n']
    first_brush_side = 0
    for i, brush in enumerate(bsp.CM_BRUSHES):
        out.append(f"// brush {i}" + "\n{\n")
        origin = -vec3(*brush.origin)  # inverted for some reason? prob bad math
        extents = vec3(*brush.extents)
        mins = origin - extents
        maxs = origin + extents
        planes = list()
        # ^ [(normal: vec3, distance: float)]
        # assemble base brushsides in order: +X -X +Y -Y +Z -Z
        for axis, min_, max_ in zip("xyz", mins, maxs):
            planes.append((vec3(**{axis: 1}), -max_))  # +ve axis
            planes.append((vec3(**{axis: -1}), min_))  # -ve axis
        # TODO: check order of generated brushsides lines up
        # TODO: pull any extra planes from CM_BRUSH_SIDE_PLANES if nessecary
        # -- unsure how / if they index the PLANES lump
        num_brush_sides = 6
        for j in range(num_brush_sides):
            tri = triangle_for(planes[j])
            j += first_brush_side
            # prop = bsp.CM_BRUSH_SIDE_PROPERTIES[j]
            tv = bsp.CM_BRUSH_SIDE_TEXTURE_VECTORS[j]
            tv_s = " ".join([" ".join(["[", *map(fstr, v), "]"]) for v in tv])
            tri_s = " ".join([" ".join(["(", *map(fstr, p), ")"]) for p in tri])
            # TODO: determine texture; using TrenchBroom default texture for now
            # -- current theory is that BrushSideProperties indexes TextureData, somehow
            out.append(" ".join([tri_s, "__TB_empty", tv_s, "0 1 1\n"]))
            # ^ "( A ) ( B ) ( C ) TEXTURE [ S ] [ T ] rotation scale_X scale_Y"  # valve 220 texture format
        first_brush_side += num_brush_sides
        out.append("}\n")
    out.append("}\n")
    # TODO: all other entities
    return out
