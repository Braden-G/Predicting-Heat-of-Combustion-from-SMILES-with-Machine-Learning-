:::graph TD
    B[Conv1D: 32 filters, kernel=3, ReLU]
    C[Flatten]
    D[Dense: 128 units, ReLU]
    E[Dropout: rate 0.3]
    F[Dense: 128 units, ReLU]
    G[Dense: 1 unit, Linear]
    
    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    :::
