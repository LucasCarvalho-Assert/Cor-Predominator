
# Color Dominance Analyzer 🎨

Este script utiliza a biblioteca OpenCV e outras ferramentas para analisar uma imagem e determinar as cores mais predominantes em uma região central. As cores são consolidadas e exibidas com suas porcentagens de predominância.

## Funcionalidades ✨

- Analisa a região central de uma imagem para determinar as cores predominantes.
- Consolida as cores em categorias principais.
- Retorna as cinco cores mais predominantes e suas porcentagens.

## Requisitos 🛠️

- Python 3.x
- Bibliotecas: `cv2`, `numpy`, `requests`, `PIL`

## Como usar 📋

1. Clone este repositório ou baixe o arquivo `color_dominance_analyzer.py`.
2. Instale as bibliotecas necessárias:
    ```sh
    pip install opencv-python-headless numpy requests pillow
    ```
3. Execute o script:
    ```sh
    python color_dominance_analyzer.py
    ```

## Exemplos de saída 📊

```python
[
    ('Cinza', 2.51),
    ('Preto', 2.28),
    ('Preto', 2.21),
    ...
]
```

## Detalhes técnicos 🔍

O script realiza os seguintes passos:

1. Carrega a imagem a partir de uma URL.
2. Redimensiona a imagem para facilitar a análise.
3. Define uma região central da imagem para análise.
4. Conta a frequência de cada cor na região definida.
5. Consolida as cores em categorias principais e calcula suas porcentagens.
6. Exibe as cinco cores mais predominantes e suas porcentagens.

## Contribuições 🤝

Sinta-se à vontade para contribuir com melhorias para este projeto! Abra uma issue ou envie um pull request.

## Licença 📜

Este projeto está licenciado sob a MIT License.
