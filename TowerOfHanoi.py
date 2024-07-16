def tower_of_hanoi(num: int, source: str, destination: str, temp: str) -> None:
    """
    :param num: The number of Disks
    :param source: The initial source where all the disks are kept.
    :param destination: The final disk number where you want to swap
    :param temp: A temporary pole
    :return: None
    """

    if num == 1:
        print("Move Disk", num, "from", source, "to", destination)
        return

    tower_of_hanoi(num - 1, source, temp, destination)
    print("Move Disk", num, "from", source, "to", destination)
    tower_of_hanoi(num - 1, temp, destination, source)


tower_of_hanoi(3, "A", "B", "C")
