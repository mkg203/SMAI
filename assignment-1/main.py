from game import SpaceJamm

if __name__ == "__main__":
    space_jam = SpaceJamm("./maps/map_1.txt")
    space_jam.show_board()
    # print(space_jam.goal_test())
    print(space_jam.move_gen())
