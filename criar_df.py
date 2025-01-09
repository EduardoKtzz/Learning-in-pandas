import pandas as pd #Importar o pandas

#Criar um DataFrame e definir dados dentro dele
df = pd.DataFrame(
    {
        "Email":[
            "marianadequeiroz92@gmail.com",
            "luisa25sp@gmail.com",
            "eudilanesilva@yahoo.com.br",
                 ],

        "CPF":[
            "66865426322",
            "66865463222",
            "09235434522",
            ],

        "Idade":["22", "17", "25"],

        "Aprovado":["Sim", "Não", "Não"],

    }
)

#Exibir tabela completa
print(df.head())

# .max() - Exibir o mmaior resultado dos números
# .describe() - Exibe estatiticas sobre os dados da planilha
print("A maior idade é:",df["Idade"].max(), "anos!")
print(df.describe())