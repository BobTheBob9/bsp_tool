"""These tests cannot fail, but they will provide warnings for unused LumpClasses"""
import inspect
import struct
from types import ModuleType
from typing import List
import warnings

import pytest

from bsp_tool import branches


# TODO: Use "./tests/maps/*.bsp" to check each LumpClass matches byte for byte


def LumpClasses_of(module: ModuleType) -> List[object]:
    attrs = dir(module)
    for a in attrs:
        LumpClass = getattr(module, a)
        if inspect.isclass(LumpClass):
            if issubclass(LumpClass, (branches.base.Struct, branches.base.MappedArray)):
                yield LumpClass


def verify(LumpClass):
    """checks LumpClass for anything irregular"""
    # TODO: verify __slots__, _format, _arrays & _mapping line up correctly
    # -- all LumpClasses must coherently translate to and from bytes
    # -- no skipped bytes! (single byte alignment gets wierd)
    # -- incomplete / mismatched / outdated type-hints should also be checked
    # -- this may require scanning comments for "deep" type-hints `# attr.sub: type  # desc`
    # Struct
    if isinstance(LumpClass, branches.base.Struct):
        if not hasattr(LumpClass, "__slots__"):
            raise NotImplementedError(f"{LumpClass.__name__} has no .__slots__!")
        # TODO: verify names in type annotations match __slots__
        if hasattr(LumpClass, "_mapping"):
            warnings.warn(UserWarning(f"{LumpClass.__name__} should not be using ._mapping!"))
        if not hasattr(LumpClass, "_arrays"):
            warnings.warn(UserWarning(f"{LumpClass.__name__} should be a base.MappedArray"))
    # MappedArray
    elif isinstance(LumpClass, branches.base.MappedArray):
        if hasattr(LumpClass, "__slots__"):
            warnings.warn(UserWarning(f"{LumpClass.__name__} should not be using .__slots__!"))
        if hasattr(LumpClass, "_arrays"):
            warnings.warn(UserWarning(f"{LumpClass.__name__} should not be using ._arrays!"))
        if not hasattr(LumpClass, "_mapping"):
            raise NotImplementedError(f"{LumpClass.__name__} has no ._mapping!")
        # TODO: verify names in type annotations match _mapping
    # Any
    if not hasattr(LumpClass, "_format"):
        raise NotImplementedError(f"{LumpClass.__name__} has no ._format!")
    assert struct.calcsize(LumpClass._format) > 0, f"{LumpClass.__name__}._format is invalid!"
    LumpClass()  # try __init__


# IdTech + IW + GoldSrc Engines (no lump versions)
basic_branch_scripts = [*branches.id_software.scripts,
                        *branches.infinity_ward.scripts,
                        branches.ion_storm.daikatana,
                        *branches.gearbox.scripts,
                        *branches.raven.scripts,
                        *branches.ritual.scripts,
                        branches.valve.goldsrc]


@pytest.mark.parametrize("branch_script", basic_branch_scripts)
def test_basic_branch_script(branch_script):
    used_LumpClasses = set(branch_script.LUMP_CLASSES.values())
    # ^ {"LUMP": LumpClass}
    # TODO: verify __slots__, _format, _arrays & _mapping line up correctly
    # -- this includes missing bytes (since single byte alignment gets wierd)
    # -- also type hints
    used_LumpClasses.add(branch_script.LumpHeader)
    unused_LumpClasses = set(LumpClasses_of(branch_script)).difference(used_LumpClasses)
    # TODO: trace what happens to imported LumpClasses
    # -- do they count as unused, because they are defined elsewhere?
    if len(unused_LumpClasses) > 0:
        warning_text = "\n".join(["Unused LumpClasses in branch script:",
                                  *[lc.__name__ for lc in unused_LumpClasses]])
        warnings.warn(UserWarning(warning_text))
    incorrect_lump_classes = dict()
    for LumpClass in used_LumpClasses:
        try:
            verify(LumpClass)
        except Exception as exc:
            incorrect_lump_classes[LumpClass.__name__] = exc
    assert incorrect_lump_classes == dict(), "some LumpClasses failed to __init__"


# Source + Titanfall Engines (lump versions)
branch_scripts = [*branches.arkane.scripts,
                  *branches.nexon.scripts,
                  *branches.respawn.scripts,
                  branches.troika.vampire,
                  *[s for s in branches.valve.scripts if (s is not branches.valve.goldsrc)]]


@pytest.mark.parametrize("branch_script", branch_scripts)
def test_branch_script(branch_script):
    """Versioned lump headers & Game Lumps"""
    used_LumpClasses = {branch_script.LumpHeader}
    for version_dict in branch_script.LUMP_CLASSES.values():
        # ^ {"LUMP": {version: LumpClass}}
        used_LumpClasses.update(version_dict.values())
    # NOTE: respawn.titanfall.Grid.from_bytes (classmethod) is used as a SpecialLumpClass
    # TODO: SpecialLumpClasses often consume child classes defined in the same script
    # need to somehow decode `GAME_LUMP_CLASSES = {"sprp": {4: lambda raw_lump: GameLump_SPRP(raw_lump, StaticPropv4)}}`
    # -- inspect + regex can pull the childclass passed to SpecialLumpClass.__init__, but it's far from ideal
    # -- all GameLumpClasses seem to do this, should we treat them differently?
    # -- e.g. GAME_LUMP_CLASSES = {"sprp": {4: (GameLump_SPRP, StaticPropv4)}}
    # -- -->  SpecialLumpClass, *child_classes = branch.GAME_LUMP_CLASSES[_id][version]
    # -- -->  SpecialLumpClass(raw_lump, *child_classes)
    # TODO: Identify all other cases where a lump is broken down into SpecialLumpClass & children
    # e.g. quake MipTextures
    if hasattr(branch_script, "GAME_LUMP_HEADER"):
        used_LumpClasses.add(branch_script.GAME_LUMP_HEADER)
    unused_LumpClasses = set(LumpClasses_of(branch_script)).difference(used_LumpClasses)
    unused_LumpClasses = set(filter(lambda lc: not lc.__name__.startswith("StaticProp"), unused_LumpClasses))
    # HACK: assume all StaticProp* classes are used by GAME_LUMP_CLASSES
    if len(unused_LumpClasses) > 0:
        warning_text = "\n".join(["Unused LumpClasses in branch script:", *[lc.__name__ for lc in unused_LumpClasses]])
        warnings.warn(UserWarning(warning_text))
    incorrect_lump_classes = dict()
    for LumpClass in used_LumpClasses:
        try:
            verify(LumpClass)
        except Exception as exc:
            incorrect_lump_classes[LumpClass.__name__] = exc
    assert incorrect_lump_classes == dict(), "some LumpClasses failed to __init__"


# TODO: use tests/maplist.py to look at headers to ensure UNUSED_* / UNKNOWN_* lumps are correctly marked
# -- looking for unmapped lump versions in ValveBsp & RespawnBsp would be nice too
