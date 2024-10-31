def a():
    animal='tiger'
    print(f'before b : {animal}')
    def b():
        nonlocal animal
        animal = 'cow'
        print(animal)
    
    print(f'after b defining : {animal}')

    b()
    print(f'after b calling : {animal}')


animal='horse'
a()

print(f'after a calling : {animal}')


