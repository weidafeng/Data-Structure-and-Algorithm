# 出勤记录不多于1个A(absance), 或者不超过两个连续的L（late）,则可以获得奖励

def reward(record):
    if record.count('A') or 'LLL' not in record:
        print("congratulations!")
        return True
    return False

record = 'ABBLL'
reward(record)