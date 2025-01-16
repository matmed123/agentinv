# AgenteInv

Aplicación de análisis y simulación de inversiones en criptomonedas con IA integrada.

## Instalación

1. Requisitos previos:
   - Python 3.10+
   - pip 22.0+

2. Crear entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate.bat # Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
```bash
cp .env.example .env
```

## Estructura del Proyecto

```
agenteinv/
├── backend/           # Lógica de negocio
├── ui/               # Interfaces gráficas
├── config/           # Configuraciones
├── tests/            # Pruebas
└── logs/             # Archivos de log
```

## Uso

```bash
python main.py
```

## Testing

```bash
pytest
```

## Licencia

MIT
