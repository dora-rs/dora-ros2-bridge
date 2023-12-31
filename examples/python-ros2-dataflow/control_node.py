#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from dora_ros2_bridge import Node
import pyarrow as pa

node = Node()

for i in range(500):
    event = node.next()
    if event is None:
        break
    if event["type"] == "INPUT":
        print(
            f"""Node received:
    id: {event["id"]},
    value: {event["data"]},
    metadata: {event["metadata"]}"""
        )
        node.send_output(
            "direction",
            pa.array(
                [1, 0, 0, 0, 0, 1],
                type=pa.uint8(),
            ),
        )
