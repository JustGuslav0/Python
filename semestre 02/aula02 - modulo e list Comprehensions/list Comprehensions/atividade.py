atv1 = [i*i for i in range(1,11)]
atv2 = [i for i in range(1,21) if i%2==0]
atv3 = [len(i) for i in ['Python', 'List', 'Comprehension', 'Exercícios']]
atv4 = [c * 9/5 + 32 for c in [0,10,20,30,40]]
atv5 = ['Fizz' if i%3==0 else i for i in range(1,21)]
atv6 = [i for i in ['maçã','banana','uva','morango','abacaxi'] if len(i)>5]
atv7 = [[x,y] for x in range(3) for y in range(3)]
print(f'''atv1 - {atv1}
atv2 - {atv2}
atv3 - {atv3}
atv4 - {atv4}
atv5 - {atv5}
atv6 - {atv6}
atv7 - {atv7}''')