int factorial(int n){
    if (n == 1){
        return 1;
    }
}

return n * factorial(n - 1);

// 꼬리 재귀 최적화 구현
int factorialTail(int n, int acc){
    if(n == 1){
        return acc;
    }
    return factorialTail(n-1, n * acc);
}

