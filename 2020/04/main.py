import re
file = open("input.txt", 'r').read()
file = file.split("\n\n")

# part 1
# valid = 0
# for row in file:
#     row = row.replace("\n"," ")
#     row = row.split(" ")
#     fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
#     for var in row:
#         var = var.split(":")
#         if var[0] in fields:
#             fields.remove(var[0])
#     if fields == [] or (len(fields)==1 and fields[0]=="cid"):
#         valid+=1
# print(valid)

# part 2


def validate_field(k,v):
    if k == "byr":
        if int(v) >= 1920 and int(v)<=2002:
            return True
    if k == "iyr":
        if int(v) >= 2010 and int(v) <= 2020:
            return True
    if k == "eyr":
        if int(v) >= 2020 and int(v) <= 2030:
            return True
    if k == "hgt":
        if "cm" in v:
            v = v.replace("cm","")
            if int(v) >= 150 and int(v) <= 193:
                return True
        if "in" in v:
            v = v.replace("in","")
            if int(v) >= 59 and int(v) <= 76:
                return True
    if k == "hcl":
        regex = re.search(r"#[0-9a-f]{6}",v)
        if regex is not None and len(v) == 7:
            return True
    if k == "ecl":
        if v in ["amb","blu","brn","gry","grn","hzl","oth"]:
            return True
    if k == "pid":
        if len(v) == 9 and re.search(r"[0-9]{9}",v):
            return True
    if k == "cid":
        return True
    return False


valid = 0
for row in file:
    row = row.replace("\n"," ")
    row = row.split(" ")
    fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
    for var in row:
        var = var.split(":")
        k = var[0]
        v = var[1]
        is_valid = validate_field(k,v)
        if var[0] in fields and is_valid == True:
            fields.remove(var[0])
    if fields == [] or (len(fields)==1 and fields[0]=="cid"):
        valid+=1
print(valid)






