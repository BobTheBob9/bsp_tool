# Call of Duty
## Developers: Infinity Ward

| BspClass | Bsp version | Game | Branch script | Supported lumps | Unused lumps | Coverage |
| -------: | ----------: | ---- | ------------- | --------------: | -----------: | :------- |
| [`InfinityWardBsp`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/bsp_tool/infinity_ward.py#L10) | 4 | Call of Duty 2 | [`infinity_ward.call_of_duty2`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/infinity_ward/call_of_duty2.py) | 19 / 40 | 0 | 47.08% |
| [`IdTechBsp`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/bsp_tool/id_software.py#L99) | 59 | Call of Duty | [`infinity_ward.call_of_duty1`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/infinity_ward/call_of_duty1.py) | 16 / 31 | 0 | 51.61% |
| [`IdTechBsp`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/bsp_tool/id_software.py#L99) | 59 | Call of Duty: United Offensive | [`infinity_ward.call_of_duty1`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/infinity_ward/call_of_duty1.py) | 16 / 31 | 0 | 51.61% |


## Supported Lumps
| Lump index | Bsp version | Lump name | LumpClass | Coverage |
| ---------: | ----------: | --------- | --------- | :------- |
| 0 | 4 | `SHADERS` | [`infinity_ward.call_of_duty1.Shader`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/infinity_ward/call_of_duty1.py#L195) | 100% |
| 1 | 4 | `LIGHTMAPS` |  | 0% |
| 1 | 59 | `LIGHTMAPS` | [`infinity_ward.call_of_duty1.Lightmap`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/infinity_ward/call_of_duty1.py#L123) | 100% |
| 2 | 4 | `LIGHT_GRID_HASHES` |  | 0% |
| 2 | 59 | `PLANES` | [`infinity_ward.call_of_duty1.Plane`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/infinity_ward/call_of_duty1.py#L181) | 100% |
| 3 | 4 | `LIGHT_GRID_VALUES` |  | 0% |
| 3 | 59 | `BRUSH_SIDES` | [`infinity_ward.call_of_duty1.BrushSide`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/infinity_ward/call_of_duty1.py#L80) | 100% |
| 4 | 4 | `PLANES` | [`infinity_ward.call_of_duty1.Plane`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/infinity_ward/call_of_duty1.py#L181) | 100% |
| 4 | 59 | `BRUSHES` |  | 0% |
| 5 | 4 | `BRUSH_SIDES` | [`infinity_ward.call_of_duty1.BrushSide`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/infinity_ward/call_of_duty1.py#L80) | 100% |
| 6 | 4 | `BRUSHES` |  | 0% |
| 6 | 59 | `TRIANGLE_SOUPS` | [`infinity_ward.call_of_duty1.TriangleSoup`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/infinity_ward/call_of_duty1.py#L204) | 100% |
| 7 | 4 | `TRIANGLE_SOUPS` | [`infinity_ward.call_of_duty2.TriangleSoup`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/infinity_ward/call_of_duty2.py#L170) | 100% |
| 7 | 59 | `DRAW_VERTICES` |  | 0% |
| 8 | 4 | `VERTICES` | [`infinity_ward.call_of_duty2.Vertex`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/infinity_ward/call_of_duty2.py#L182) | 83% |
| 8 | 59 | `DRAW_INDICES` | [`shared.UnsignedShorts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L38) | 100% |
| 9 | 4 | `TRIANGLES` | [`infinity_ward.call_of_duty2.Triangle`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/infinity_ward/call_of_duty2.py#L163) | 100% |
| 9 | 59 | `CULL_GROUPS` |  | 0% |
| 10 | 4 | `CULL_GROUPS` |  | 0% |
| 10 | 59 | `CULL_GROUP_INDICES` | [`shared.UnsignedInts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L34) | 100% |
| 11 | 4 | `CULL_GROUP_INDICES` | [`shared.UnsignedInts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L34) | 100% |
| 11 | 59 | `PORTAL_VERTICES` |  | 0% |
| 12 | 4 | `SHADOW_VERTICES` |  | 0% |
| 13 | 4 | `SHADOW_INDICES` |  | 0% |
| 13 | 59 | `OCCLUDER_PLANES` | [`shared.UnsignedInts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L34) | 100% |
| 14 | 4 | `SHADOW_CLUSTERS` |  | 0% |
| 14 | 59 | `OCCLUDER_EDGES` | [`id_software.quake.Edge`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/id_software/quake.py#L138) | 100% |
| 15 | 4 | `SHADOW_AABB_TREES` |  | 0% |
| 15 | 59 | `OCCLUDER_INDICES` | [`shared.UnsignedShorts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L38) | 100% |
| 16 | 4 | `SHADOW_SOURCES` |  | 0% |
| 17 | 4 | `PORTAL_VERTICES` | [`id_software.quake.Vertex`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/id_software/quake.py#L238) | 100% |
| 17 | 59 | `CELLS` |  | 0% |
| 18 | 4 | `OCCLUDERS` |  | 0% |
| 19 | 4 | `OCCLUDER_PLANES` | [`shared.UnsignedInts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L34) | 100% |
| 19 | 59 | `LIGHT_INDICES` | [`shared.UnsignedShorts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L38) | 100% |
| 20 | 4 | `OCCLUDER_EDGES` | [`id_software.quake.Edge`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/id_software/quake.py#L138) | 100% |
| 20 | 59 | `NODES` |  | 0% |
| 21 | 4 | `OCCLUDER_INDICES` | [`shared.UnsignedShorts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L38) | 100% |
| 21 | 59 | `LEAVES` | [`infinity_ward.call_of_duty1.Leaf`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/infinity_ward/call_of_duty1.py#L108) | 100% |
| 22 | 4 | `AABB_TREE` |  | 0% |
| 22 | 59 | `LEAF_BRUSHES` | [`shared.UnsignedInts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L34) | 100% |
| 23 | 4 | `CELLS` |  | 0% |
| 23 | 59 | `LEAF_SURFACES` | [`shared.UnsignedInts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L34) | 100% |
| 24 | 4 | `PORTALS` |  | 0% |
| 25 | 4 | `NODES` |  | 0% |
| 26 | 4 | `LEAVES` | [`infinity_ward.call_of_duty1.Leaf`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/infinity_ward/call_of_duty1.py#L108) | 100% |
| 26 | 59 | `COLLISION_INDICES` | [`shared.UnsignedShorts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L38) | 100% |
| 27 | 4 | `LEAF_BRUSHES` | [`shared.UnsignedInts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L34) | 100% |
| 27 | 59 | `MODELS` |  | 0% |
| 28 | 4 | `LEAF_SURFACES` | [`shared.UnsignedInts`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L34) | 100% |
| 28 | 59 | `VISIBILITY` |  | 0% |
| 29 | 4 | `COLLISION_VERTICES` |  | 0% |
| 29 | 59 | `ENTITIES` | [`shared.Entities`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L43) | 100% |
| 30 | 4 | `COLLISION_EDGES` |  | 0% |
| 31 | 4 | `COLLISION_TRIANGLES` |  | 0% |
| 32 | 4 | `COLLISION_BORDERS` |  | 0% |
| 33 | 4 | `COLLISION_PARTS` |  | 0% |
| 34 | 4 | `COLLISION_AABBS` |  | 0% |
| 35 | 4 | `MODELS` |  | 0% |
| 36 | 4 | `VISIBILITY` |  | 0% |
| 37 | 4 | `ENTITIES` | [`shared.Entities`](https://github.com/snake-biscuits/bsp_tool/blob/master/bsp_tool/branches/shared.py#L43) | 100% |
| 38 | 4 | `PATHS` |  | 0% |


