import re

with open("input.txt", "r") as f:
    input = f.read()

required_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def validate_hgt(height):
    m = re.match("^(\d+)cm$", height)
    if m:
        value = int(m.group(1))
        if value > 193 or value < 150:
            return False
        return True

    m = re.match("^(\d+)in$", height)
    if m:
        value = int(m.group(1))
        if value > 76 or value < 59:
            return False
        return True

    return False


field_validators = {
    "byr": lambda x: re.match("^\d{4}$", x) and int(x) <= 2002 and int(x) >= 1920,
    "iyr": lambda x: re.match("^\d{4}$", x) and int(x) <= 2020 and int(x) >= 2010,
    "eyr": lambda x: re.match("^\d{4}$", x) and int(x) <= 2030 and int(x) >= 2020,
    "hgt": validate_hgt,
    "hcl": lambda x: re.match("^#[0-9a-f]{6}$", x),
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: re.match("^\d{9}$", x),
}

passports = input.split("\n\n")

count_valid = 0

for passport in passports:
    passport_info = {}
    for kvpair in passport.split():
        key, value = kvpair.split(":")
        passport_info[key] = value

    passport_keys = set(passport_info.keys())

    if required_fields.issubset(passport_keys):
        failed = False
        for key in passport_keys:
            if key in field_validators:
                if not field_validators[key](passport_info[key]):
                    print(f"Validation failed for {key}:{passport_info[key]}")
                    failed = True
        if not failed:
            count_valid += 1


print(count_valid)
