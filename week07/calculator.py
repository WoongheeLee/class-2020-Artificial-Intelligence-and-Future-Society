def addition(*args):
    """
    정수를 입력받아서 모두 더한 값을 반환
    """
    
    summation = 0
    
    for n in args:
        summation += n
        
    return summation


def multiplication(*args):
    """
    정수를 입력받아서 모두 곱한 값을 반환
    """         
    mul = 1
    
    for n in args:
        mul *= n
                   
    return mul
                   
                   
def vector_product(A, B):
    """
    두 벡터를 입력받아, 벡터 곱을 반환
    """
    
    assert len(A) == len(B) # 조건이 위배되면 오류 발생시켜서 실수 방지
    
    result =  0
    
    for i in range(len(A)):
        result += A[i] * B[i]
        
    return result