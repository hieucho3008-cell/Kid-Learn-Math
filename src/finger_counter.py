def count_fingers(hand):

    tips = [4, 8, 12, 16, 20]

    count = 0

    # Thumb
    if hand[tips[0]][0] > hand[tips[0]-1][0]:
        count += 1

    # Index -> Pinky
    for tip in tips[1:]:

        if hand[tip][1] < hand[tip-2][1]:
            count += 1

    return count
