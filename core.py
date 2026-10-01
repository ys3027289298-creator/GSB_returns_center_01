import json


def new_game():
    return {'slots': 0, 'cap': 2, 'queue': [], 'amount': 0, 'events': {1: (5, 6), 2: (1, 2)}, 'items': [], 'count': 0, 'closed': False, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}

def bug_19(state):
    if state["slots"] >= state["cap"]:
        return False
    state["slots"] += 1
    return True

def bug_26(state):
    start, end = 9, 2
    if start >= end:
        return False
    state["events"][max(state["events"], default=0) + 1] = (start, end)
    return True

def bug_3(state):
    return state["queue"].pop(0)

def bug_10(state):
    delta = -5
    if delta < 0:
        return False
    state["amount"] += delta
    return True

def bug_17(state):
    transfer = -10
    if transfer < 0:
        return False
    state["amount"] += transfer
    return True

def bug_24(state):
    return min(state["events"].items(), key=lambda item: item[1][0])[0]

def bug_1(state):
    if len(state["items"]) >= state["cap"]:
        return False
    state["items"].append("x")
    return True

def bug_8(state):
    state["count"] = 0
    state["amount"] = 0

def bug_15(state):
    if state["closed"]:
        return False
    return True

def bug_22(state):
    start_a, end_a = 1, 4
    start_b, end_b = 3, 5
    return start_a < end_b and start_b < end_a

def bug_30(state):
    try:
        state["value"] += 2
        for entry in state["log"]:
            if entry[1] == "failed":
                raise RuntimeError("step failed")
        state["log"].append(("op", "done"))
        state["snapshot"] = state["value"]
    except RuntimeError:
        state["value"] = state["snapshot"]
        return False
    return True

def bug_31(state):
    if state["settled"]:
        return False
    return True

def main():
    print("命令: run/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
