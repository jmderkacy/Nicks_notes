
import re

regex = r"(?<=\{)(.*?)(?=\})"

test_str = ("Some random stuff in here {image 1 url}[name]\n"
    "Some random stuff in here {image 2 url}|name|\n"
    "Some random stuff in here {image 3 url}[name|")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
