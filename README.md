## CS224n

-  **a4 result**
 
 ***vanilla dev accuracy***

![alt text](<Screenshot 2025-06-06 234507.png>)

***rope accuracy***

![alt text](image.png)

---
update #1

after fix some bug of RoPE， the accuracy finnally achieve above 30%,

I think there has a error in annotation
```python

#    cos(t theta_i) and sin(t theta_i)
#        where t is the position and
#              theta_i = 1/10000^(-2(i-1)/dim) for i in [1, dim/2]
```
but the truly theta_i should be 10000^(-2(i-1)/dim) without that 1/....

so, anyway, after I change it to the correct formula, the accuracy reached 30%

![alt text](<Screenshot 2025-06-07 152910.png>)