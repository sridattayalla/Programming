def move_tower(height, from_twr, to_twr, with_twr):
    if height > 0:
        move_tower(height - 1, from_twr, with_twr, to_twr)
        print("moving disc from ", from_twr," to ", to_twr)
        move_tower(height - 1, with_twr, to_twr, from_twr)

move_tower(3, "A", "B", "C")