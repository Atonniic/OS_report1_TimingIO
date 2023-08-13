import timeit
import os

#I/O-bound operation
def WriteFile():
    #เขียน binary file ขนาดใหญ่( 1 GB )
    with open( 'data.bin', 'wb' ) as file:
        file.write( b'\x00' * ( 1024 ** 3 ) )

#CPU-bound operation        
def Factorial( number ):
    if number == 0:
        return 1
    else:
        return number * Factorial( number - 1 )
    
def TimeTaken( func ):
    start = timeit.default_timer()
    func()
    end = timeit.default_timer()
    return end - start

#Call function และวัดเวลาที่ใช้
print(f"Time taken ( I/O-bound ): { TimeTaken( WriteFile ) } seconds")
print(f"Time taken ( CPU-bound ): { TimeTaken( lambda: Factorial( 994 ) ) } seconds")

#ลบ data.bin ออกจากไดเร็คทอรี่
os.remove('data.bin')
