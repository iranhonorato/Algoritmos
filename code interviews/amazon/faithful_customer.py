


def faithful_customer(log1:list[dict], log2:list[dict]) -> list:
    ans = list()

    customer_log1 = {}

    for i in range(len(log1)):
        if log1[i]["client_id"] not in customer_log1:
            customer_log1[log1[i]["client_id"]] = [log1[i]["page_id"]]

        else: 
            customer_log1[log1[i]["client_id"]].append(log1[i]["page_id"])

    for j in range(len(log2)):
        if log2[j]["client_id"] in customer_log1 and log2[j]["page_id"] not in customer_log1[log2[j]["client_id"]]:
            ans.append(log2[j]["client_id"])

    return ans

logs_dia_1 = [
    {"timestamp": "2026-10-01", "client_id": 10, "page_id": 1},
    {"timestamp": "2026-10-01", "client_id": 20, "page_id": 1},
    {"timestamp": "2026-10-01", "client_id": 30, "page_id": 3},
]

logs_dia_2 = [
    {"timestamp": "2026-10-02", "client_id": 10, "page_id": 2}, # Entra (Dia 1: {1}, Dia 2: {2})
    {"timestamp": "2026-10-02", "client_id": 20, "page_id": 1}, # Não entra (Repetiu a página 1)
    {"timestamp": "2026-10-02", "client_id": 30, "page_id": 3}, # Não entra (Repetiu a página 3)
    {"timestamp": "2026-10-02", "client_id": 30, "page_id": 4},
]

resultado = faithful_customer(logs_dia_1, logs_dia_2)
print("Usuários válidos:", resultado)
