def champion_rank(pilot: int, events: str) -> int:

    print(events)

    if not events: return pilot

    ev = events.split()
    raceway = {}
    for k in range(1, 21):
        raceway[k] = k

    for i in range(0, len(ev) - 1, 2):
        pilot_id, event = int(ev[i]), ev[i + 1]

        if event.lower() == "o":
            raceway[pilot_id] -= 1

        elif event.lower() == "i":
            raceway[pilot_id] = -1
            for p in range(pilot_id + 1, 21):
                raceway[p] -= 1

    return raceway[pilot] if raceway[pilot] else 1


if __name__ == "__main__":
    print(champion_rank(3, ""))    # 3
    print(champion_rank(10, "1 I 10 O 2 I"))    # 7
    print(champion_rank(12, "4 O 3 O"))         # 12
    print(champion_rank(2, "9 O 17 O 9 O 12 O 2 O 12 O 9 O 1 O 5 O 12 O 17 O 20 O 16 O 7 O 2 O 8 O 16 O 14 O 3 O 14 O 11 O 16 O 1 O 13 O 8 O 14 O 5 O 12 O 4 O"))
    print(champion_rank(1, "5 O 7 O 17 O 14 O 19 O 6 O 11 O 18 O 7 O 4 O 12 O 19 O 17 O 13 O 13 O 7 O 5 O 8 O 4 O 4 O 16 O 12 O 12 O 16 O 9 O 8 O 5 O 11 O 3 O 17 O 10 O 6 O 15 O 6 O 8 O 2 O 10 O 6 O 11 O 4 O 10 O 7 O 16 O 13 O 12 O 4 O 2 O"))
    # 3