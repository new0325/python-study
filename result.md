|연산자|int|float|str|list|tuple|set|dict||
|---|------------|----------|-----------|------------|-------------|-------------|------------|-------------|
|+|가능|가능|가능|가능|가능|불가능|불가능|
|-|가능|가능|불가능|불가능|불가능|가능|불가능|
|*|가능|가능|불가능|불가능|불가능|불가능|불가능|
|/|가능|가능|불가능|불가능|불가능|불가능|불가능|

|연산자|int+float|int+str|int+list|float+str|float+list|str+list|str+tuple|list+tuple|
|---|---|---|---|---|---|---|---|---|
|+|가능|불가능|불가능|불가능|불가능|불가능|불가능|불가능|
|결과|float|x|x|x|x|x|x|x|

|연산자|int-float|int-str|int-list|float-str|float-list|str-list|str-tuple|list-tuple|
|---|---|---|---|---|---|---|---|---|
|-|가능|불가능|불가능|불가능|불가능|불가능|불가능|불가능|
|결과|float|x|x|x|x|x|x|x|

|연산자|float-int|str-int|list-int|str-float|list-float|list-str|tuple-str|tuple-list|
|---|---|---|---|---|---|---|---|---|
|-|가능|불가능|불가능|불가능|불가능|불가능|불가능|불가능|
|결과|float|x|x|x|x|x|x|x|

|연산자|int*float|int*str|int*list|int*tuple|float*str|float*list|str*list|str*dict|
|---|---|---|---|---|---|---|---|---|
|*|가능|가능|가능|가능|불가능|불가능|불가능|불가능|
|결과|float|str|list|tuple|x|x|x|x|

|연산자|float*int|str*int|list*int|str*float|list*float|list*str|tuple*str|tuple*list|
|---|---|---|---|---|---|---|---|---|
|*|가능|가능|가능|불가능|불가능|불가능|불가능|불가능|
|결과|float|str|list|x|x|x|x|x|


•Q. int와 float 타입을 곱하면 결과가 어떻게 되나요?
<Br>A. 'float'

•Q. int 타입을 str 타입과 곱하면, 문자열이 어떻게 되나요?
<Br>A. 'str'

•Q. int 타입을 list 타입과 곱하면, 리스트가 어떻게 되나요?
<Br>A. 'list가 int의 배수만큼 중복 노출 됨'

•Q. int 타입을 tuple 타입과 곱하면, 튜플이 어떻게 되나요?
<Br>A. 'tuple이 int의 배수만큼 중복 노출 됨'