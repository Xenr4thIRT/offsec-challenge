# 🛡️ Desafío Técnico Offsec - Agente IA para LDAP

## 📌 Descripción General

Este proyecto resuelve el desafío técnico del equipo de Offensive Security de **Mercado Libre**, mediante un **sistema mono-agente de IA** que interactúa con un servidor **OpenLDAP** para resolver consultas utilizando herramientas específicas.

El sistema fue desarrollado en **Python**, con soporte para **Google Gemini 1.5 Flash**, e implementa las herramientas requeridas del desafío.

## 🧠 Arquitectura

```
Mono-agente LDAP
├── Agente Ejecutador
    ├── Gemini 1.5 Flash
    ├── Herramientas base y extendidas
    └── Conexión dinámica a OpenLDAP
```

## 🧐 Capacidades Implementadas

### Herramientas base (requeridas):
- `get_current_user_info()`: Devuelve la información del usuario actual (admin).
- `get_user_groups(username)`: Devuelve los grupos a los que pertenece un usuario.

### Herramientas adicionales (implementadas):
- `get_all_users()`: Devuelve todos los usuarios registrados.
- `get_all_groups()`: Devuelve todos los grupos existentes en LDAP.

## 📁 Estructura del Proyecto

```
offsec_challenge/
├── agents/
│   └── mono_agent.py        # Lógica del agente principal
├── tools/
│   ├── ldap_core.py         # Conexion al servidor LDAP
│   ├── ldap_tools.py        # Implementación de herramientas
│   └── tool_registry.py     # Registro de herramientas disponibles
├── configs/
│   └── settings.py          # Variables de entorno (dotenv)
├── open_ldap_files/         # Infraestructura LDAP (docker)
├── README.md
├── main.py
├── pyproject.toml
└── poetry.lock
```

## 🚀 Ejecución

### 1. Clona el repositorio

```bash
git clone https://github.com/Xenr4thIRT/offsec-challenge
cd offsec-challenge
```

### 2. Configura el entorno

```bash
cp .env.example .env
nano .env
# Completen las variables con la configuración (como la API key de Gemini, etc.)
```

### 3. Levanta el entorno LDAP

```bash
cd open_ldap_files
./setup-ldap.sh
```

### 4. Activa el entorno virtual y ejecutá

```bash
poetry install
poetry shell
poetry run python main.py
```

## 🦺 Ejemplos de uso

```bash
🔍 Consulta LDAP >> ¿quién soy?
🔍 Consulta LDAP >> ¿qué grupos tengo?
🔍 Consulta LDAP >> ¿qué usuarios existen?
🔍 Consulta LDAP >> ¿qué grupos existen?
```

## 🧰 Tecnologías

- 🐍 Python 3.10
- 🧠 Gemini 1.5 Flash (Google Generative AI)
- 📆 Poetry
- 📚 OpenLDAP + phpLDAPAdmin
- 🔐 python-ldap3

## ✅ Checklist del Challenge

| Requisito                                 | Estado      |
|------------------------------------------|-------------|
| Conectividad con servidor LDAP           | ✅ Completo |
| Uso de Gemini (IA generativa)            | ✅ Completo |
| Herramientas base (`get_user_groups`)    | ✅ Completo |
| Herramientas base (`get_current_user_info`) | ✅ Completo |
| Implementación simple y funcional        | ✅ Completo |
| Herramientas extra                       | ✅ Incluidas (`get_all_users`, `get_all_groups`) |
| Auto-generación de herramientas          | ❌ No implementado |
| Reset del sistema                        | ❌ No implementado |
| Logging / Manejo de errores              | ✅ Básico incluido |
| Documentación           | ✅ Este README |

---

## 📬 Contacto

Desarrollado por **Miguel Larreal Acosta** - *candidato para el equipo de Offensive Security de Mercado Libre*.
