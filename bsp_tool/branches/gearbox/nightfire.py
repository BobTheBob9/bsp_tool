# https://code.google.com/archive/p/jbn-bsp-lump-tools
import enum
from typing import List

from .. import base
from .. import shared
from ..id_software import quake
from ..valve import goldsrc


FILE_MAGIC = None

BSP_VERSION = 42

GAME_PATHS = {"James Bond 007: Nightfire": "James Bond 007 Nightfire"}

GAME_VERSIONS = {GAME_NAME: BSP_VERSION for GAME_NAME in GAME_PATHS}


class LUMP(enum.Enum):
    ENTITIES = 0
    PLANES = 1
    TEXTURES = 2
    MATERIALS = 3
    VERTICES = 4
    NORMALS = 5
    INDICES = 6
    VISIBILITY = 7
    NODES = 8
    FACES = 9
    LIGHTMAPS = 10
    LEAVES = 11
    MARK_SURFACES = 12
    MARK_BRUSHES = 13
    MODELS = 14
    BRUSHES = 15
    BRUSH_SIDES = 16
    TEXTURE_INFO = 17


LumpHeader = quake.LumpHeader


# classes for lumps, in alphabetical order:
class BrushSide(base.MappedArray):  # LUMP 16
    plane: int
    face: int  # changed from TextureInfo in Quake 2
    _mapping = ["plane", "face"]
    _format = "2i"


class Face(base.MappedArray):  # LUMP 9
    plane: int
    first_vertex: int
    num_vertices: int
    first_index: int
    num_indices: int
    flags: int
    texture: int
    material: int
    texture_scale: int
    unknown: int
    light_styles: int
    lightmap: int
    _mapping = ["plane", "first_vertex", "num_vertices", "first_index",
                "num_indices", "flags", "texture", "material", "texture_scale",
                "unknown", "light_styles", "lightmap"]
    _format = "5iI6i"


class Leaf(base.Struct):  # LUMP 11
    contents: int
    cluster: int
    bounds: List[List[float]]
    # bounds.mins: List[float]  # xyz
    # bounds.maxs: List[float]  # xyz
    first_mark_brush: int
    num_mark_brushes: int
    first_mark_face: int
    num_mark_faces: int
    __slots__ = ["contents", "cluster", "bounds",
                 "first_mark_brush", "num_mark_brushes", "first_mark_face", "num_mark_faces"]
    _format = "2i6f4i"
    _arrays = {"bounds": {"mins": [*"xyz"], "maxs": [*"xyz"]}}


class Model(base.Struct):  # LUMP 14
    bounds: List[List[float]]
    # bounds.mins: List[float]  # xyz
    # bounds.maxs: List[float]  # xyz
    unknown: List[int]  # doesn't align with quake or goldsrc lump sizes afaik
    first_leaf: int  # index to the first Leaf in this Model
    num_leaves: int  # number of leaves after first_leaf in this Model
    first_face: int  # index to the first Face in this Model
    num_faces: int  # number of faces after first_face in this Model
    __slots__ = ["bounds", "unknown", "first_leaf", "num_leaves", "first_face", "num_faces"]
    _format = "6f8i"
    _arrays = {"bounds": {"mins": [*"xyz"], "maxs": [*"xyz"]}, "unknown": 4}


class Node(base.Struct):  # LUMP 8
    # https://en.wikipedia.org/wiki/Half-space_(geometry)
    # NOTE: bounded by associated model
    # basic convex solid stuff
    plane: int
    children: List[int]  # +ve ClipNode, -1 outside model, -2 inside model
    bounds: List[List[float]]
    # bounds.mins: List[float]  # xyz
    # bounds.maxs: List[float]  # xyz
    __slots__ = ["plane", "children", "bounds"]
    _format = "3i6f"
    _arrays = {"children": ["front", "back"], "bounds": {"mins": [*"xyz"], "maxs": [*"xyz"]}}


class TextureInfo(base.Struct):  # LUMP 17
    u: List[float]
    v: List[float]
    __slots__ = ["u", "v"]
    _format = "8f"
    _arrays = {"u": [*"xyzw"], "v": [*"xyzw"]}


BASIC_LUMP_CLASSES = goldsrc.BASIC_LUMP_CLASSES.copy()
BASIC_LUMP_CLASSES.update({"INDICES": shared.UnsignedInts})

LUMP_CLASSES = goldsrc.LUMP_CLASSES.copy()
LUMP_CLASSES.update({"BRUSH_SIDES":  BrushSide,
                     "FACES":        Face,
                     "LEAVES":       Leaf,
                     "MODELS":       Model,
                     "NODES":        Node,
                     "TEXTURE_INFO": TextureInfo})

SPECIAL_LUMP_CLASSES = goldsrc.SPECIAL_LUMP_CLASSES.copy()


methods = [*goldsrc.methods]
