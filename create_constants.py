import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
table_name = 'documents_app_constants'
data_list = [['standart_deduction_low_sallary', 'Стандартный вычет для граждан с низким налогооблагаемым доходом', 102.15],
             ['standart_deduction_child_under_18', 'Стандартный вычет на детей до 18 лет и других ижд.', 30.00],
             ['standart_deduction_child_under_18_lte_2', 'Стандартный вычет на двоих или более детей до 18 лет', 57.00],
             ['standart_deduction_disabled_child_under_18', 'Стандартный вычет на детей инвалидов до 18 лет', 57.00],
             ['standart_deduction_if_legal_guardian_status', 'Стандартный вычет ребенок до 18 лет и (или) ижд. для \
одиноких родителей, приемных родителей, опекунов и попечителей', 57.00],
             ['standart_deduction_some_categories_of_citizens', 'Стандартный вычет для отдельных категорий граждан',144.00],
             ['free_tax_sallary', 'Налогонеоблогаемый доход', 620.00]
             ]
for i in data_list:
    print((table_name, i[0], i[1], i[2]))
    c.execute('INSERT INTO %s ("coding_constant_name","constant_name","constant_value") VALUES ("%s","%s",%s)' %(table_name, i[0], i[1], i[2]))
conn.commit()