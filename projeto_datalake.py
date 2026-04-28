# %%
# Projeto Data Lake - Leitura de Arquivo Parquet do AWS S3 usando Python
# %%
import boto3
import pandas as pd
import io
import pyarrow.parquet as pq
from sqlalchemy import create_engine


# %%
database_URL = 'postgresql://postgres.ctggdythmubrpqynmtjn:iKH4VO9S2igRJxJo@aws-1-us-east-1.pooler.supabase.com:5432/postgres'
# %%
# Configurações dos parametros AWS S3
S3_ENDPOINT_URL = "https://ctggdythmubrpqynmtjn.storage.supabase.co/storage/v1/s3"
AWS_REGION = "us-east-1"
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_KEY_ID = ""
BUCKET_NAME = "meu_bucket"
PASSWORD_URL = "https://ctggdythmubrpqynmtjn.storage.supabase.co/storage/v1/s3"

#%%
# Inicializa o cliente S3
s3_client = boto3.client('s3',
                          endpoint_url=S3_ENDPOINT_URL,
                          region_name=AWS_REGION,
                          aws_access_key_id=AWS_ACCESS_KEY_ID, 
                          aws_secret_access_key=AWS_SECRET_KEY_ID)
# %% Listar os buckets disponíveis
response = s3_client.list_buckets()['Buckets']
for bucket in response:
    print(bucket['Name'])
# %% Listar os objetos no bucket especificado
response = s3_client.list_objects(Bucket=BUCKET_NAME)# 
 
# %% Listar os arquivos no bucket especificado
arquivos = [obj["Key"] for obj in response["Contents"]]
for arquivos_parquet in arquivos:
  print(arquivos_parquet)
# %% Pegar arquivo Parquet do S3 e ler com Pandas
FILE_KEY = "produtos.parquet"
response = s3_client.get_object(Bucket=BUCKET_NAME, Key=FILE_KEY)
parquet_bytes = response["Body"].read()
dfProdutos = pd.read_parquet(io.BytesIO(parquet_bytes))
type(parquet_bytes)
# %%

# %% Visualizar as primeiras linhas do DataFrame
dfProdutos.head(5)
#%% Visualizar as últimas linhas do DataFrame
dfProdutos.tail(5)
#%% Visualizar o número de linhas e colunas do DataFrame
dfProdutos.shape
#%%
#Visualizar o tipo de dados de cada coluna
dfProdutos.dtypes
#%%
#Visualizar as estatísticas descritivas do DataFrame
dfProdutos.describe()
#%%
#Visualizar o número de valores únicos em cada coluna
dfProdutos.nunique()

# %%

#Visualizar as colunas do DataFrame
dfProdutos.columns
# %%
dfProdutos.head()
# %%
dfProdutos.info()

# %% Cria a conexão com o banco de dados PostgreSQL usando SQLAlchemy
engine = create_engine(database_URL)
# %% Salva o DataFrame no banco de dados PostgreSQL usando o método to_sql do Pandas
dfProdutos.to_sql('produtos', 
                  con=engine, 
                  if_exists='replace',
                  index=False) 
# %%
# %%
# %%
# %%
