from typing import List, Iterator


def non_functional() -> None:
    names = ['Mary', 'Isla', 'Sam']

    for i in names:
        names[i] = hash(names[i])

    hash(names)
    print(names)


def functional(names: List[str]) -> Iterator[int]:
    return map(hash, names)
