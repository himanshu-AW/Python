def TowerOfHanoi(n,from_A,to_C,aux_B):
    if n<=1:
        print('Move disk 1 from rod ',from_A,' to rod ',to_C)
        return
    TowerOfHanoi(n-1,from_A,aux_B,to_C)
    print('Move disk ',n,'from rod ',from_A,' to rod ',to_C)
    TowerOfHanoi(n-1,aux_B,to_C,from_A)
    

n=3
TowerOfHanoi(n,'A','C','B')