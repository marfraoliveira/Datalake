# %%
import boto3
import pandas as pd
import io
import pyarrow.parquet as pq
# %%
# Configurações dos parametros AWS S3
S3_ENDPOINT_URL = "https://ctggdythmubrpqynmtjn.storage.supabase.co/storage/v1/s3"
AWS_REGION = "us-east-1"
AWS_ACCESS_KEY_ID = "091e4b53f0115bd1cddd68d626fe839b"
AWS_SECRET_KEY_ID = "4e366e2c070e200bf714844800e5675e94ba2eb75279fb2105d1d7a363bba085"
BUCKET_NAME = "meu_bucket"
#%%
# Inicializa o cliente S3
s3_client = boto3.client('s3',
                          endpoint_url=S3_ENDPOINT_URL,
                          region_name=AWS_REGION,
                          aws_access_key_id=AWS_ACCESS_KEY_ID, 
                          aws_secret_access_key=AWS_SECRET_KEY_ID)
# %%
response = s3_client.list_buckets()['Buckets']
for bucket in response:
    print(bucket['Name'])
# %%
response = s3_client.list_objects(Bucket=BUCKET_NAME)# 
 
# %%
# Listar os arquivos no bucket
arquivos = [obj["Key"] for obj in response["Contents"]]
for arquivos_parquet in arquivos:
  print(arquivos_parquet)
# %%
# Baixar arquivo Parquet do S3 e ler com Pandas 
FILE_KEY = "produtos.parquet"
response = s3_client.get_object(Bucket=BUCKET_NAME, Key=FILE_KEY)
parquet_bytes = response["Body"].read()
df = pd.read_parquet(io.BytesIO(parquet_bytes))
# %%

# %%
# Visualizar as primeiras linhas do DataFrame
df.head(5)
#%%Visualizar as últimas linhas do DataFrame
df.tail(5)
#%%
# Visualizar o número de linhas e colunas do DataFrame
df.shape
#%%
#Visualizar o tipo de dados de cada coluna
df.dtypes
#%%
#Visualizar as estatísticas descritivas do DataFrame
df.describe()
#%%
#Visualizar o número de valores únicos em cada coluna
df.nunique()

# %%

#Visualizar as colunas do DataFrame
df.columns
# %%

# %%
