import subprocess
import re

NUMBERS_I_USE = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

output = subprocess.Popen("i3-msg -t get_workspaces | python -m json.tool | grep num",
                          shell=True, stdout=subprocess.PIPE).stdout.read()
output = str(output)

nums_in_use = re.findall(r'\d+', output)
nums_in_use = [int(num) for num in nums_in_use]
nums_in_use = set(nums_in_use)
nums_not_used = list(NUMBERS_I_USE - nums_in_use)
nums_not_used = sorted(nums_not_used)

subprocess.call(['notify-send', str(nums_not_used), '-t', '2'])
