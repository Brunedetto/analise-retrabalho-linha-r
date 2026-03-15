import pandas as pd
import numpy as np

# 1. Criar 30 dias de produção
datas = pd.date_range(start="2024-04-01", periods=30)

# 2. Criar estrutura base
df = pd.DataFrame({
    "data": datas,
    "turno": "Tarde",
    "linha": "R"
})

# 3. Definir semente para manter padrão fixo
np.random.seed(42)

# 4. Simular produção diária (7500 a 9000)
df["producao_total"] = np.random.randint(7500, 9000, size=30)

# 5. Simular taxa normal de retrabalho (2% a 5%)
df["taxa_retrabalho"] = np.random.uniform(0.02, 0.05, size=30)

# 6. Calcular peças retrabalhadas
df["pecas_retrabalho"] = (df["producao_total"] * df["taxa_retrabalho"]).astype(int)

# 7. Definir custo unitário
df["custo_unitario"] = 0.50

# 8. Calcular impacto financeiro
df["impacto_financeiro"] = df["pecas_retrabalho"] * df["custo_unitario"]

print(df.head())