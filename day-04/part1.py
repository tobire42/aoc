with open("input.txt", "r") as f:
    input = f.read()

required_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

passports = input.split("\n\n")

count_valid = 0

for passport in passports:
    passport_info = {}
    for kvpair in passport.split():
        key, value = kvpair.split(":")
        passport_info[key] = value

    passport_keys = set(passport_info.keys())

    if required_fields.issubset(passport_keys):
        count_valid += 1


print(count_valid)
