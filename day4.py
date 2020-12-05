import re

f = open('day4.data', 'r')
data = f.read()
passports = data.split('\n\n')
passports = [p.replace('\n', ' ')
                 .replace(' ', ',')
                 .replace(':', '\":\"')
                 .replace(',', '\",\"')
             for p in passports]

passports = [eval('{\"' + p + '\"}') for p in passports]
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  # ignore 'cid' field
num_valid = 0


def valid_fields(p):
    byr = True if 1920 <= int(p['byr']) <= 2002 else False
    iyr = True if 2010 <= int(p['iyr']) <= 2020 else False
    eyr = True if 2020 <= int(p['eyr']) <= 2030 else False

    hgt_unit = p['hgt'][-2:]
    if hgt_unit == 'cm':
        hgt_num = int(p['hgt'][:-2])
        hgt = True if 150 <= hgt_num <= 193 else False
    elif hgt_unit == 'in':
        hgt_num = int(p['hgt'][:-2])
        hgt = True if 59 <= hgt_num <= 76 else False
    else:
        hgt = False
    hcl = True if len(re.findall(r"#[0-9a-z]{6}", p['hcl'])) > 0 else False
    ecl = True if p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] else False
    pid = True if len(p['pid']) == 9 and p['pid'].isdigit() else False

    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        return True
    else:
        return False


for p in passports:
    is_valid = True
    for f in required_fields:
        if f not in p.keys():
            is_valid = False
            break
    if is_valid and not valid_fields(p):
        is_valid = False
    if is_valid:
        num_valid += 1
print(num_valid)
