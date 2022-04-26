k=0
x=0
for s1 in 'ТИМОФЕЙ':
    for s2 in 'ТИМОФЕЙ':
        for s3 in 'ТИМОФЕЙ':
            for s4 in 'ТИМОФЕЙ':
                for s5 in 'ТИМОФЕЙ':
                    s=s1+s2+s3+s4+s5
                    x+=1
                    if s.count('Й')<=1 and s.count('Т')>=1:
                        k+=1
print(k)
print(x)


                        
                    
