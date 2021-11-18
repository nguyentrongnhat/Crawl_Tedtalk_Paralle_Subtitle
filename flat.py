# length doc1 > length doc2
def flat(doc1, doc2):
    length1 = 0
    length2 = 0
    min = 0
    max = 0
    for i in range(len(doc1)):
        length1 = len(doc1[i].split(' '))
        length2 = len(doc2[i].split(' '))
        print(length1)
        print(length2)
        min = length1
        if(length1 > length2):
            min = length2
        error = abs(length1-length2)/min
        print(error)
        if (error > 1):
            print(doc1[i])
            print(doc2[i])
            print('trung error:[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]')
            
            if(length1 < length2 and '.' in doc2[i]):
                print('vao day')
                split_index = doc2[i].index('.')
                split_data = doc2[i][split_index + 1:]
                doc2[i] = doc2[i][:split_index + 1]
                doc2.insert(i + 1, split_data)
            if(length1 > length2 and '.' in doc1[i])::
                split_index = doc1[i].index('.')
                split_data = doc1[i][split_index + 1:]
                doc1[i] = doc1[i][:split_index + 1]
                doc1.insert(i + 1, split_data)
        print('=====================================================================')
    return doc1, doc2