#!/usr/bin/env bash

objdump -d "$1" |grep -E '^( +)([0-9a-f]+):' |awk -F'\t' '{print $2}' |tr -d '\n' |sed -e 's/ \+/ /g' -e 's/ $//g' -e 's/^/ /g' -e 's/ /\\x/g'; echo
