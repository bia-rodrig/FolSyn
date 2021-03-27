# 01 - Informações de Desenvolvimento

Utilizado:

- banco de dados SQLITE
- Interface gráfica Tkinter

Configuração do banco de dados:

- **ID:** Integer, Primary key, Autoincrement - número de identificação
- **Room:** Varchar -Nome da sala onde fica a máquina
- **Machine name:** Varchar - nome do computador (computer information)
- **IP:** Varchar - Número do IP do computador
- **Shared Folder:** Varchar - caminho para a pasta compartilhada que vai receber os arquivos após sincronização

## Compilação

Comando executado:

```python
pyinstaller.exe --onefile --windowed --icon=FolSyn.ico FolSyn_v1.py
```