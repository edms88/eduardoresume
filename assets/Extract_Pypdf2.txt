import re
import os
import PyPDF2
import openpyxl
import pandas as pd
import datetime as dt
import shutil
import time


teste = pd.DataFrame(columns=['cliente','cidade','num_serie','tipo_equip','dtinicio','dtfim'])
teste.to_excel('extracao.xlsx', index=False)


resumo_excel = openpyxl.load_workbook('extracao.xlsx')
resumo_sheet = resumo_excel['Sheet1']

for file_name in os.listdir(r'C:\Users\esilveira\Constat\Central de Serviços - Relatórios de Fechamento\pdfs'):
    print(file_name)
    load_pdf = open(r'C:\Users\esilveira\Constat\Central de Serviços - Relatórios de Fechamento\pdfs\\'+file_name,'rb')
    read_pdf = PyPDF2.PdfFileReader(load_pdf)
    page_count = read_pdf.getNumPages()
    first_page = read_pdf.getPage(0)
    page_content = first_page.extractText()
    page_content = page_content.replace('\n','')

    
    #print(page_content)

    #clientes
    cli = r'Cliente : [A-Z0-9.-]* [A-Z0-9.-]* [A-Z0-9.-]*'
    regex_cliente = re.compile(cli, flags=re.IGNORECASE)
    cliente = regex_cliente.search(page_content).group()
    
    #localidade
    city = r'[A-Z0-9.-]*/[A-Z0-9.-]* [A-Z0-9.-]* [A-Z0-9.-]* [A-Z0-9.-]*/[A-Z0-9.-]*[A-Z0-9.-]* [A-Z0-9.-]*'

    regex_city = re.compile(city, flags=re.IGNORECASE)
    cidade = regex_city.search(page_content).group()
    
    #N de serie
    nserie = r'Nº Série  [A-Z0-9.-]*'
    nserie = re.compile(nserie, flags=re.IGNORECASE)
    num_serie = nserie.search(page_content).group()
    

    #tipo de equip
    Modelo = r'Modelo:  [A-Z0-9.-]*'

    Modelo = re.compile(Modelo, flags=re.IGNORECASE)
    tipo_equip = Modelo.search(page_content).group()


    # Data de inicio
    inicio = r'Início:  [A-Z0-9.-]*/[A-Z0-9.-]*/[A-Z0-9.-]* [A-Z0-9.-]*:[A-Z0-9.-]*'
    tempo1 = re.compile(inicio, flags=re.IGNORECASE)
    dtinicio = tempo1.search(page_content).group()


    # Data termino
    termino = r'Término:  [A-Z0-9.-]*/[A-Z0-9.-]*/[A-Z0-9.-]* [A-Z0-9.-]*:[A-Z0-9.-]*'
    tempo2 = re.compile(termino, flags=re.IGNORECASE)
    dtfim = tempo2.search(page_content).group()

    #fechando os aquivos.
    load_pdf.close()

    last_row_number = resumo_sheet.max_row
    #print(last_row_number)

    resumo_sheet.cell(column=1, row=last_row_number+1).value = cliente
    resumo_sheet.cell(column=2, row=last_row_number+1).value = cidade
    resumo_sheet.cell(column=3, row=last_row_number+1).value = num_serie
    resumo_sheet.cell(column=4, row=last_row_number+1).value = tipo_equip
    resumo_sheet.cell(column=5, row=last_row_number+1).value = dtinicio
    resumo_sheet.cell(column=6, row=last_row_number+1).value = dtfim

    resumo_excel.save('extracao.xlsx')



resumo = pd.read_excel('extracao.xlsx')
resumo[['Cliente drop','Cliente']] = resumo['cliente'].str.split(':', expand=True)
resumo[['Pais','Estado','Cidade']] = resumo['cidade'].str.split('/', expand=True)
resumo[['num_serie2','N° de serie']] = resumo['num_serie'].str.split('Série ', expand=True)
resumo[['Modelo_drop','Modelo']] = resumo['tipo_equip'].str.split(':', expand=True)
resumo[['Data Terminio','dtterminio']] = resumo['dtfim'].str.split('Término:', expand=True)
resumo[['Inicio','Data atendimento']] = resumo['dtinicio'].str.split('Início:', expand=True)

resumo_clear = resumo.drop(['cliente','cidade','num_serie','tipo_equip','dtinicio','dtfim','Cliente drop','Pais','Estado','num_serie2','Modelo_drop','Data Terminio','Inicio'], axis=1)


resumo_clear['Data atendimento'] = pd.to_datetime(resumo_clear['Data atendimento'])
resumo_clear['dtterminio'] = pd.to_datetime(resumo_clear['dtterminio'])

resumo_clear['data'] = resumo_clear['Data atendimento'].dt.strftime('%D')
resumo_clear['hora inicial'] = resumo_clear['Data atendimento'].dt.strftime('%H:%M')
resumo_clear['hora final'] = resumo_clear['dtterminio'].dt.strftime('%H:%M')

resumo_final = resumo_clear.drop(['dtterminio','Data atendimento'], axis=1)

resumo_final.to_excel('resultado.xlsx', index=False)


source = r'C:\Users\esilveira\Constat\Central de Serviços - Relatórios de Fechamento\pdfs'
destination = r'C:\Users\esilveira\Constat\Central de Serviços - Relatórios de Fechamento\pdf_antigos'
files = os.listdir(source)

for file in files:
    new_path = shutil.move(f"{source}/{file}", destination)
    time.sleep(1)
    print(new_path)
