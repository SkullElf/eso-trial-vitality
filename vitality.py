# vitality.py - ESO Trial Score & Vitality Calculator

trials_data = {
    "aetherian archive": {"base_score_hm": 124300},
    "hel ra citadel": {"base_score_hm": 133100},
    "sanctum ophidia": {"base_score_hm": 142700},
    "maw of lorkhaj": {"base_score_hm": 108150},
    "halls of fabrication": {"base_score_hm": 160100},
    "asylum sanctorium": {"base_score_hm": 70000},
    "cloudrest": {"base_score_hm": 85750, "base_score_hm_bonus": 88000},  # Bonus is the trash of all minis
    "sunspire": {"base_score_hm": 207250},
    "kyne's aegis": {"base_score_hm": 205950},
    "rockgrove": {"base_score_hm": 226700, "base_score_hm_bonus": 232200},  # Bonus is the snake and the wounded soldiers
    "dreadsail reef": {"base_score_hm": 265850},
    "sanity's edge": {"base_score_hm": 205200},
    "lucent citadel": {"base_score_hm": 192850}
}


def calculate_vitality(trial_name: str, trial_score: int, duration_seconds: int) -> str:
    """Processes trial data, calculates vitality, and verifies the result."""
    trial_name = trial_name.lower()

    if trial_name not in trials_data:
        raise ValueError("Trial name not found in data.")

    trial_info = trials_data[trial_name]
    base_score = trial_info.get("base_score_hm")
    base_score_bonus = trial_info.get("base_score_hm_bonus")

    # Try calculating vitality with both base_score and base_score_bonus
    for score in [base_score_bonus, base_score]:
        if score is None:
            continue

        vitality = (trial_score / (1 + (2700 - duration_seconds) / 10000) - score) / 1000
        vitality = round(vitality)

        # Define score sensitivity per second
        score_change_per_second = (score + vitality * 1000) / 10000
        max_allowed_mismatch = score_change_per_second  # Max mismatch within 1 second because milliseconds are ignored by the game

        # Verify the calculated vitality
        recalculated_score = (score + vitality * 1000) * (1 + (2700 - duration_seconds) / 10000)
        if abs(recalculated_score - trial_score) <= max_allowed_mismatch:
            return f"{vitality}/36" if score == base_score else f"{vitality}/36 with bonus"

    return "N/A"


# Example usage
if __name__ == "__main__":
    # Example 1
    run_data = {
        "trial_name": "Rockgrove",
        "score": 309756,
        "duration_seconds": 886  # 14 minutes and 46 seconds
    }
    result = calculate_vitality(run_data["trial_name"], run_data["score"], run_data["duration_seconds"])
    print("Rockgrove example:", result)
# ==========================================
    # Example 2
    run_data = {
        "trial_name": "Lucent Citadel",
        "score": 261808,
        "duration_seconds": 1209  # 20 minutes and 09 seconds
    }
    result = calculate_vitality(run_data["trial_name"], run_data["score"], run_data["duration_seconds"])
    print("Lucent Citadel example:", result)
# ==========================================
    # Example 3
    run_data = {
        "trial_name": "Sanity's Edge",
        "score": 275680,
        "duration_seconds": 1222  # 20 minutes and 22 seconds
    }
    result = calculate_vitality(run_data["trial_name"], run_data["score"], run_data["duration_seconds"])
    print("Sanity's Edge example:", result)
# ==========================================
    # Example 4 (invalid result)
    run_data = {
        "trial_name": "Cloudrest",
        "score": 980000,
        "duration_seconds": 700  # 11 minutes and 40 seconds
    }
    result = calculate_vitality(run_data["trial_name"], run_data["score"], run_data["duration_seconds"])
    print("Cloudrest example:", result)
