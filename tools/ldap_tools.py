from .ldap_core import get_ldap_connection
from configs.settings import BASE_DN

def get_current_user_info():
    """
    Devuelve toda la información del usuario actual (admin).
    """
    try:
        conn = get_ldap_connection()
        conn.search(
            search_base=BASE_DN,
            search_filter="(cn=admin)",
            attributes=["*"]
        )
        return conn.entries
    except Exception as e:
        print(f"Error al obtener info del usuario actual: {e}")
        return []

def get_user_groups(username):
    """
    Devuelve los nombres de los grupos a los que pertenece el usuario con cn=username.
    """
    try:
        conn = get_ldap_connection()

        user_dn = f"cn={username},ou=users,{BASE_DN}"
        group_search_base = f"ou=groups,{BASE_DN}"
        group_filter = f"(member={user_dn})"

        conn.search(
            search_base=group_search_base,
            search_filter=group_filter,
            attributes=["cn"]
        )

        return [entry.cn.value for entry in conn.entries]

    except Exception as e:
        print(f"Error al buscar grupos del usuario '{username}': {e}")
        return []

def get_all_users():
    """
    Devuelve una lista con todos los usuarios en LDAP (sus CNs).
    """
    try:
        conn = get_ldap_connection()
        search_base = f"ou=users,{BASE_DN}"
        search_filter = "(objectClass=inetOrgPerson)"
        attributes = ["cn"]

        conn.search(
            search_base=search_base,
            search_filter=search_filter,
            attributes=attributes
        )

        return [entry.cn.value for entry in conn.entries]

    except Exception as e:
        print(f"Error al obtener la lista de usuarios: {e}")
        return []

def get_all_groups():
    """
    Devuelve una lista con todos los grupos definidos en LDAP (sus CNs).
    """
    try:
        conn = get_ldap_connection()
        search_base = f"ou=groups,{BASE_DN}"
        search_filter = "(objectClass=groupOfNames)"
        attributes = ["cn"]

        conn.search(
            search_base=search_base,
            search_filter=search_filter,
            attributes=attributes
        )

        return [entry.cn.value for entry in conn.entries]

    except Exception as e:
        print(f"Error al obtener la lista de grupos: {e}")
        return []
