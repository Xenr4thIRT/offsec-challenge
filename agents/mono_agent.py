import google.generativeai as genai
from tools.tool_registry import TOOL_REGISTRY, list_tools
from tools.ldap_tools import get_current_user_info, get_user_groups
from configs.settings import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-flash")


def run_agent():
    print("Mono-agente LDAP listo. Escribí 'salir' para terminar.")
    print("Escribí 'herramientas' para listar capacidades actuales.\n")

    while True:
        query = input("Consulta LDAP >> ").strip().lower()

        if query in ["exit", "salir", "quit"]:
            print("Saliendo del agente.")
            break

        if query in ["herramientas", "tools", "capacidades"]:
            print("\nHerramientas disponibles:")
            for tool in list_tools():
                print(tool)
            print("")
            continue

        prompt = f"""
Eres un agente IA conectado a un servidor LDAP.

Dispones de estas herramientas:
- get_current_user_info
- get_user_groups
- get_all_users
- get_all_groups

Dado este mensaje del usuario:
\"{query}\"

Responde únicamente con el nombre exacto de la herramienta que deberías usar, sin ningún texto adicional.
Ejemplo de respuesta válida: get_user_groups
"""

        try:
            response = model.generate_content(prompt)
            tool_name = response.text.strip().split()[0]  # respuesta esperada: nombre de función
        except Exception as e:
            print(f"Error al consultar Gemini: {e}")
            continue

        tool = TOOL_REGISTRY.get(tool_name)
        if not tool:
            print("No tengo una herramienta para responder esa consulta aún.")
            continue

        print(f"Ejecutando herramienta: {tool_name}")

        if tool_name == "get_current_user_info":
            try:
                for entry in get_current_user_info():
                    print(entry)
            except Exception as e:
                print(f"Error ejecutando la herramienta: {e}")

        elif tool_name == "get_user_groups":
            try:
                if "de" in query:
                    username = query.split("de")[-1].strip().replace("?", "")
                else:
                    username = "admin"
                grupos = get_user_groups(username)
                if not grupos:
                    print(f"El usuario '{username}' no tiene grupos o no fue encontrado.")
                for group in grupos:
                    print("-", group)
            except Exception as e:
                print(f"Error ejecutando la herramienta: {e}")

        elif tool_name == "get_all_users":
            try:
                from tools.ldap_tools import get_all_users
                usuarios = get_all_users()
                if not usuarios:
                    print("No se encontraron usuarios.")
                for usuario in usuarios:
                    print("-", usuario)
            except Exception as e:
                print(f"Error ejecutando la herramienta: {e}")

        elif tool_name == "get_all_groups":
            try:
                from tools.ldap_tools import get_all_groups
                grupos = get_all_groups()
                if not grupos:
                    print("No se encontraron grupos.")
                for grupo in grupos:
                    print("-", grupo)
            except Exception as e:
                print(f"Error ejecutando la herramienta: {e}")

        else:
            print("Herramienta reconocida pero no implementada aún.")
