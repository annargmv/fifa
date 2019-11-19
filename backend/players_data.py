
class Backend:
    def __init__(self):
        self._players_dict = {}

    def read_from_file(self):
        with open('backend/static/data1.csv') as f:
            lines = f.readlines()[1:]
            self.create_dict_with_keys()
            for line in lines:
                line_list = line.strip().split(",")
                self.create_dict_of_players(line_list)

        return self._players_dict

    def create_dict_of_players(self, players_data):
        for i in range(15, 30):
            start_range = i
            end_range = i + 5

            if start_range <= int(players_data[3]) <= end_range:
                self._players_dict["{}-{}".format(start_range, end_range)].append(
                    {"name": players_data[2], "photo_link": players_data[4]})
        return self._players_dict


    def create_dict_with_keys(self):
        for i in range(15, 30):
            start_range = i
            end_range = i + 5
            self._players_dict["{}-{}".format(start_range, end_range)] = []
        # print(self._players_dict)


def main():
    player = Backend()
    player.create_dict_with_keys()
    player.read_from_file()

if __name__== "__main__" :
    main()