импортировать  numpy  как  np
import  matplotlib . pyplot  как  plt
из  склеарна . соседи  import  NearestNeighbors  # Ввод библиотек

# Вводные данные
А  =  np . массив ([[ 3.1 , 2.3 ], [ 2.3 , 4.2 ], [ 3.9 , 3.5 ], [ 3.7 , 6.4 ], [ 4.8 , 1.9 ],
             [ 8.3 , 3.1 ], [ 5.2 , 7.5 ], [ 4.8 , 4.7 ], [ 3.5 , 5.1 ], [ 4.4 , 2.9 ]])

# Соседи
k  =  3

# Тест
test_data  = [ 3.3 , 2.9 ]

# Визуализиция ввода даных
plt . рисунок ()
plt . название ( "входные данные" )
plt . scatter ( A [:, 0 ], A [:, 1 ], marker  =  "o" , s  =  100 , c  =  "черный" )

# Создание ближ. соседей с обучением
knn_model  =  Ближайшие соседи ( n_neighbors  =  k , algorithm  =  "auto" ). подходит ( A )
расстояния , индексы  =  knn_model . колени ([ test_data ])

# Коорды ближ. Соседей
print ( " \ n k Соседи:" )
для  ранга , индекс  в  Перечислим ( индексы [ 0 ] [: K ], начать  =  1 ):
    print ( str ( rank ) +  "is" , A [ index ])

# визуализируция соседей
plt . title ( "Ближайшие соседи" )
plt . scatter ( A [:, 0 ], A [:, 1 ], marker = "o" , s = 100 , c = "k" )
plt . scatter ( A [ индексы ] [ 0 ] [:] [:, 0 ], A [ индексы ] [ 0 ] [:] [:, 1 ], marker  =  "o" , s = 250 , facecolors  =  'none' , edgecolors = 'фиолетовый' )
plt . разброс ( test_data [ 0 ], test_data [ 1 ], marker  =  "x" , c  =  "purple" , s  =  100 )

plt . показать ()
