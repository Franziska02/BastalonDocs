# Caso d'uso progressione
```mermaid
classDiagram
Inizia_Livello -->Muori
Muori --> Torna_hub
Torna_hub --> Potenziamento
Inizia_Livello --> Batti_livello
Batti_livello --> Progredisci
Progredisci --> Nuovo_Livello
Nuovo_Livello --> Batti_livello
Nuovo_Livello --> Muori
Nuovo_Livello --> Torna_hub
Potenziamento --> Inizia_Livello
```