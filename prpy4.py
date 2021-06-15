из  склеарна . импорт наборов данных  *
импортировать  панд  как  pd
import  matplotlib . pyplot  как  plt
импортировать  numpy  как  np
из  склеарна . соседи  импортируют  KNeighborsClassifier  # Импорт библиотек

def  Image_display ( i ):
    plt . imshow ( цифра [ 'изображения' ] [ i ], cmap  =  'Greys_r' )
    plt . показать ()

# Загрузка данных
цифра  =  load_digits ()
digit_d  =  pd . DataFrame ( digit [ 'data' ] [ 0 : 1600 ]) # используем 1600 изображений для обучающего образца, оставшиеся 197 сохранены для тестирования

# Набор данного обучения / тест
train_x  =  цифра [ 'данные' ] [: 1600 ]
train_y  =  цифра [ 'цель' ] [: 1600 ]

# Набор данны тест KNN
KNN  =  KNeighborsClassifier ( 20 )
КНН . подходят ( train_x , train_y )

# Классификатор ближ. соседей
KNeighborsClassifier ( алгоритм  =  'auto' , leaf_size  =  30 , metric  =  'minkowski' , metric_params  =  None , n_jobs  =  1 , n_neighbors  =  20 , p  =  2 , weights  =  'uniform' )

# Образцовый тест> 1600
test  =  np . массив ( цифра [ 'данные' ] [ 1725 ])
test1  =  тест . изменить форму ( 1 , - 1 )
Отображение_изображения ( 1725 )

# Прогноз
print ( KNN . предсказать ( test1 ))

печать ( цифра [ 'target_names' ])
