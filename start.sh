#!/bin/bash

# Instalar Bun
curl -fsSL https://bun.sh/install | bash

# Exportar PATH para usar la versión nueva de Bun
export PATH="/home/render/.bun/bin:$PATH"

# Correr Reflex en modo producción
reflex run --env prod