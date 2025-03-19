def identification(name):
    print('Вы являетесь')

    if name == 'Alex':
        result = 'Автором'
    else:
        result = 'Студентом'
    return result


uid = identification('Alex')
print(uid)


def status(result):
    print(result)


status(uid)
