"""A library for .bsp file analysis & modification"""
__all__ = ["base", "branches", "load_bsp", "tools", "IdSoftBsp", "D3DBsp", "ValveBsp", "RespawnBsp"]
from types import ModuleType
from typing import Union

from . import base
from . import branches
from . import tools
from .id_software import IdSoftBsp
from .infinity_ward import D3DBsp
from .respawn import RespawnBsp
from .valve import ValveBsp


def load_bsp(filename: str, branch: Union[str, ModuleType]):
    if not filename.endswith(".bsp"):
        raise RuntimeError(f"{filename} is not a .bsp file!")
    with open(filename, "rb") as bsp_file:
        file_magic = bsp_file.read(4)
        if file_magic not in branches.by_magic:
            raise RuntimeError(f"{filename} is not from a known engine branch ({file_magic.decode()})")
    if branch.lower() == "unknown":  # guess .bsp format from version
        bsp_version = int.from_bytes(bsp_file.read(4), "little")
        if branch not in branches.by_version:
            raise NotImplementedError(f"{file_magic} version {bsp_version} is not supported")
            # you can avoid this error by forcing a branch:
            # - load_bsp("example.bsp", branches.valve.orange_box)
        branch = branches.by_version[bsp_version]
    else:  # look up branch by name
        if branch not in branches.by_name:
            raise NotImplementedError(f"{branch} .bsp format is not supported, yet.")
        branch = branches.by_name[branch]

    # create appropriate Bsp sub-class
    ...
    # this function should be attached to transitioning to creating .bsp files, rather than simply loading them.
    # beyond that, compiling could be interesting, particularly parellellised lightmap generation
    # (calculate per face texure, assemble & link afterwards)
