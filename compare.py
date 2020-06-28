#!/usr/bin/env python3

import re

from typing import Tuple, List
from pprint import pprint

MrsFragment = Tuple[str, List[str], str]

def compare(mrsString1: str, mrsString2: str) -> bool:
    return _normalize(mrsString1) == _normalize(mrsString2)

def _normalize(mrsString: str) -> MrsFragment:
    mrsString = re.sub(r"(\b\w)\d+", "\\1_", mrsString)
    intro, eps, end = _parse(mrsString)
    return intro, sorted(eps), end

def _parse(mrsString: str) -> MrsFragment:
    intro, rest = mrsString.split("RELS: <", 1)
    epsString, end = rest.split(" > ", 1)
    counter = 0
    i = 0
    d = 0
    eps = []
    while i < len(epsString):
        c = epsString[i]
        if c == "[":
            if d == 0:
                start = i
            d += 1
        elif c == "]":
            if d == 0:
                raise Exception("Invalid MRS")
            d -= 1
            if d == 0:
                eps.append(epsString[start:i+1])
                start = None
        i += 1
    return intro, eps, end
