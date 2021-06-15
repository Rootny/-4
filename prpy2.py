импортировать  numpy  как  np
из  склеарна . кластерный  импорт  MeanShift
import  matplotlib . pyplot  как  plt
от  Matplotlib  импорта  стиля
стиль . использовать ( "ggplot" )
из  склеарна . наборы данных  импортируют  make_blobs

# Настройка визуала
центры  = [[ 2 , 2 ], [ 4 , 5 ], [ 3 , 10 ]]
X , _  =  make_blobs ( n_samples  =  500 , центры  =  центры , cluster_std  =  1 )
plt . разброс ( X [:, 0 ], X [:, 1 ])

# Обучение с входными данными
мс  =  Среднее смещение ()
мс . подходит ( X )
метки  =  мс . метки_
cluster_centers  =  мс . cluster_centers_

# Кластеры и ожидаймые координаты
печать ( cluster_centers )
n_clusters_  =  len ( np . уникальный ( метки ))
print ( "Предполагаемые кластеры:" , n_clusters_ )

# Настройка визуала
цвета  =  10 * [ 'r.' , 'g.' , 'b.' , 'c.' , 'k.' , 'y.' , м. ]
для  i  в  диапазоне ( len ( X )):
    plt . сюжет ( X [ i ] [ 0 ], X [ i ] [ 1 ], цвета [ метки [ i ]], размер маркера  =  10 )

# мидл
plt . scatter ( cluster_centers [:, 0 ], cluster_centers [:, 1 ], marker  =  "x" , color  =  'k' , s  =  100 , linewidths  =  1 , zorder  =  10 )
plt . показать ()
