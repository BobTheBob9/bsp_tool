from __future__ import annotations
import os
import struct
from types import MethodType, ModuleType
from typing import Any, Dict, List


class Bsp:
    """Bsp base class"""
    bsp_version: int | (int, int) = 0  # .bsp format version
    associated_files: List[str]  # files in the folder of loaded file with similar names
    # TODO: include subfolder files (e.g. graphs/<mapname>.ain)
    branch: ModuleType  # soft copy of "branch script"
    bsp_file_size: int = 0  # size of .bsp in bytes
    endianness: str = "little"
    file_magic: bytes = b"XBSP"
    # NOTE: XBSP is not a real bsp variant! this is just a placeholder
    filename: str
    folder: str
    headers: Dict[str, Any]
    # ^ {"LUMP.name": LumpHeader}
    # NOTE: header type is self.branch.LumpHeader
    loading_errors: Dict[str, Exception]
    # ^ {"LUMP.name": Error("details")}

    def __init__(self, branch: ModuleType, filename: str = "untitled.bsp", autoload: bool = True):
        if not filename.lower().endswith(".bsp"):
            raise RuntimeError("Not a .bsp")
        filename = os.path.realpath(filename)
        self.folder, self.filename = os.path.split(filename)
        self.set_branch(branch)
        self.headers = dict()
        if autoload:
            if os.path.exists(filename):
                self._preload()
            else:
                print(f"{filename} not found, creating a new .bsp")
                self.headers = {L.name: self.branch.LumpHeader() for L in self.branch.LUMP}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

    def __repr__(self):
        branch_script = ".".join(self.branch.__name__.split(".")[-2:])
        if isinstance(self.bsp_version, tuple):
            major, minor = self.bsp_version
            version_number = f"{major}.{minor}"
        else:
            version_number = self.bsp_version
        version = f"({self.file_magic.decode('ascii', 'ignore')} version {version_number})"
        return f"<{self.__class__.__name__} '{self.filename}' {branch_script} {version}>"

    def lump_as_bytes(self, lump_name: str) -> bytes:
        """Converts the named (unversioned) lump back into bytes"""
        if not hasattr(self, lump_name):
            return b""  # lump is empty / deleted
        lump_entries = getattr(self, lump_name)
        all_mapped_lumps = {*self.branch.BASIC_LUMP_CLASSES,
                            *self.branch.LUMP_CLASSES,
                            *self.branch.SPECIAL_LUMP_CLASSES}
        # RawBspLump -> bytes
        if lump_name not in all_mapped_lumps or lump_name in self.loading_errors:
            return bytes(lump_entries)
        # BasicBspLump -> bytes
        if lump_name in self.branch.BASIC_LUMP_CLASSES:
            _format = self.branch.BASIC_LUMP_CLASSES[lump_name]._format
            raw_lump = struct.pack(f"{len(lump_entries)}{_format}", *lump_entries)
        # BspLump -> bytes
        elif lump_name in self.branch.LUMP_CLASSES:
            _format = self.branch.LUMP_CLASSES[lump_name]._format
            raw_lump = b"".join([struct.pack(_format, *x.flat()) for x in lump_entries])
        # SpecialLumpClass -> bytes
        elif lump_name in self.branch.SPECIAL_LUMP_CLASSES:
            raw_lump = lump_entries.as_bytes()
        return raw_lump

    def save_as(self, filename: str):
        """Expects outfile to be a file with write bytes capability"""
        raise NotImplementedError()
        # os.makedirs(os.path.dirname(os.path.realpath(filename)), exist_ok=True)
        # outfile = open(filename, "wb")
        # # try to preserve the original order of lumps
        # outfile.write(self.file_magic)
        # outfile.write(self.version.to_bytes(4, "little"))  # .bsp format version
        # for LUMP in self.branch.LUMP:
        #     pass  # calculate and write each header
        #     # adapting each header to bytes could be hard
        # # write the contents of each lump
        # outfile.write(b"0001") # map revision
        # # write contents of lumps

    def save(self):
        self.save_as(os.path.join(self.folder, self.filename))

    def set_branch(self, branch: ModuleType):
        """Calling .set_branch(...) on a loaded .bsp will not convert it!"""
        # branch is a "branch script" that has been imported into python
        # if writing your own "branch script", see branches/README.md for a guide
        # TODO: remove old methods first
        self.branch = branch
        # attach methods
        for method in getattr(branch, "methods", list()):
            method = MethodType(method, self)
            setattr(self, method.__name__, method)
        # could we also attach static methods? class methods?
