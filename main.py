def calculate_bounty(base_reward, difficulty, quality):
    """
    Calculate a code bounty reward.

    difficulty: 1-5
    quality: 1-5
    """

    if not 1 <= difficulty <= 5:
        raise ValueError("Difficulty must be between 1 and 5")

    if not 1 <= quality <= 5:
        raise ValueError("Quality must be between 1 and 5")

    difficulty_multiplier = 1 + (difficulty - 1) * 0.15
    quality_multiplier = 1 + (quality - 1) * 0.10

    reward = base_reward * difficulty_multiplier * quality_multiplier

    return round(reward, 2)


if __name__ == "__main__":
    bounty = calculate_bounty(
        base_reward=100,
        difficulty=4,
        quality=5
    )

    print(f"Code bounty reward: ${bounty}")
