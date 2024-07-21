## Bloom-Filter with Python3

### 1. Bloom-filter?
    - 어떤 원소가 기존 집합에 속하는지 여부를 검사하기 위해 사용되는 확률적 자료구조이다.

    - Bloom-filter는 '확률적 자료구조'이므로, False-Positive (양성이라 판단하였지만, 거짓인 경우) 문제가 발생할 수 있다.

    - 그러나, 반대로 False-Negative (음성이라 판단하였지만, 거짓인 경우) 문제는 발생하지 않는다.
    Bloom-filter 는 일부 Hash Comfilct (해시 충돌)을 허용해야 사용이 가능하다.

### 2. Bloom-filter의 구성요소

    - m bit 크기의 bit array

    - k 개의 Hash functions

### 3. Hash functions

    - Bloom-filter의 Hash functions는 Independent 하며 Uniform distribution 해야 한다.

    - 또한 속도가 빨라야 한다.

    - 암호학적 Hash functions (SHA256 등)은 안정적이고 좋은 성능을 가졌지만, 계산 비용이 너무 높아서 무리다.

    - 따라서 murmur 해시함수를 이용하여 구현하였다.

### 4. murmur Hash function

    - 해시 값 만을 만들어내는 Hash function의 일종이다.

    - 암호화 해시 함수에 비해 안정성은 떨어질 수 있지만, 속도가 빠르다는 장점이 있다. (계산 비용 절감)

    - Bloom-filter는 어느정도의 해시 충돌을 허용해야 하므로, 이를 채택하였다.