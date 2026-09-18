# 초기 가중치 랜덤으로 적용.
# 추후에 사용자 피드백 기반으로 가중치 조정 가능.

BOTTOM_SILHOUETTES = [
    "slim",
    "tapered",
    "straight",
    "relaxed_straight",
    "wide",
    "balloon",
]

BOTTOM_SILHOUETTE_PROFILES = {

    "slim": {
        "weights": {
            "waist": 0.30,
            "rise": 0.10,
            "thigh": 0.30,
            "hem": 0.20,
            "length": 0.10,
        },
        "shape": {
            "thigh": "narrow",
            "hem": "narrow",
            "rise": "neutral",
        }
    },

    "tapered": {
        "weights": {
            "waist": 0.25,
            "rise": 0.10,
            "thigh": 0.25,
            "hem": 0.30,
            "length": 0.10,
        },
        "shape": {
            "thigh": "moderate",
            "hem": "narrow",
            "rise": "neutral",
        }
    },

    "straight": {
        "weights": {
            "waist": 0.25,
            "rise": 0.10,
            "thigh": 0.25,
            "hem": 0.20,
            "length": 0.20,
        },
        "shape": {
            "thigh": "moderate",
            "hem": "moderate",
            "rise": "neutral",
        }
    },

    "relaxed_straight": {
        "weights": {
            "waist": 0.20,
            "rise": 0.15,
            "thigh": 0.30,
            "hem": 0.15,
            "length": 0.20,
        },
        "shape": {
            "thigh": "relaxed",
            "hem": "moderate",
            "rise": "slightly_high",
        }
    },

    "wide": {
        "weights": {
            "waist": 0.20,
            "rise": 0.15,
            "thigh": 0.25,
            "hem": 0.25,
            "length": 0.15,
        },
        "shape": {
            "thigh": "wide",
            "hem": "wide",
            "rise": "neutral_to_high",
        }
    },

    "balloon": {
        "weights": {
            "waist": 0.20,
            "rise": 0.15,
            "thigh": 0.30,
            "hem": 0.25,
            "length": 0.10,
        },
        "shape": {
            "thigh": "very_wide",
            "hem": "narrower_than_thigh",
            "rise": "neutral_to_high",
        }
    },
}