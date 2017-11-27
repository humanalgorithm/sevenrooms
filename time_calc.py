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

    def compute_free_blocks(self, schedule_time_blocks):
        def _process_schedule_time_blocks(schedule_time_blocks, free_time_blocks):
            earliest_time = self.availability_start
            for counter in range(0, len(schedule_time_blocks)):
                latest_time = _get_latest_time(counter, schedule_time_blocks)
                _process_block(schedule_time_blocks[counter], free_time_blocks, earliest_time, latest_time)
                earliest_time = schedule_time_blocks[counter].get()[self.end_key]
                _process_if_last_block(schedule_time_blocks, counter)
            return free_time_blocks

        def _get_latest_time(counter, schedule_time_blocks):
            if counter+1 < len(schedule_time_blocks):
                return schedule_time_blocks[counter+1].get()[self.start_key]
            else:
                return self.availability_end

        def _process_block(schedule_time_block, free_time_blocks, earliest_time, latest_time):
            schedule_block_start = schedule_time_block.get()[self.start_key]
            schedule_block_end = schedule_time_block.get()[self.end_key]
            if schedule_block_start == self.availability_start:
                earliest_time = schedule_block_end
            if schedule_block_start >= earliest_time and schedule_block_end <= latest_time:
                free_time_blocks.append(TimeBlock(**{self.start_key: earliest_time,
                     self.end_key: schedule_time_block.get()[self.start_key]}))

        def _process_if_last_block(schedule_time_blocks, counter):
            if counter == len(schedule_time_blocks)-1:
                free_time_blocks.append(TimeBlock(**{self.start_key: schedule_time_blocks[counter].get()[self.end_key],
                     self.end_key: self.availability_end}))

        def _return_all_free():
            free_blocks = [TimeBlock(**{self.start_key: self.availability_start, self.end_key: self.availability_end})]
            return free_blocks

        if not schedule_time_blocks:
            return _return_all_free()
        schedule_time_blocks = TimeUtility().sort_times(schedule_time_blocks)
        free_time_blocks = []
        return _process_schedule_time_blocks(schedule_time_blocks, free_time_blocks)

    '''
    def compute_free_blocks(self, schedule_time_blocks):
        def _process_schedule_time_blocks(schedule_time_blocks, earliest_free_time):
            free_blocks = []
            for counter in range(0, len(schedule_time_blocks)):
                schedule_time_block = schedule_time_blocks[counter]
                _add_time_block_if_not_overlap_earliest_time(schedule_time_block, free_blocks, earliest_free_time)
                earliest_free_time = schedule_time_block.get()[self.end_key]
                _process_end_time_if_last_block(counter, schedule_time_blocks, earliest_free_time, free_blocks)
            return free_blocks

        def _add_time_block_if_not_overlap_earliest_time(schedule_time_block, free_blocks, earliest_free_time):
            if schedule_time_block.get()[self.start_key] >= earliest_free_time:
                free_blocks.append(TimeBlock(**{self.start_key: earliest_free_time,
                                                self.end_key: schedule_time_block.get()[self.start_key]}))

        def _process_end_time_if_last_block(counter, schedule_time_blocks, earliest_free_time, free_blocks):
            if counter == len(schedule_time_blocks)-1:
                free_blocks.append(TimeBlock(**{self.start_key: earliest_free_time, self.end_key: self.availability_end}))


        schedule_time_blocks = TimeUtility().sort_times(schedule_time_blocks)
        earliest_free_time = self.availability_start
        return _process_schedule_time_blocks(schedule_time_blocks, earliest_free_time)
    '''