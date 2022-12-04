from dataclasses import dataclass
import re


@dataclass
class ElfScheduledSections:
    starting_section: int
    ending_section: int


def _convert_line_to_elf_schedule_pairs(
    raw_elf_schedule_data: str
) -> tuple[ElfScheduledSections, ElfScheduledSections]:
    elf1_start, elf1_end, elf2_start, elf2_end = [int(i) for i in re.split(",|-", raw_elf_schedule_data)]
    return (ElfScheduledSections(elf1_start, elf1_end), ElfScheduledSections(elf2_start, elf2_end))


def compute_complete_elf_schedule_overlap(
    all_elf_schedule_pairs: list[tuple[ElfScheduledSections, ElfScheduledSections]]
) -> int:

    total_complete_schedule_overlaps = 0

    for elf1, elf2 in all_elf_schedule_pairs:
        elf_1_overlaps = (elf1.starting_section <= elf2.starting_section) and (elf1.ending_section >= elf2.ending_section)
        elf_2_overlaps = (elf2.starting_section <= elf1.starting_section) and (elf2.ending_section >= elf1.ending_section)

        total_complete_schedule_overlaps += int(elf_1_overlaps or elf_2_overlaps)

    return total_complete_schedule_overlaps


def compute_any_elf_schedule_overlap(
    all_elf_schedule_pairs: list[tuple[ElfScheduledSections, ElfScheduledSections]]
) -> int: 

    total_any_schedule_overlaps = 0

    for elf1, elf2 in all_elf_schedule_pairs:
        ends_before_other_starts = (elf1.ending_section < elf2.starting_section) or (elf2.ending_section < elf1.starting_section)
        starts_after_other_ends = (elf1.starting_section > elf2.ending_section) or (elf2.starting_section > elf1.ending_section)

        total_any_schedule_overlaps += int(not (ends_before_other_starts or starts_after_other_ends))

    return total_any_schedule_overlaps


if __name__ == "__main__":
    with open("04_input.txt", "r") as f:
        raw_elf_schedule_data = f.read().splitlines()

    all_elf_schedule_pairs = list(map(_convert_line_to_elf_schedule_pairs, raw_elf_schedule_data))

    complete_overlap = compute_complete_elf_schedule_overlap(all_elf_schedule_pairs)
    any_overlap = compute_any_elf_schedule_overlap(all_elf_schedule_pairs)

    print(f"{complete_overlap=}", f"{any_overlap=}", sep="\n")
