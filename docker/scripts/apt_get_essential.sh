#!/bin/bash
set -eou pipefail

apt-get update && apt-get install -y  --no-install-recommends \
    apt-utils=2.0.9 \
    ca-certificates=20230311ubuntu0.20.04.1 \
    curl=7.68.0-1ubuntu2.19 \
    && \
    update-ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
