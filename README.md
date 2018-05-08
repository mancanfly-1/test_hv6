# test_hv6
  create a simple Counter case according to hv6

## how to run

I test the test_hv6 at the same environment with hv6

To compile:
    must run compile first, it includes compile .c --> .ll , then compose any .ll --> hv6.ll, at end, translating
    hv6.ll --> hv6.py using irpy which provided by hv6.
    
    `make`
     
To run verfiy:(must complie first)
    running testcase in main.py. it verifies 3 test cases which include increase, decrease and iszero. it verifies the equals  
    between statemachine and lowwer code(behavior as contex object in python), and add a invariant property(counter never < 0 )
    
    `make verify`
      
 to run app
 
    `make app`
      
## file structure
    
- test_hv6
  - counter.c       // source code
  - invariant.py    // as you see
  - main.py         // test case
  - specs.py        // specification of three funcation
  - irpy            // copy from hv6
  
- x86_64            // build dir
      
  
- script            // clear undefined behavior in llvm ir.

- datatype          // define our state machine.

- libirpy           // as the name defined.
