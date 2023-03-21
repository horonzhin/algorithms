# Ханойские башни с помощью рекурсий

def tower(n, fr, to, spare):
    if n == 1:
        print('move from ' + str(fr) + ' to' + str(to))
    else:
        tower(n - 1, fr, spare, to)
        tower(1, fr, to, spare)
        tower(n - 1, spare, to, fr)
