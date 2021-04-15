def set_intro():
    basket_list = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    basket_tuple = ('apple', 'orange', 'apple', 'pear', 'orange', 'banana')
    basket_set = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

    print(basket_list)
    print(basket_tuple)
    print(basket_set)

    print('orange' in basket_set)
    print('Orange' in basket_set)

    print(sorted(basket_set))

def set_methods():
    european_flowers = {"sunflowers", "roses", "lavender", "tulips", "goldcrest"}
    american_flowers = {"roses", "tulips", "lilies", "daisies"}

    american_flowers.add("orchids")
    print(american_flowers)

    american_flowers.add(20)
    print(american_flowers)

    print(american_flowers.difference(european_flowers))    
    print(european_flowers.difference(american_flowers))    

    print(american_flowers.intersection(european_flowers))
    print(european_flowers.intersection(american_flowers))


    set1 = {10, 20, 30}
    set2 = {40, 20, 50, 30, 60, 10}
    set3 = {80, 90, 50, 40}
    print(f'set1 is subset set2: {set1.issubset(set2)}')
    print(f'set2 is subset set1: {set2.issubset(set1)}')
    

    print(f'set1 is superset set2: {set1.issuperset(set2)}')
    print(f'set2 is superset set1: {set2.issuperset(set1)}')
    
    print(f'set1 is disjoint set3: {set1.isdisjoint(set3)}')
    print(f'set3 is disjoint set1: {set3.isdisjoint(set1)}')
    print(f'set2 is disjoint set3: {set2.isdisjoint(set3)}')

    american_flowers.discard(20)
    print(american_flowers)

    american_flowers.discard(20)
    print(american_flowers)
    
    american_flowers.remove('roses')
    print(american_flowers)
    
    # Raise Error
    # american_flowers.remove('roses')
    # print(american_flowers)
    
    print(american_flowers.pop())
    print(american_flowers)

    print(american_flowers.pop())
    print(american_flowers)

    print(american_flowers.pop())
    print(american_flowers)

    print(american_flowers.pop())
    print(american_flowers)

    # Raise Error
    # print(american_flowers.pop())
    # print(american_flowers)

    set_union = set2.union(set3)
    print(set_union)

    set_union = set3.union(set2)
    print(set_union)
    print(set2)
    print(set3)

    set1.update(set3)
    print(f'set2 = {set2}')
    print(f'set3 = {set3}')

    print(f'symmetric_difference = {set2.symmetric_difference(set3)}')
    print(f'symmetric_difference = {set3.symmetric_difference(set2)}')

    print(f'difference = {set2.difference(set3)}')
    print(f'difference = {set3.difference(set2)}')