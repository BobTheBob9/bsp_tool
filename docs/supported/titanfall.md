# Titanfall Series
## Developers: Respawn Entertainment & NEXON

| BspClass | Bsp version | Game | Branch script | Supported lumps | Unused lumps | Coverage |
| -------: | ----------: | ---- | ------------- | --------------: | -----------: | :------- |
| [`RespawnBsp`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/bsp_tool/respawn.py#L148) | 29 | Titanfall | [`respawn.titanfall`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py) | 62 / 72 | 56 | 68.78% |
| [`RespawnBsp`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/bsp_tool/respawn.py#L148) | 29 | Titanfall: Online | [`respawn.titanfall`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py) | 62 / 72 | 56 | 68.78% |
| [`RespawnBsp`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/bsp_tool/respawn.py#L148) | 36 | Titanfall 2 Tech Test | [`respawn.titanfall2`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall2.py) | 64 / 76 | 52 | 66.55% |
| [`RespawnBsp`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/bsp_tool/respawn.py#L148) | 37 | Titanfall 2 | [`respawn.titanfall2`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall2.py) | 64 / 76 | 52 | 66.55% |


### References
 * [Valve Developer Wiki](https://developer.valvesoftware.com/wiki/Source_BSP_File_Format/Game-Specific#Titanfall)
 * [McSimp's Titanfall Map Exporter Tool](https://raw.githubusercontent.com/Wanty5883/Titanfall2/master/tools/TitanfallMapExporter.py)
   - by [Icepick](https://github.com/Titanfall-Mods/Titanfall-2-Icepick) contributor [McSimp](https://github.com/McSimp)
 * [Legion](https://github.com/dtzxporter/Legion/)


### Extracting `.bsp`s
Titanfall Engine `.bsp`, `.bsp_lump` & `.ent` are stored in `.vpk` files.
Extracting these files to work on them requires Titanfall Engine specific tools:

Once you have chosen your [extraction tool](Extraction-tools):
 * Locate the `.vpk`s for the game you want to work with (game must be installed)
   - `Titanfall/vpk/`
   - `Titanfall2/vpk/`
   - `Apex Legends/vpk/`
 * Open the `*.bsp.pak000_dir.vpk` for the map you want to load
   - Titanfall 2 map names can be found here: [NoSkill Modding Wiki](https://noskill.gitbook.io/titanfall2/documentation/file-location/vpk-file-names)
   - Lobbies are stored in `mp_common.bsp.pak000_dir.vpk`
 * Extract the `.bsp`, `.ent`s & `.bsp_lumps` from the `maps/` folder to someplace you'll remember
   - each `.vpk` holds assets for one `.bsp` (textures and models are stored elsewhere)


### Extraction Tools
 * [Titanfall VPKTool3.4 Portable](https://github.com/Wanty5883/Titanfall2/blob/master/tools/Titanfall_VPKTool3.4_Portable.zip) (GUI only)
   - by `Cra0kalo` (currently Closed Source) **recommended**
 * [TitanfallVPKTool](https://github.com/p0358/TitanfallVPKTool) (GUI & CLI)
   - by `P0358`
 * [RSPNVPK](https://github.com/squidgyberries/RSPNVPK) (CLI only)
   - Fork of `MrSteyk`'s Tool
 * [UnoVPKTool](https://github.com/Unordinal/UnoVPKTool) (CLI only)
   - by `Unordinal`

> NOTE: Apex's `GAME_LUMP` lump version should be the same as the version of the `.bsp` it is in


## Supported Lumps
| Lump index | Hex index | Bsp version | Lump name | Lump version | LumpClass | Coverage |
| ---------: | --------: | ----------: | --------- | -----------: | --------- | :------- |
| 0 | 0000 | 29 | `ENTITIES` | 0 | [`shared.Entities`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L43) | 100% |
| 1 | 0001 | 29 | `PLANES` | 1 | [`respawn.titanfall.Plane`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L381) | 100% |
| 2 | 0002 | 29 | `TEXTURE_DATA` | 1 | [`respawn.titanfall.TextureData`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L438) | 100% |
| 3 | 0003 | 29 | `VERTICES` | 0 | [`id_software.quake.Vertex`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/id_software/quake.py#L238) | 100% |
| 4 | 0004 | 29 | `UNUSED_4` | 0 |  | 0% |
| 4 | 0004 | 37 | `LIGHTPROBE_PARENT_INFOS` | 0 |  | 0% |
| 5 | 0005 | 29 | `UNUSED_5` | 0 |  | 0% |
| 5 | 0005 | 37 | `SHADOW_ENVIRONMENTS` | 0 | [`respawn.titanfall2.ShadowEnvironment`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall2.py#L238) | 40% |
| 6 | 0006 | 29 | `UNUSED_6` | 0 |  | 0% |
| 6 | 0006 | 37 | `LIGHTPROBE_BSP_NODES` | 0 |  | 0% |
| 7 | 0007 | 29 | `UNUSED_7` | 0 |  | 0% |
| 7 | 0007 | 37 | `LIGHTPROBE_BSP_REF_IDS` | 0 |  | 0% |
| 8 | 0008 | 29 | `UNUSED_8` | 0 |  | 0% |
| 9 | 0009 | 29 | `UNUSED_9` | 0 |  | 0% |
| 10 | 000A | 29 | `UNUSED_10` | 0 |  | 0% |
| 11 | 000B | 29 | `UNUSED_11` | 0 |  | 0% |
| 12 | 000C | 29 | `UNUSED_12` | 0 |  | 0% |
| 13 | 000D | 29 | `UNUSED_13` | 0 |  | 0% |
| 14 | 000E | 29 | `MODELS` | 0 | [`respawn.titanfall.Model`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L349) | 100% |
| 15 | 000F | 29 | `UNUSED_15` | 0 |  | 0% |
| 16 | 0010 | 29 | `UNUSED_16` | 0 |  | 0% |
| 17 | 0011 | 29 | `UNUSED_17` | 0 |  | 0% |
| 18 | 0012 | 29 | `UNUSED_18` | 0 |  | 0% |
| 19 | 0013 | 29 | `UNUSED_19` | 0 |  | 0% |
| 20 | 0014 | 29 | `UNUSED_20` | 0 |  | 0% |
| 21 | 0015 | 29 | `UNUSED_21` | 0 |  | 0% |
| 22 | 0016 | 29 | `UNUSED_22` | 0 |  | 0% |
| 23 | 0017 | 29 | `UNUSED_23` | 0 |  | 0% |
| 24 | 0018 | 29 | `ENTITY_PARTITIONS` | 0 | [`respawn.titanfall.EntityPartitions`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L543) | 100% |
| 25 | 0019 | 29 | `UNUSED_25` | 0 |  | 0% |
| 26 | 001A | 29 | `UNUSED_26` | 0 |  | 0% |
| 27 | 001B | 29 | `UNUSED_27` | 0 |  | 0% |
| 28 | 001C | 29 | `UNUSED_28` | 0 |  | 0% |
| 29 | 001D | 29 | `PHYSICS_COLLIDE` | 0 | [`physics.CollideLump`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/physics.py#L18) | 90% |
| 30 | 001E | 29 | `VERTEX_NORMALS` | 0 | [`id_software.quake.Vertex`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/id_software/quake.py#L238) | 100% |
| 31 | 001F | 29 | `UNUSED_31` | 0 |  | 0% |
| 32 | 0020 | 29 | `UNUSED_32` | 0 |  | 0% |
| 33 | 0021 | 29 | `UNUSED_33` | 0 |  | 0% |
| 34 | 0022 | 29 | `UNUSED_34` | 0 |  | 0% |
| 35 | 0023 | 29 | `GAME_LUMP` | - | [`lumps.GameLump`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/lumps/__init__.py#L319) | 90% |
| 35 | 0023 | 29 | `GAME_LUMP.sprp` | - | [`respawn.titanfall.GameLump_SPRP`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L552) | 60% |
| 35 | 0023 | 29 | `GAME_LUMP.sprp.props` | 12 | [`respawn.titanfall.StaticPropv12`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L598) | 94% |
| 35 | 0023 | 37 | `GAME_LUMP.sprp` | - | [`respawn.titanfall2.GameLump_SPRP`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall2.py#L252) | 40% |
| 35 | 0023 | 37 | `GAME_LUMP.sprp.props` | 13 | [`respawn.titanfall2.StaticPropv13`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall2.py#L286) | 92% |
| 36 | 0024 | 29 | `LEAF_WATER_DATA` | 1 | [`valve.source.LeafWaterData`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/valve/source.py#L460) | 100% |
| 37 | 0025 | 29 | `UNUSED_37` | 0 |  | 0% |
| 38 | 0026 | 29 | `UNUSED_38` | 0 |  | 0% |
| 39 | 0027 | 29 | `UNUSED_39` | 0 |  | 0% |
| 40 | 0028 | 29 | `PAKFILE` | 0 | [`shared.PakFile`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L121) | 100% |
| 41 | 0029 | 29 | `UNUSED_41` | 0 |  | 0% |
| 42 | 002A | 29 | `CUBEMAPS` | 0 | [`respawn.titanfall.Cubemap`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L260) | 50% |
| 43 | 002B | 29 | `TEXTURE_DATA_STRING_DATA` | 0 | [`shared.TextureDataStringData`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L132) | 100% |
| 44 | 002C | 29 | `TEXTURE_DATA_STRING_TABLE` | 0 | [`shared.UnsignedInts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L34) | 100% |
| 45 | 002D | 29 | `UNUSED_45` | 0 |  | 0% |
| 46 | 002E | 29 | `UNUSED_46` | 0 |  | 0% |
| 47 | 002F | 29 | `UNUSED_47` | 0 |  | 0% |
| 48 | 0030 | 29 | `UNUSED_48` | 0 |  | 0% |
| 49 | 0031 | 29 | `UNUSED_49` | 0 |  | 0% |
| 50 | 0032 | 29 | `UNUSED_50` | 0 |  | 0% |
| 51 | 0033 | 29 | `UNUSED_51` | 0 |  | 0% |
| 52 | 0034 | 29 | `UNUSED_52` | 0 |  | 0% |
| 53 | 0035 | 29 | `UNUSED_53` | 0 |  | 0% |
| 54 | 0036 | 29 | `WORLD_LIGHTS` | 1 | [`respawn.titanfall.WorldLight`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L473) | 50% |
| 54 | 0036 | 37 | `WORLD_LIGHTS` | 2 | [`respawn.titanfall2.WorldLightv2`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall2.py#L221) | 50% |
| 54 | 0036 | 37 | `WORLD_LIGHTS` | 3 | [`respawn.titanfall2.WorldLightv3`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall2.py#L228) | 50% |
| 55 | 0037 | 29 | `UNUSED_55` | 0 |  | 0% |
| 55 | 0037 | 37 | `WORLD_LIGHT_PARENT_INFOS` | 0 |  | 0% |
| 56 | 0038 | 29 | `UNUSED_56` | 0 |  | 0% |
| 57 | 0039 | 29 | `UNUSED_57` | 0 |  | 0% |
| 58 | 003A | 29 | `UNUSED_58` | 0 |  | 0% |
| 59 | 003B | 29 | `UNUSED_59` | 0 |  | 0% |
| 60 | 003C | 29 | `UNUSED_60` | 0 |  | 0% |
| 61 | 003D | 29 | `UNUSED_61` | 0 |  | 0% |
| 62 | 003E | 29 | `PHYSICS_LEVEL` | 0 |  | 0% |
| 63 | 003F | 29 | `UNUSED_63` | 0 |  | 0% |
| 64 | 0040 | 29 | `UNUSED_64` | 0 |  | 0% |
| 65 | 0041 | 29 | `UNUSED_65` | 0 |  | 0% |
| 66 | 0042 | 29 | `TRICOLL_TRIANGLES` | 2 | [`shared.UnsignedInts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L34) | 100% |
| 67 | 0043 | 29 | `UNUSED_67` | 0 |  | 0% |
| 68 | 0044 | 29 | `TRICOLL_NODES` | 1 | [`respawn.titanfall.TricollNode`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L467) | 0% |
| 69 | 0045 | 29 | `TRICOLL_HEADERS` | 1 | [`respawn.titanfall.TricollHeader`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L459) | 0% |
| 70 | 0046 | 29 | `PHYSICS_TRIANGLES` | 0 |  | 0% |
| 71 | 0047 | 29 | `VERTEX_UNLIT` | 0 | [`respawn.titanfall.VertexUnlit`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L517) | 75% |
| 72 | 0048 | 29 | `VERTEX_LIT_FLAT` | 1 | [`respawn.titanfall.VertexLitFlat`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L506) | 75% |
| 73 | 0049 | 29 | `VERTEX_LIT_BUMP` | 1 | [`respawn.titanfall.VertexLitBump`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L490) | 75% |
| 74 | 004A | 29 | `VERTEX_UNLIT_TS` | 0 | [`respawn.titanfall.VertexUnlitTS`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L528) | 75% |
| 75 | 004B | 29 | `VERTEX_BLINN_PHONG` | 0 | [`respawn.titanfall.VertexBlinnPhong`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L481) | 66% |
| 76 | 004C | 29 | `VERTEX_RESERVED_5` | 0 |  | 0% |
| 77 | 004D | 29 | `VERTEX_RESERVED_6` | 0 |  | 0% |
| 78 | 004E | 29 | `VERTEX_RESERVED_7` | 0 |  | 0% |
| 79 | 004F | 29 | `MESH_INDICES` | 0 | [`shared.UnsignedShorts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L38) | 100% |
| 80 | 0050 | 29 | `MESHES` | 0 | [`respawn.titanfall.Mesh`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L312) | 85% |
| 81 | 0051 | 29 | `MESH_BOUNDS` | 0 | [`respawn.titanfall.MeshBounds`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L328) | 75% |
| 82 | 0052 | 29 | `MATERIAL_SORT` | 0 | [`respawn.titanfall.MaterialSort`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L302) | 80% |
| 83 | 0053 | 29 | `LIGHTMAP_HEADERS` | 1 | [`respawn.titanfall.LightmapHeader`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L285) | 100% |
| 84 | 0054 | 29 | `UNUSED_84` | 0 |  | 0% |
| 85 | 0055 | 29 | `CM_GRID` | 0 | [`base.from_bytes`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/base.py#L132) | 90% |
| 86 | 0056 | 29 | `CM_GRID_CELLS` | 0 | [`shared.UnsignedInts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L34) | 100% |
| 87 | 0057 | 29 | `CM_GEO_SETS` | 0 | [`respawn.titanfall.GeoSet`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L268) | 0% |
| 88 | 0058 | 29 | `CM_GEO_SET_BOUNDS` | 0 | [`respawn.titanfall.Bounds`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L227) | 50% |
| 89 | 0059 | 29 | `CM_PRIMITIVES` | 0 | [`respawn.titanfall.Primitive`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L411) | 100% |
| 90 | 005A | 29 | `CM_PRIMITIVE_BOUNDS` | 0 | [`respawn.titanfall.Bounds`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L227) | 50% |
| 91 | 005B | 29 | `CM_UNIQUE_CONTENTS` | 0 | [`shared.UnsignedInts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L34) | 100% |
| 92 | 005C | 29 | `CM_BRUSHES` | 0 | [`respawn.titanfall.Brush`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L238) | 75% |
| 93 | 005D | 29 | `CM_BRUSH_SIDE_PLANE_OFFSETS` | 0 | [`shared.UnsignedShorts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L38) | 100% |
| 94 | 005E | 29 | `CM_BRUSH_SIDE_PROPS` | 0 | [`shared.UnsignedShorts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L38) | 100% |
| 95 | 005F | 29 | `CM_BRUSH_TEX_VECS` | 0 | [`respawn.titanfall.TextureVector`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L451) | 100% |
| 96 | 0060 | 29 | `TRICOLL_BEVEL_STARTS` | 0 | [`shared.UnsignedShorts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L38) | 100% |
| 97 | 0061 | 29 | `TRICOLL_BEVEL_INDICES` | 0 | [`shared.UnsignedInts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L34) | 100% |
| 98 | 0062 | 29 | `LIGHTMAP_DATA_SKY` | 0 | [`extensions.lightmaps.save_rbsp_r1`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/bsp_tool/extensions/lightmaps.py#L113) | 100% |
| 98 | 0062 | 37 | `LIGHTMAP_DATA_SKY` | 0 | [`extensions.lightmaps.save_rbsp_r2`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/bsp_tool/extensions/lightmaps.py#L144) | 100% |
| 99 | 0063 | 29 | `CSM_AABB_NODES` | 0 | [`respawn.titanfall.Node`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L360) | 50% |
| 100 | 0064 | 29 | `CSM_OBJ_REFERENCES` | 0 | [`shared.UnsignedShorts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L38) | 100% |
| 101 | 0065 | 29 | `LIGHTPROBES` | 0 |  | 0% |
| 102 | 0066 | 29 | `STATIC_PROP_LIGHTPROBE_INDICES` | 0 |  | 0% |
| 103 | 0067 | 29 | `LIGHTPROBE_TREE` | 0 |  | 0% |
| 104 | 0068 | 29 | `LIGHTPROBE_REFERENCES` | 0 | [`respawn.titanfall.LightProbeRef`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L294) | 100% |
| 104 | 0068 | 37 | `LIGHTPROBE_REFERENCES` | 0 | [`respawn.titanfall2.LightProbeRef`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall2.py#L212) | 66% |
| 105 | 0069 | 29 | `LIGHTMAP_DATA_REAL_TIME_LIGHTS` | 0 | [`extensions.lightmaps.save_rbsp_r1`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/bsp_tool/extensions/lightmaps.py#L113) | 100% |
| 105 | 0069 | 37 | `LIGHTMAP_DATA_REAL_TIME_LIGHTS` | 0 | [`extensions.lightmaps.save_rbsp_r2`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/bsp_tool/extensions/lightmaps.py#L144) | 100% |
| 106 | 006A | 29 | `CELL_BSP_NODES` | 0 |  | 0% |
| 107 | 006B | 29 | `CELLS` | 0 | [`respawn.titanfall.Cell`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L248) | 100% |
| 108 | 006C | 29 | `PORTALS` | 0 | [`respawn.titanfall.Portal`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L389) | 50% |
| 109 | 006D | 29 | `PORTAL_VERTICES` | 0 | [`id_software.quake.Vertex`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/id_software/quake.py#L238) | 100% |
| 110 | 006E | 29 | `PORTAL_EDGES` | 0 | [`id_software.quake.Edge`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/id_software/quake.py#L138) | 100% |
| 111 | 006F | 29 | `PORTAL_VERTEX_EDGES` | 0 | [`respawn.titanfall.PortalEdgeIntersect`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L397) | 0% |
| 112 | 0070 | 29 | `PORTAL_VERTEX_REFERENCES` | 0 | [`shared.UnsignedShorts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L38) | 100% |
| 113 | 0071 | 29 | `PORTAL_EDGE_REFERENCES` | 0 | [`shared.UnsignedShorts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L38) | 100% |
| 114 | 0072 | 29 | `PORTAL_EDGE_INTERSECT_AT_EDGE` | 0 | [`respawn.titanfall.PortalEdgeIntersect`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L397) | 0% |
| 114 | 0072 | 37 | `PORTAL_EDGE_INTERSECT_EDGE` | 0 |  | 0% |
| 115 | 0073 | 29 | `PORTAL_EDGE_INTERSECT_AT_VERTEX` | 0 | [`respawn.titanfall.PortalEdgeIntersect`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L397) | 0% |
| 116 | 0074 | 29 | `PORTAL_EDGE_INTERSECT_HEADER` | 0 | [`respawn.titanfall.PortalEdgeIntersectHeader`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L404) | 100% |
| 117 | 0075 | 29 | `OCCLUSION_MESH_VERTICES` | 0 | [`id_software.quake.Vertex`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/id_software/quake.py#L238) | 100% |
| 118 | 0076 | 29 | `OCCLUSION_MESH_INDICES` | 0 | [`shared.Shorts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L26) | 100% |
| 119 | 0077 | 29 | `CELL_AABB_NODES` | 0 | [`respawn.titanfall.Node`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L360) | 50% |
| 120 | 0078 | 29 | `OBJ_REFERENCES` | 0 | [`shared.UnsignedShorts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L38) | 100% |
| 121 | 0079 | 29 | `OBJ_REFERENCE_BOUNDS` | 0 | [`respawn.titanfall.ObjRefBounds`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L370) | 100% |
| 122 | 007A | 29 | `UNUSED_122` | 0 |  | 0% |
| 122 | 007A | 37 | `LIGHTMAP_DATA_RTL_PAGE` | 0 |  | 0% |
| 123 | 007B | 29 | `LEVEL_INFO` | 0 |  | 0% |
| 124 | 007C | 29 | `SHADOW_MESH_OPAQUE_VERTICES` | 0 | [`id_software.quake.Vertex`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/id_software/quake.py#L238) | 100% |
| 125 | 007D | 29 | `SHADOW_MESH_ALPHA_VERTICES` | 0 | [`respawn.titanfall.ShadowMeshAlphaVertex`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/respawn/titanfall.py#L428) | 75% |
| 126 | 007E | 29 | `SHADOW_MESH_INDICES` | 0 | [`shared.UnsignedShorts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L38) | 100% |


