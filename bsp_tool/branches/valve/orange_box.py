# https://github.com/ValveSoftware/source-sdk-2013/blob/master/sp/src/public/bspfile.h
import enum
import io
import struct
from typing import List

from .. import base
from . import source


FILE_MAGIC = b"VBSP"

BSP_VERSION = 20

GAME_PATHS = {"Day of Defeat: Source": "day of defeat source/dod",
              "E.Y.E: Divine Cybermancy": "EYE Divine Cybermancy/EYE",
              "G-String": "G String/gstringv2",
              "Garry's Mod": "GarrysMod/garrysmod",
              "Half-Life 2: Episode 2": "half-life 2/ep2",
              "Half-Life 2 Update": "Half-Life 2 Update/hl2",
              "NEOTOKYO": "NEOTOKYO/neotokyosource",
              "Portal": "Portal/portal",
              "Team Fortress 2": "Team Fortress 2/tf"}

GAME_VERSIONS = {GAME_NAME: BSP_VERSION for GAME_NAME in GAME_PATHS}


class LUMP(enum.Enum):
    ENTITIES = 0
    PLANES = 1
    TEXTURE_DATA = 2
    VERTICES = 3
    VISIBILITY = 4
    NODES = 5
    TEXTURE_INFO = 6
    FACES = 7  # version 1
    LIGHTING = 8  # version 1
    OCCLUSION = 9  # version 2
    LEAVES = 10  # version 1
    FACE_IDS = 11  # TF2 branch, for mapping debug & detail prop seed
    EDGES = 12
    SURFEDGES = 13
    MODELS = 14
    WORLD_LIGHTS = 15
    LEAF_FACES = 16
    LEAF_BRUSHES = 17
    BRUSHES = 18
    BRUSH_SIDES = 19
    AREAS = 20
    AREA_PORTALS = 21
    UNUSED_22 = 22
    UNUSED_23 = 23
    UNUSED_24 = 24
    UNUSED_25 = 25
    DISPLACEMENT_INFO = 26
    ORIGINAL_FACES = 27
    PHYSICS_DISPLACEMENT = 28
    PHYSICS_COLLIDE = 29
    VERTEX_NORMALS = 30
    VERTEX_NORMAL_INDICES = 31
    DISPLACEMENT_LIGHTMAP_ALPHAS = 32  # deprecated / X360 ?
    DISPLACEMENT_VERTICES = 33
    DISPLACEMENT_LIGHTMAP_SAMPLE_POSITIONS = 34
    GAME_LUMP = 35
    LEAF_WATER_DATA = 36
    PRIMITIVES = 37
    PRIMITIVE_VERTICES = 38  # deprecated / X360 ?
    PRIMITIVE_INDICES = 39
    PAKFILE = 40
    CLIP_PORTAL_VERTICES = 41
    CUBEMAPS = 42
    TEXTURE_DATA_STRING_DATA = 43
    TEXTURE_DATA_STRING_TABLE = 44
    OVERLAYS = 45
    LEAF_MIN_DIST_TO_WATER = 46
    FACE_MACRO_TEXTURE_INFO = 47
    DISPLACEMENT_TRIS = 48
    PHYSICS_COLLIDE_SURFACE = 49  # deprecated / X360 ?
    WATER_OVERLAYS = 50  # deprecated / X360 ?
    LEAF_AMBIENT_INDEX_HDR = 51
    LEAF_AMBIENT_INDEX = 52
    LIGHTING_HDR = 53  # version 1
    WORLD_LIGHTS_HDR = 54
    LEAF_AMBIENT_LIGHTING_HDR = 55  # version 1
    LEAF_AMBIENT_LIGHTING = 56  # version 1
    XZIP_PAKFILE = 57  # deprecated / X360 ?
    FACES_HDR = 58  # version 1
    MAP_FLAGS = 59
    OVERLAY_FADES = 60
    UNUSED_61 = 61
    UNUSED_62 = 62
    UNUSED_63 = 63


LumpHeader = source.LumpHeader

# a rough map of the relationships between lumps:

#                     /-> SurfEdge -> Edge -> Vertex
# Leaf -> Node -> Face -> Plane
#                     \-> DisplacementInfo -> DisplacementVertex

# ClipPortalVertices are AreaPortal geometry [citation neeeded]


# classes for each lump, in alphabetical order:
class Leaf(source.Leaf):  # LUMP 10  (v1)
    """Endpoint of a vis tree branch, a pocket of Faces"""
    contents: int  # Contents flags
    cluster: int   # index of this Leaf's viscluster (leaf group in VISIBILITY lump)
    area_flags: int  # area & flags bitfield (short area:9; short flags:7;)
    # why was this done when the struct is padded by one short anyway?
    mins: List[float]  # bounding box minimums along XYZ axes
    maxs: List[float]  # bounding box maximums along XYZ axes
    first_leaf_face: int   # index of first LeafFace
    num_leaf_faces: int    # number of LeafFaces
    first_leaf_brush: int  # index of first LeafBrush
    num_leaf_brushes: int  # number of LeafBrushes
    leaf_water_data_id: int  # -1 if this leaf isn't submerged
    padding: int  # should be empty
    __slots__ = ["contents", "cluster", "area_flags", "mins", "maxs",
                 "first_leaf_face", "num_leaf_faces", "first_leaf_brush",
                 "num_leaf_brushes", "leaf_water_data_id", "padding"]
    _format = "i8h4H2h"
    _arrays = {"mins": [*"xyz"], "maxs": [*"xyz"]}


# classes for special lumps, in alphabetical order:
class PhysicsDisplacement(list):  # LUMP 28
    def __init__(self, raw_lump: bytes):
        lump = io.BytesIO(raw_lump)
        count = int.from_bytes(lump.read(2), "little")
        data_sizes = list(*struct.unpack(f"{count}H", lump.read(count * 2)))
        physics_data = list()
        for size in data_sizes:
            physics_data.append(lump.read(size))
        super().__init__(physics_data)

    def as_bytes(self) -> bytes:
        count = len(self).to_bytes(2, "little")
        sizes = map(lambda s: s.to_bytes(2, "little"), [len(d) for d in self])
        return b"".join(count, *sizes, *self)


class StaticPropv10(base.Struct):  # sprp GAME LUMP (LUMP 35)
    origin: List[float]  # origin.xyz
    angles: List[float]  # origin.yzx  QAngle; Z0 = East
    model_name: int  # index into AME_LUMP.sprp.model_names
    first_leaf: int  # index into Leaf lump
    num_leafs: int  # number of Leafs after first_leaf this StaticPropv10 is in
    solid_mode: int  # collision flags enum
    skin: int  # index of this StaticProp's skin in the .mdl
    fade_distance: List[float]  # min & max distances to fade out
    lighting_origin: List[float]  # xyz position to sample lighting from
    forced_fade_scale: float  # relative to pixels used to render on-screen?
    dx_level: List[int]  # supported directX level, will not render depending on settings
    flags: int  # other flags
    lightmap: List[int]  # dimensions of this StaticProp's lightmap (GAME_LUMP.static prop lighting?)
    __slots__ = ["origin", "angles", "name_index", "first_leaf", "num_leafs",
                 "solid_mode", "skin", "fade_distance", "lighting_origin",
                 "forced_fade_scale", "dx_level", "flags", "lightmap"]
    _format = "6f3HBi6f2Hi2H"
    _arrays = {"origin": [*"xyz"], "angles": [*"yzx"], "fade_distance": ["min", "max"],
               "lighting_origin": [*"xyz"], "dx_level": ["min", "max"],
               "lightmap": ["width", "height"]}


# {"LUMP_NAME": {version: LumpClass}}
BASIC_LUMP_CLASSES = source.BASIC_LUMP_CLASSES.copy()

LUMP_CLASSES = source.LUMP_CLASSES.copy()
LUMP_CLASSES.pop("LEAF_AMBIENT_LIGHTING")
LUMP_CLASSES.pop("LEAF_AMBIENT_LIGHTING_HDR")
LUMP_CLASSES["LEAVES"].update({1: Leaf})

SPECIAL_LUMP_CLASSES = source.SPECIAL_LUMP_CLASSES.copy()


GAME_LUMP_HEADER = source.GAME_LUMP_HEADER

# {"lump": {version: SpecialLumpClass}}
GAME_LUMP_CLASSES = source.GAME_LUMP_CLASSES.copy()
GAME_LUMP_CLASSES["sprp"].update({7: lambda raw_lump: source.GameLump_SPRP(raw_lump, StaticPropv10),  # 7*
                                 10: lambda raw_lump: source.GameLump_SPRP(raw_lump, StaticPropv10)})


methods = [*source.methods]
