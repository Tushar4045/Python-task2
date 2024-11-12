#from folderName.fileName import funvtionNamee
from mathOp.multiOp import multivalue
from mathOp.divOp import divvalue

if __name__== '__main__':
    val1 = int(input('Enter the first value: '))
    val2 = int(input('enter the  second  value: '))
    op = input('which math OP you want to perform? ')

    if op.lower() == 'multi':
        m  = multivalue(val1,val2)
        print(f'multiplication: {m}')
    elif op.lower() == 'div':
        d = divvalue(val1,val2)
        print(f'division: {d}')
    else:
        print('please enter the op multi or div')
