# process the csv file
class parser_process:

    def __init__(self, input_file):
        self.input_file = input_file
        self.user_dic = {}
        self.data_points = []


    def process(self):
        try:
            f_in = open(self.input_file, "r")
        except:
            print("unable to open " + self.input_file)

        # get rid of the first line
        first_line = f_in.readline()
        # read and parse
        for line in f_in:
            id, day, bg = line.split(",")
            # convert to int
            i_day = int(day)
            i_bg = int(bg)
            # new member
            if id in self.user_dic:
                # update the user_dic
                self.user_dic[id].add(i_day, i_bg)
            else:
                r_member = rle_member(i_day, i_bg)
                self.user_dic[id] = r_member

    # this is called after process --> output max_days for each user to an array
    def get_result(self):
        for k, v in self.user_dic.items():
            # output max_days
            self.data_points.append(v.get_max_days())

        return self.data_points


# keep track of string representation ==> a: active| i: inactive
# 1a2i
# assuming the incoming days are consecutive
class rle_member:
    def __init__(self, i_day, i_bg):
        self.states = ["i", "a"]
        # make sure days are also consecutive
        self.cur_day = i_day
        self.cur_state = self.states[i_bg]
        # consecutive
        self.count = 1
        # case for max_days
        self.max_days = 0
        if self.cur_state == "i":
            self.max_days = 1

        self.elt = ""


    def add(self, i_day, i_bg):
        # bg is either 0 or 1
        state = self.states[i_bg]

        # not equal
        if self.cur_state != state:
            # update the self.elt representation
            self.elt = self.elt + str(self.count) + self.cur_state
            # reset self.count & cur_state
            self.cur_state = state
            self.count = 1
        # equal
        else:
            # increment self.count
            self.count += 1
            # keep track of max_days
            if state is "i":
                self.max_days = max(self.max_days, self.count)


    # call whenever switching user_id a and b
    def update(self):
        self.elt = self.elt + str(self.count) + self.cur_state


    def get_elt(self):
        # ensure the last update
        self.update()
        return self.elt

    def get_max_days(self):
        return self.max_days