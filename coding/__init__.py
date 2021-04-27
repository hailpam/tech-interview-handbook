
__all__ = ['array', 'backtracking', 'dp', 'ds-and-algo', 'graph', 'recursion']

def test(input, expected, output):
    """
    Utility to test the outcome of a function call.
    """
    if expected != output:
        print('[-] i=%s <> e=%s <> o=%s' % (input, expected, output))
        import sys
        sys.exit(1)
    print('[+] i=%s <> e=%s <> o=%s' % (input, expected, output)) 
