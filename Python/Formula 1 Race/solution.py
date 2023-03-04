def champion_rank(pilot: int, events: str) -> int:

    if not events: return pilot

    ev = events.split()
    print(ev)
    pilots = list(range(1, 21))
    print(pilots)

    for i in range(0, len(ev) - 1, 2):
        pilot_id, event = ev[i], ev[i + 1]



if __name__ == "__main__":
    print(champion_rank(3, ""))    # 3
    print(champion_rank(10, "1 I 10 O 2 I"))    # 7
    print(champion_rank(12, "4 O 3 O"))         # 12
    