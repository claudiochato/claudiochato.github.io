# claudiochato.github.io

Código da página de links do Cláudio, o Chato no Instagram, publicada em https://claudiochato.github.io/.

## A nossa Skill para o Claude

O nosso processo assenta quase por completo numa Skill para o Claude. É ela que conduz a verificação, afirmação a afirmação. Fora da skill, só pedimos ao Claude que gere as imagens dos posts do Instagram e que ajude a escrever a legenda.

Qualquer pessoa pode instalar a mesma skill no seu Claude e usá-la em privado. Quando for preciso recolher fontes, é só ir orientando o Claude no browser da aplicação.

- [Descarregar a skill](https://claudiochato.github.io/skill/social-media-veracity.skill), o ficheiro para instalar no Claude
- [Ler a skill em texto](static/skill/SKILL.md)

Mantemos a skill no Git para que qualquer pessoa possa analisá-la e propor alterações.

## Contribuir melhorias para a skill

A versão de referência da skill é o ficheiro de texto [`static/skill/SKILL.md`](static/skill/SKILL.md). Para propor uma melhoria:

1. Faz um fork deste repositório e altera `static/skill/SKILL.md`.
2. Abre um pull request para `main`, a explicar o que muda e porquê.

Não alteres o ficheiro `social-media-veracity.skill`. É um ficheiro binário, que não dá para rever num pull request, e nós geramo-lo de novo a partir do `SKILL.md` sempre que aceitarmos uma alteração.

Ao abrires um pull request, aceitas que a tua contribuição fique sob a licença da skill, a CC BY-SA 4.0.

## Licença

O código do site está sob a licença MIT (ver `LICENSE`).

A skill, ou seja, os ficheiros `SKILL.md` e `social-media-veracity.skill`, está sob a licença [CC BY-SA 4.0](static/skill/LICENSE.txt). Podes usá-la, alterá-la e republicá-la, desde que atribuas a autoria a «Cláudio, o Chato» e que qualquer versão alterada que publiques fique sob a mesma licença. Usá-la em privado não te obriga a nada.

Nenhuma destas licenças abrange o nome «Cláudio, o Chato», a mascote, as miniaturas nem as restantes imagens da marca e dos posts, que têm todos os direitos reservados.

## Informação para desenvolvimento

O site é feito com Hugo e publicado no GitHub Pages.

- **Editar os links:** `data/links.yaml`
- **Miniaturas:** em `data/links.yaml`, `url` é o destino da ligação e `instagram` é o teu post, de onde vem a miniatura. Preenche `instagram` e corre `python3 scripts/miniatura.py`. O script guarda as miniaturas em falta em `assets/miniaturas/`, por isso faz commit também desses ficheiros. Se o Instagram recusar o download, guarda a imagem à mão e corre `python3 scripts/miniatura.py URL --ficheiro imagem.jpg`.
- **Skill:** os ficheiros estão em `static/skill/`. A página `/skill/` do site é gerada a partir do `SKILL.md`, por isso não precisa de ser editada à parte. Depois de aceitar uma alteração ao `SKILL.md`, gera de novo `social-media-veracity.skill` a partir dele, para as duas versões não ficarem diferentes.
- **Mascote:** coloca `mascote.png` em `static/img/mascote.png`. Até lá, o avatar mostra um «C».
- **Pré-visualizar:** `hugo server`
- **Publicar:** faz push para `main`.
