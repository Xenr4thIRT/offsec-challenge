from tools.ldap_tools import get_current_user_info, get_user_groups, get_all_users, get_all_groups

TOOL_REGISTRY = {
    "get_current_user_info": {
        "func": get_current_user_info,
        "description": "Devuelve la información del usuario actual (admin).",
        "example": "¿Quién soy? / ¿Cuál es mi información?"
    },
    "get_user_groups": {
        "func": get_user_groups,
        "description": "Devuelve los grupos a los que pertenece un usuario.",
        "example": "¿Qué grupos tengo? / ¿Qué grupos tiene john.doe?"
    },
    "get_all_users": {
        "func": get_all_users,
        "description": "Devuelve la lista de todos los usuarios en el LDAP.",
        "example": "¿Qué usuarios existen?"
    },
    "get_all_groups": {
        "func": get_all_groups,
        "description": "Devuelve la lista de todos los grupos definidos en el LDAP.",
        "example": "¿Qué grupos existen?"
    }
}

def list_tools():
    return [
        f"- {name}: {data['description']} | Ejemplo: {data['example']}"
        for name, data in TOOL_REGISTRY.items()
    ]
