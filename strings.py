#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import math
import sys
import uuid
from uuid import UUID


def get_size(data: str) -> int:
    size = sys.getsizeof(data)
    return size


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"

    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")

    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)

    return "%s %s" % (s, size_name[i])


def is_special(charvalue: str) -> bool:
    special = any(ord(char) > 126 for char in charvalue)

    return special


def generate_id_seed() -> UUID:
    """
    UUID based on the host ID and current time

    :return:
    """
    unique_id = uuid.uuid1()
    return unique_id


def generate_id() -> UUID:
    """
    Random UUID

    :return:
    """
    unique_id = uuid.uuid4()
    return unique_id
