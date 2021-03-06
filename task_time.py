import json
import sys

max_pause_to_count_as_continuous = 120

with open(sys.argv[1]) as file:
    data = json.load(file)
    sum_continuous = 0
    sum_total = 0
    last_timestamp = data[0].get("timestamp")
    for datapoint in data:
        cur_timestamp = datapoint.get("timestamp")
        if not cur_timestamp:
            continue
        delta = cur_timestamp - last_timestamp
        if delta < max_pause_to_count_as_continuous:
            sum_continuous += delta
        sum_total += delta
        last_timestamp = cur_timestamp
    print("Number of continuous time spent:", sum_continuous, "seconds, which is",
          sum_continuous/60, "minutes or", sum_continuous/3600, "hours")
    print("Number of total time spent:", sum_total, "seconds, which is",
          sum_total/60, "minutes or", sum_total/3600, "hours")
