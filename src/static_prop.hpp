namespace bsp_tool {
    /* Common base types */
    // TODO: replace with an import from a common types header
    struct Vector { float x, y, z; };
    struct QAngle { float pitch, yaw, roll; };
    struct Colour32 { unsigned char r, g, b, a; };

    namespace respawn_entertainment {
        // mostly identified by BobTheBob
        struct StaticPropv12 {
            struct Vector    origin;
            struct QAngle    angles;
            unsigned short   mdl_name;
            unsigned short   first_leaf;              // NOTE: rBSP has no leaves
            unsigned short   leaf_count;
            unsigned char    solid;
            unsigned char    flags;
            int              skin;
            unsigned int     cubemap;                 // new! an index?
            float            fade_distance_min;
            float            fade_distance_max;
            struct Vector    lighting_origin;
            float            forced_fade_scale;
            char             cpu_level_min;           // -1 == any
            char             cpu_level_max;
            char             gpu_level_min;
            char             gpu_level_max;
            struct Colour32  diffuse_modulation;
            bool             disable_x360;            // 4 byte bool
            float            scale;                   // should be 1.0?
            unsigned short   collision_flags_add;     // new!
            unsigned short   collision_flags_remove;  // new!
        };

        // mostly identified by BobTheBob
        struct StaticPropv13 {
            struct Vector    origin;
            struct QAngle    angles;
            char             unknown_1[4];
            unsigned short   mdl_name;
            unsigned char    solid_type;
            unsigned char    flags;
            char             unknown_2[4];         // generally  00 00 <num under 10> 00
            float            forced_fade_scale;
            struct Vector    lighting_origin;
            char             cpu_level_min;        // -1 == any
            char             cpu_level_max;
            char             gpu_level_min;
            char             gpu_level_max;
            struct Colour32  diffuse_modulation;  // always 0000?
            unsigned short   collision_flags_add;
            unsigned short   collision_flags_remove;
        };
    }
}
