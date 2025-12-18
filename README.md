# baseml

<img width="862" height="449" alt="image" src="https://github.com/user-attachments/assets/1dd05ba7-e969-4a5f-b475-9c66426ff30c" />

### Task

- [x] criar venv
- [x] criar setup.py
- [x] instalar dependências
- [x] criar data loader
  - [x] criar e testar load_data.py (carrega os dados)
    - [x] criar classe
    - [x] método que builda path
    - [x] método que verifica se leu o csv
    - [x] criar método que carrega os dados (data_load)
    - [x] testar para ver se ele está lendo um csv, de fato.
  - [x] escolher dataset (simples)
  - [x] criar módulo test_train_model.py
  - [x] criar módulo train_model.py
  - [x] criar func processar dados para treino
    - [x] carregar os dados do data_loader.py
    - [x] splitar os dados
      - [x] separar em X e em Y
  - [x] criar config/
    - [ ] criar models que serão treinados no yml file
    - [ ] definir lista de modelos
      - [ ] logit
      - [ ] randomforest
      - [ ] knn reg
      - [ ] svm
      - [ ] dummy class
  - [ ] ajustar target colum para ser 0 e 1 ao invés de yes-no
