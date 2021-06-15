import  matplotlib . pyplot  как  plt
импортировать  seaborn  как  sns ;
sns . набор ()
импортировать  numpy  как  np
из  склеарна . кластерный  импорт  KMeans
из  склеарна . наборы данных  импортируют  make_blobs

# Данные
X , y_true  =  make_blobs ( n_samples  =  500 , центры  =  4 , cluster_std  =  0.40 , random_state  =  0 )

# Настройка визуала
plt . разброс ( X [:, 0 ], X [:, 1 ], s  =  50 )

kmeans  =  KMeans ( n_clusters  =  4 )

# Обучение мидл K
kсред . подходит ( X )
y_kmeans  =  kmeans . предсказать ( X )
plt . scatter ( X [:, 0 ], X [:, 1 ], c  =  y_kmeans , s  =  50 , cmap  =  'viridis' ) # визуализация

# Мидл
центры  =  kсред . cluster_centers_
plt . разброс ( центры [:, 0 ], центры [:, 1 ], c  =  'черный' , s  =  200 , альфа  =  0,10 )

plt . показать ()
