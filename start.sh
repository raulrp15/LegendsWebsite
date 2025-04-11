#!/bin/bash

# Instalar Bun
curl -fsSL https://bun.sh/install | bash

# Exportar PATH de Bun
export PATH="/home/render/.bun/bin:$PATH"

# Instalar Reflex globalmente con pipx
pip install pipx
pipx ensurepath
pipx install reflex

# Exportar path de pipx (por si acaso)
export PATH="$HOME/.local/bin:$PATH"

# Ejecutar Reflex en modo producción
reflex run --env prod