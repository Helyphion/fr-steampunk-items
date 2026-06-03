# this script was not made with publishing in mind, so it has no safeguards for incorrect input or anything like that
# I've mostly just included it for completion's sake (and so I can easily find it again)

ids = input()

split_ids = str(ids).split(",")

output = ""

for x in split_ids:
    output += "[gamedb item=" + x + "]\n"

output = "[size=2]" + output[:-1] + "[/size]"

print(output)

""" scratchpad:
https://www1.flightrising.com/dgen/dressing-room/dummy?breed=8&gender=0&skin=0&apparel=363,368,428,387,392,31590,433,438&xt=dressing.png














"""
