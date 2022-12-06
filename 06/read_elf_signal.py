
def get_index_after_market_from_elf_signal(
    signal: str,
    unique_chars_that_mark_start: int,
) -> str:
    i = 0

    while i < len(signal):
        start, end = i, i + unique_chars_that_mark_start

        if len(set(signal[start:end])) == unique_chars_that_mark_start:
            return end

        i += 1

    return -1


if __name__ == "__main__":

    with open("06_input.txt", "r") as f:
            raw_signal = f.readline().strip()

    start_of_packet = get_index_after_market_from_elf_signal(raw_signal, 4)
    start_of_message = get_index_after_market_from_elf_signal(raw_signal, 14)

    print(f"{start_of_packet=}", f"{start_of_message=}", sep="\n")
