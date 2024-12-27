#!/bin/sh

source $(pwd)/.env
docker compose up -d --remove-orphans
echo "Success..."

