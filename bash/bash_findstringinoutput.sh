#!/usr/bin/env bash

needle='bash'

if [[ $(ps aux) =~ $needle ]]; then
  echo "matched"
fi