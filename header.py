# -*- coding: UTF-8 -*-

def header_author():
    print '''
    ____  ___  ____  _   _ 
    (  _ \(__ )(_  _)( )_( )
    )(_) )(_ \  )(   ) _ ( 
    (____/(___/ (__) (_) (_)
    ____  _  _  ____  ____ 
    (  _ \( \/ )(_  _)( ___)
    ) _ < \  /   )(   )__) 
    (____/ (__)  (__) (____)
    '''

def header_script_name():
    print '''
    ___________              _________                    
    \_   _____/_ _____  ___ /   _____/ ____   ____ ___.__.
    |    __)|  |  \  \/  / \_____  \ /  _ \_/ ___<   |  |
    |     \ |  |  />    <  /        (  <_> )  \___\___  |
    \___  / |____//__/\_ \/_______  /\____/ \___  > ____|
        \/              \/        \/            \/\/     
    
    '''

def put():
    header_author()
    header_script_name()

if __name__ == '__main__':
    put()