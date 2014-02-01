import random

castle = [
    [
        ["ca_planet_survey"]
    ],
    [
        ["ca_no_atmosphere", "ca_no_atmosphere_domes", "ca_artificial_atmosphere"],
        ["ca_toxic_atmosphere", "ca_toxic_atmosphere_domes", "ca_scrubbed_atmosphere"],
        ["ca_clean_atmosphere"]
    ],
    [
        ["ca_no_water", "ca_trace_water", "ca_lakes", "ca_seas", "ca_oceans"]
    ],
    [
        ["ca_frozen", "ca_cold", "ca_cool", "ca_optimal_cold"],
        ["ca_burning", "ca_hot", "ca_warm", "ca_optimal_hot"]
    ]
]

castle_ss = [
    [
        ["ca_space_station_0", "ca_space_station_1", "ca_space_station_2", "ca_space_station_3", "ca_space_station_4"]
    ]
]

city = [
    [
        ["ct_planet_survey"]
    ],
    [
        ["ct_no_atmosphere", "ct_no_atmosphere_domes", "ct_artificial_atmosphere"],
        ["ct_toxic_atmosphere", "ct_toxic_atmosphere_domes", "ct_scrubbed_atmosphere"],
        ["ct_clean_atmosphere"]
    ],
    [
        ["ct_no_water", "ct_trace_water", "ct_lakes", "ct_seas", "ct_oceans"]
    ],
    [
        ["ct_frozen", "ct_cold", "ct_cool", "ct_optimal_cold"],
        ["ct_burning", "ct_hot", "ct_warm", "ct_optimal_hot"]
    ]
]

city_ss = [
    [
        ["ct_space_station_0", "ct_space_station_1", "ct_space_station_2", "ct_space_station_3", "ct_space_station_4" ]
    ]
]

city_ss_asteroid = [
    [
        ["ct_asteroids"]
    ]
]

temple = [
    [
        ["tp_planet_survey"]
    ],
    [
        ["tp_no_atmosphere", "tp_no_atmosphere_domes", "tp_artificial_atmosphere"],
        ["tp_toxic_atmosphere", "tp_toxic_atmosphere_domes", "tp_scrubbed_atmosphere"],
        ["tp_clean_atmosphere"]
    ],
    [
        ["tp_no_water", "tp_trace_water", "tp_lakes", "tp_seas", "tp_oceans"]
    ],
    [
        ["tp_frozen", "tp_cold", "tp_cool", "tp_optimal_cold"],
        ["tp_burning", "tp_hot", "tp_warm", "tp_optimal_hot"]
    ]
]

ss_list = [
    "b_zhai_zhigang_waystation",
    "b_liu_wang_waystation",
    "b_liu_yang_waystation",
    "b_zhang_xiaoguang_waystation",
    "b_wang_yaping_waystation",
    "b_qinglong_waystation",
    "b_tletlioh_waystation",
    "b_santa_maria_waystation",
    "b_dom_frontera_waystation",
    "b_al_jisr_waystation",
    "b_al_bawwaaba_waystation",
    "b_shams_akhdar_waystation",
    "b_sharman_waystation",
    "b_orbital_station_alpha",
    "b_orbital_station_beta",
    "b_orbital_station_gamma",
    "b_heavens_gate",
    "b_tengoku_waystation",
    "b_hu_lao_gate",
    "b_tannhauser_gate",
    "b_liu_yang_observatory",
    "b_macau_station",
    "b_xianggang_xin_orbital",
    "b_jiu_wanguan_xi_orbital"
    "b_wanguan_orbital_b",
    "b_jiayuan_orbital",
    "b_ying_shi_viii_orbital"
]

asteroid_list = [
    "b_sharman_waystation",
    "b_orbital_station_alpha",
    "b_orbital_station_beta",
    "b_orbital_station_gamma",
    "b_heavens_gate",
    "b_tengoku_waystation",
    "b_macau_station",
    "b_xianggang_xin_orbital",
    "b_gaoda_de_shan_iii_refinery",
    "b_jiu_wanguan_xi_orbital_a",
    "b_ying_shi_xii_orbital",
    "b_ghuanghai_inner_belt",
    "b_ghuanghai_outer_belt"
]

def create(config):
    source_list = castle if "castle" in config else city if "city" in config else temple
    prefix = "ca_" if "castle" in config else "ct_" if "city" in config else "tp_"
    ret = list()

    if "space_station" in config:
        ret.append(prefix + "space_station_0")

        if "asteroids" in config:
            ret.append(prefix + "asteroids")

    else:
        ret.append(prefix + "planet_survey")

        if "no_atmo" in config:
            ret.append(prefix + "no_atmosphere")
        elif "toxic" in config:
            ret.append(prefix + "toxic_atmosphere")
        elif "clean" in config:
            ret.append(prefix + "clean_atmosphere")
        else:
            r = random.random()
            if r < 0.2:
                    ret.append(prefix + "clean_atmosphere")
            elif r < 0.6:
                    ret.append(prefix + "toxic_atmosphere")
            else:
                    ret.append(prefix + "no_atmosphere")

        levels = ["no_water", "trace_water", "lakes", "seas", "oceans"]
        l = None
        for level in levels:
            if level in config:
                l = level
                break
        if l is None:
            l = random.choice(levels)
        ret.append(prefix + l)
        
        temps = ["frozen", "cold", "cool", "optimal_cold", "burning", "hot", "warm", "optimal_hot"]
        t = None
        for temp in temps:
            if temp in config:
                t = temp
                break
        if t is None:
            t = random.choice(temps)
        ret.append(prefix + t)

    return ret
    
if __name__ == "__main__":
    print("castle")