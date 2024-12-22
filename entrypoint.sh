#!/bin/bash

if [ -z "$PYROUBOT_KEY" ]; then
  read -p "Masukkan kunci anda: " key
else
  key="$PYROUBOT_KEY"
fi

clear

git pull && python3 -m PyroUbot "$key"
