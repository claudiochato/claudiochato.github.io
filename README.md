# claudiochato.github.io

Código da página de links do Cláudio, o Chato no Instagram, publicada em https://claudiochato.github.io/.

## Licença

O código está sob a licença MIT (ver `LICENSE`). Essa licença não abrange o nome «Cláudio, o Chato», a mascote, as miniaturas nem as restantes imagens da marca e dos posts, que têm todos os direitos reservados.

## Informação para desenvolvimento

O site é feito com Hugo e publicado no GitHub Pages.

- **Editar os links:** `data/links.yaml`
- **Miniaturas:** em `data/links.yaml`, `url` é o destino da ligação e `instagram` é o teu post, de onde vem a miniatura. Preenche `instagram` e corre `python3 scripts/miniatura.py`. O script guarda as miniaturas em falta em `assets/miniaturas/`, por isso faz commit também desses ficheiros. Se o Instagram recusar o download, guarda a imagem à mão e corre `python3 scripts/miniatura.py URL --ficheiro imagem.jpg`.
- **Mascote:** coloca `mascote.png` em `static/img/mascote.png`. Até lá, o avatar mostra um «C».
- **Pré-visualizar:** `hugo server`
- **Publicar:** faz push para `main`.
