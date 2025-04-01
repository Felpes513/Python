import re
import sys

# Captura todas as linhas digitadas pelo usuário
print("Digite o texto a ser analisado (pressione Ctrl+D para finalizar):")
texto = sys.stdin.read()

# Expressões Regulares
padrao_data = r"data_exame:\s*([\d/]+\s[\d:]+)"
padrao_empresa = r"empresa_id:\s*(\d+)"
padrao_studies = r"studies_iuid:\s*([\d.]+)"

# Encontrando todos os exames
datas_exames = re.findall(padrao_data, texto)
empresas_ids = re.findall(padrao_empresa, texto)
studies_iuids = re.findall(padrao_studies, texto)

# Verificando se há exames encontrados
if datas_exames and empresas_ids and studies_iuids:
    print("\n✅ Dados extraídos:")
    for i in range(len(datas_exames)):
        print(f"\n🔹 Exame {i+1}:")
        print(f"📅 Data do Exame: {datas_exames[i]}")
        print(f"🏢 Empresa ID: {empresas_ids[i]}")
        print(f"🔍 Studies IUID: {studies_iuids[i]}")
else:
    print("\n⚠ Nenhum exame encontrado! Verifique se os dados foram inseridos corretamente.")