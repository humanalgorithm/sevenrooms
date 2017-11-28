import datetime as dt
from reservation import TimeBlock


class TimeUtility():
    def sort_times(self, time_block_list):
        sorted_list = sorted(time_block_list, key=lambda k: k.start)
        return sorted_list


class TimeCalculuation():
    def __init__(self):
        self.availability_start = dt.time(17, 0, 0)
        self.availability_end = dt.time(21, 0, 0)
        self.availability_extended = dt.time(22, 0, 0)

    def get_reservation_time_can_be_added(self, schedule_time_blocks, time_block):
        if time_block.start > self.availability_end or time_block.end < self.availability_start:  # within range
            return False
        if time_block.start < self.availability_end and time_block.end >= self.availability_end:
            duration = dt.datetime.combine(dt.date.min, time_block.end) - dt.datetime.combine(dt.date.min, self.availability_end)
            if duration > dt.timedelta(hours=1):  # doesn't go 61 mins over end
                return False

        schedule_time_blocks = TimeUtility().sort_times(schedule_time_blocks)
        start_less_than_end = filter(lambda x: x.start <= time_block.end, schedule_time_blocks)
        end_greater_than_start = filter(lambda x: x.end > time_block.start, start_less_than_end)
        if end_greater_than_start:
            return False
        return True

    def compute_free_blocks(self, schedule_time_blocks):
        def _process_schedule_time_blocks(schedule_time_blocks):
            free_time_blocks = []
            _process_first_block(schedule_time_blocks[0], free_time_blocks)
            _process_loop_blocks(schedule_time_blocks, free_time_blocks)
            _process_last_block(schedule_time_blocks, free_time_blocks)
            return free_time_blocks

        def _process_first_block(schedule_time_block, free_time_blocks):
            if self.availability_start == schedule_time_block.start:
                return
            free_time_blocks.append(TimeBlock(self.availability_start, schedule_time_block.start))

        def _process_loop_blocks(schedule_time_blocks, free_time_blocks):
            for counter in range(0, len(schedule_time_blocks)):
                start_time = schedule_time_blocks[counter].end
                end_time = _get_next_schedule_time_block_start(schedule_time_blocks, counter)
                if end_time and (start_time != end_time):
                    free_time_blocks.append(TimeBlock(start=start_time, end=end_time))

        def _get_next_schedule_time_block_start(schedule_time_blocks, counter):
            if counter + 1 < len(schedule_time_blocks):
                return schedule_time_blocks[counter + 1].start

        def _process_last_block(schedule_time_blocks, free_time_blocks):
            last_block = schedule_time_blocks[len(schedule_time_blocks) - 1]
            if self.availability_end == last_block.end:
                return
            if last_block.end < self.availability_end:
                free_time_blocks.append(TimeBlock(last_block.end, self.availability_end))

        def _return_all_free():
            free_blocks = [TimeBlock(start=self.availability_start, end=self.availability_end)]
            return free_blocks

        if not schedule_time_blocks:
            return _return_all_free()
        schedule_time_blocks = TimeUtility().sort_times(schedule_time_blocks)
        return _process_schedule_time_blocks(schedule_time_blocks)
