import a2
import io
import inspect

def ensure(passes, test_case, tested=[]):
    '''(bool, str, list of strs) -> bool
    
    Print out whether test_case passes or fails; append additional information
    based on the name of the calling function.

    Return the initial value of passes.
    
    The tested list should not be specified.
    '''

    # Find the name of the test function calling ensure
    stack = inspect.stack()

    found = False
    idx = 1
    
    while idx < len(stack) and found == False:
        (_, _, _, function_name, _, _) = stack[idx]
        
        if function_name.startswith('test_'):
            # Print out a message stating which test is being run if
            # this is the first call to ensure within the test function.
            if not function_name in tested:
                print("Running tests in function " + function_name)
            tested.append(function_name)

        found = True
                
    # Print out a message about whether the test passes or fails. 
    if not passes:
        print(' * ' + test_case + ' FAILED.')
    else:
        print(' * ' + test_case + ' passed.')
        
    return passes


def test_encipher_type():
    ensure(a2.encipher.__code__.co_argcount == 3, 'argument number test')
    result = a2.encipher('hello', 5, {'e': '9'})
    ensure(type(result) == str, 'return type')


def test_decipher_type():
    ensure(a2.decipher.__code__.co_argcount == 3, 'argument number test')
    result = a2.decipher('hello', 5, {'e': '9'})
    ensure(type(result) == str, 'return type')


def test_reverse_groups_type():
    ensure(a2.reverse_groups.__code__.co_argcount == 1, 'argument number test')
    result = a2.reverse_groups([['A', 'B', 'C'], ['D', 'E', 'F']])
    ensure(type(result) == str, 'return type')


def test_get_key_type():
    ensure(a2.reverse_groups.__code__.co_argcount == 1, 'argument number test')
    result = a2.get_key(io.StringIO('1\nAB\n'))
    if ensure(type(result) == tuple, 'return type'):
        ensure(len(result) == 2, 'return length')
        ensure(type(result[0]) == int, 'returned tuple contents\' type')
        ensure(type(result[1]) == dict, 'returned tuple contents\' type')


def test_process_type():
    ensure(a2.process.__code__.co_argcount == 3, 'argument number test')
    result = a2.process('test.txt', 3, {'e': '9'})
    ensure(result == None, 'argument number test')


def run_tests():
    '''() -> None
    
    Run all the tests in this file.
    '''
    
    globals_list = list(globals().items())
    globals_list.sort()
    for obj_name, obj in globals_list:
        if obj_name.startswith('test_'):
            try:
                obj()
                print()
            except Exception as e:
                print('#' * 80)
                print("   Problem detected: ")
                print('   ' + str(e))
                print('#' * 80)

if __name__ == '__main__':
    # Replace the 'open' function in a2 with a dummy version
    a2.open = lambda *_, **_2: io.StringIO('1\nAB\n')
    run_tests()
