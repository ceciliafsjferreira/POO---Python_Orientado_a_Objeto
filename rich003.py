from rich import print as rprint
from rich.table import Table

tabela = Table(title='Tabela de Alunos', style='bold blue', border_style='purple')

tabela.add_column('Nome', style='yellow', justify='center')
tabela.add_column('Idade', style='yellow', justify='center')
tabela.add_column('Curso', style='yellow', justify='center')
tabela.add_row('Cecília', '21 anos', 'Python')

rprint(tabela)