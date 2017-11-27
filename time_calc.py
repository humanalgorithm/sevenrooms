import datetime as dt

class TimeBlock():
    def __init__(self, start, end):
        self.time_block = {"start": start, "end": end}

    def __repr__(self):
        return "{}".format(self.time_block)

    def get(self):
        return self.time_block

class TimeUtility():
    def sort_times(self, time_block_list):
        sorted_list = sorted(time_block_list, key=lambda k: k.get()['start'])
        return sorted_list

class TimeCalculuation():
    def __init__(self):
        self.availability_start = dt.time(17, 0, 0)
        self.availability_end = dt.time(21, 0, 0)
        self.start_key = "start"
        self.end_key = "end"

    def get_time_block_can_be_added(self, schedule_time_blocks, time_block):
        schedule_time_blocks = TimeUtility().sort_times(schedule_time_blocks)
        start_less_than_end = filter(lambda x: x.get()[self.start_key] < time_block.get()[self.end_key], schedule_time_blocks)
        end_greater_than_start = filter(lambda x: x.get()[self.end_key] > time_block.get()[self.start_key], start_less_than_end)
        if end_greater_than_start:
            print "end greater than start ", end_greater_than_start
            return False
        return True

    def get_free_time_blocks_after_adding_schedule_block(self, schedule_time_blocks):
        def _process_schedule_time_blocks(schedule_time_blocks, earliest_free_time):
            free_blocks = []
            for counter in range(0, len(schedule_time_blocks)):
                schedule_time_block = schedule_time_blocks[counter]
                _add_time_block_if_not_overlap_earliest_time(schedule_time_block, free_blocks, earliest_free_time)
                earliest_free_time = schedule_time_block.get()[self.end_key]
                _process_end_time_if_last_block(counter, schedule_time_blocks, earliest_free_time, free_blocks)
            return free_blocks

        def _add_time_block_if_not_overlap_earliest_time(schedule_time_block, free_blocks, earliest_free_time):
            if not schedule_time_block.get()[self.start_key] == earliest_free_time:
                free_blocks.append(TimeBlock(**{self.start_key: earliest_free_time,
                                                self.end_key: schedule_time_block.get()[self.start_key]}))

        def _process_end_time_if_last_block(counter, schedule_time_blocks, earliest_free_time, free_blocks):
            if counter == len(schedule_time_blocks)-1:
                free_blocks.append(TimeBlock(**{self.start_key: earliest_free_time, self.end_key: self.availability_end}))

        if not schedule_time_blocks:
            return self._return_all_free()
        schedule_time_blocks = TimeUtility().sort_times(schedule_time_blocks)
        earliest_free_time = self.availability_start
        return _process_schedule_time_blocks(schedule_time_blocks, earliest_free_time)


    def _return_all_free(self):
        free_blocks = [TimeBlock(**{self.start_key: self.availability_start, self.end_key: self.availability_end})]
        return free_blocks
