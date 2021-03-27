# 04 - Manual do Usuário

## Interface

### Janela principal

Janela exibida assim que o software é executado.

![04%20-%20Manual%20do%20Usua%CC%81rio/manual_1.png](04%20-%20Manual%20do%20Usua%CC%81rio/manual_1.png)

1 - Lista com os "apelidos" das pastas compartilhadas que receberão a sincronização. 

2 - Botão para adicionar uma nova pasta comaprtilhada ao software

3 - Botão que vai puxar pasta por pasta da lista, fazendo a sincronização

4 - Botão para remover um item da lista. É preciso selecionar o ítem e clicar no botão.

### Janela Add new shared folder

Janela exibida após o usuário clicar no botão **Add Folder** da janela principal.

![04%20-%20Manual%20do%20Usua%CC%81rio/manual_2.png](04%20-%20Manual%20do%20Usua%CC%81rio/manual_2.png)

Informações a serem preenchidas

- **Room:** um apelido para a máquina. É o nome que aparecerá na lista, na janela principal. A identificação **Room** (sala), é para melhor identificação de onde a máquina está.
- **Machine Name**: nome da máquina na rede. Essa informação deve ser coletada diretamente na máquina que vai ser adicionada, na opção **Computer Information**
- **Shared Folder**: Nome do compartilhamento dado à pasta que irá receber as informações da sincronização. Na maioria das vezes, essa informação vai ser composta por //machine_name/nome_da_pasta_compartilhada
- **Save:** botão que vai cadastrar as informações digitadas no formulario, no banco de dados.

## Sincronização

Após cadastrar os compartilhamentos que receberão a sincronização, clique no botão **SYNC**.

A aplicação percorrerá cada item da lista, fazendo a sincronização das pastas.

Importante: se um arquivo for apagado na pasta source, após o sync será apagada nas pastas destinos tambem. 

Se a sincronização for finalizada com sucesso, será exibida uma mensagem para cada item da lista:

![04%20-%20Manual%20do%20Usua%CC%81rio/manual_3.png](04%20-%20Manual%20do%20Usua%CC%81rio/manual_3.png)