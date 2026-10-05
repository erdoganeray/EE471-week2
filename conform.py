# This script is written by Eray

def _format_command(start, end):
    if start == end:
        return f"Person in position {start} flip your cap!"
    return f"People in positions {start} through {end} flip your caps!"


def _extract_runs(caps, ignore=frozenset()):
    runs = []
    run_char, run_start = None, None
    for i, c in enumerate(caps):
        if c in ignore:
            if run_char is not None:
                runs.append((run_char, run_start, i - 1))
                run_char = None
            continue
        if c != run_char:
            if run_char is not None:
                runs.append((run_char, run_start, i - 1))
            run_char, run_start = c, i
    if run_char is not None:
        runs.append((run_char, run_start, len(caps) - 1))
    return runs


def pleaseConform(caps):
    runs = _extract_runs(caps)
    f_runs = [r for r in runs if r[0] == 'F']
    b_runs = [r for r in runs if r[0] == 'B']
    for _, start, end in (f_runs if len(f_runs) < len(b_runs) else b_runs):
        print(_format_command(start, end))


def pleaseConformOnepass(caps):
    if not caps:
        return
    # Runs always start with caps[0]'s letter, so by alternation caps[0]
    # never has fewer runs than the other letter: flipping "not caps[0]"
    # is always optimal, and needs only one left-to-right pass.
    target = caps[0]
    run_start = None
    for i, c in enumerate(caps):
        if c != target:
            if run_start is None:
                run_start = i
        elif run_start is not None:
            print(_format_command(run_start, i - 1))
            run_start = None
    if run_start is not None:
        print(_format_command(run_start, len(caps) - 1))


def pleaseConformSkipBald(caps):
    runs = _extract_runs(caps, ignore={'H'})
    f_runs = [r for r in runs if r[0] == 'F']
    b_runs = [r for r in runs if r[0] == 'B']
    for _, start, end in (f_runs if len(f_runs) < len(b_runs) else b_runs):
        print(_format_command(start, end))


if __name__ == "__main__":
    cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
    cap3 = ['F', 'F', 'B', 'H', 'B', 'F', 'B', 'B', 'B', 'F', 'H', 'F', 'F']

    print("pleaseConform(cap1):")
    pleaseConform(cap1)

    print("\npleaseConformOnepass(cap1):")
    pleaseConformOnepass(cap1)

    print("\npleaseConformOnepass([]):")
    pleaseConformOnepass([])
    print("(no output, no crash)")

    print("\npleaseConformSkipBald(cap3):")
    pleaseConformSkipBald(cap3)
