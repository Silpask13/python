def towerhanoi(n,source,destination,intermediate):
    if n==1:
        print(f"move disk 1 from{source}to {destination}")
        return
    towerhanoi(n-1,source,intermediate,destination) 
    print(f"move disk{n}from {source} to {destination}")
    towerhanoi(n-1,intermediate,destination,source)
n=2
towerhanoi(n,'a','b','c')    
