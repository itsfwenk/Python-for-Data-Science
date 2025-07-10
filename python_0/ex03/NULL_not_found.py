import math

def NULL_not_found(object: any) -> int:
    return_code = 0

    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif isinstance(object, float) and math.isnan(object):
        print(f"Cheese: {object} {type(object)}")
    elif object == 0 and type(object) is int:
        print(f"Zero: {object} {type(object)}")
    elif object == '' and type(object) is str:
        print(f"Empty: {type(object)}")
    elif object is False:
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not Found")
        return_code = 1

    return return_code

# tester.py
# from NULL_not_found import NULL_not_found
# Nothing = None
# Garlic = float("NaN")
# Zero = 0
# Empty = ''
# Fake = False
# NULL_not_found(Nothing)
# NULL_not_found(Garlic)
# NULL_not_found(Zero)
# NULL_not_found(Empty)
# NULL_not_found(Fake)
# print(NULL_not_found("Brian"))