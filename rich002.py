from rich import print as rprint
from rich.panel import Panel

nome  = Panel(
    'Cecília',
    title='[yellow]Nome[/yellow]',
    style='bold blue',
    border_style= 'purple',
    width= 20)
idade = Panel(
    '21 anos',
    title='[yellow]Idade[/yellow]',
    style='bold blue',
    border_style= 'purple',
    width= 20)

rprint(nome , idade)