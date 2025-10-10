def longest_positive_streak(nums: list[int]) -> int:
    """
    Return the length of the longest consecutive run of strictly positive numbers in nums.
    Rules:
    - Empty list returns 0.
    - Non-positive numbers (0 or negatives) break the streak.
    - Deterministic and pure: no randomness, prints, or global state.
    """
    max_streak = 0
    current_streak = 0
    for num in nums:
        if num > 0:
            current_streak += 1
        else:
            max_streak = max(max_streak, current_streak)
            current_streak = 0
    max_streak = max(max_streak, current_streak)
    return max_streak
