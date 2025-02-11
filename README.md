# RESUMOS AUTOMATIZADOS

Este repositório permite gerar resumos automatizados de notícias.

## Instruções

1. Crie um arquivo `.env` e insira sua chave da OpenAI com o nome `OPENAI_API_KEY`.

2. Coloque os arquivos de notícias extraídos no formato `.txt` na pasta `input`.

3. Execute o script `summarizer.py` com o comando:
   ```bash
   python summarizer.py
   ```

4. Os resumos das notícias estarão disponíveis na pasta `output` no formato Word.
