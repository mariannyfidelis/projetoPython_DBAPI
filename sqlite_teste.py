import sqlite3

#Sqlite connection
conn = sqlite3.connect(":memory:")

t = int(input())

if(conn and isinstance(conn,sqlite3.Connection)):
    print("Conexão realizada!")
else:
    print("A conexão não foi realizada!")

for n in range(0, t):
    eval(input())

c = conn.cursor()
c.execute("SELECT * FROM acoes")
linhas = c.fetchall()

col_width = [max(len(str(x)) + 2 for x in col) for col in zip(*linhas)]

for a in linhas:
    print("| {:<{align_col_0}} | {:<{align_col_1}} | {:<{align_col_2}} | {:<{align_col_3}} | {:<{align_col_4}}"
          .format(a[0], a[1], a[2], a[3], a[4],
                  align_col_0=col_width[0], 
                  align_col_1=col_width[1],
                  align_col_2=col_width[2],
                  align_col_3=col_width[3],
                  align_col_4=col_width[4]))

c.execute("INSERT INTO acoes VALUES ('2019-01-05','COMPRA','APB55',24,50.27)")

print(c.lastrowid)
                  
conn.close()