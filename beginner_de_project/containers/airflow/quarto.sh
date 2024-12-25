#!/bin/bash

curl -L -o /tmp/quarto-1.5.43-linux-amd64.tar.gz https://github.com/quarto-dev/quarto-cli/releases/download/v1.5.43/quarto-1.5.43-linux-amd64.tar.gz
mkdir -p /opt/quarto
tar -C /opt/quarto -xvzf /tmp/quarto-1.5.43-linux-amd64.tar.gz

ln -s /opt/quarto/quarto-1.5.43/bin/quarto /usr/local/bin/quarto
