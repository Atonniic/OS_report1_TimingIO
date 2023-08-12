import timeit
import os

#I/O-bound operation
def WriteFile():
    #เขียน binary file ขนาดใหญ่( 1 GB )
    with open( 'data.bin', 'wb' ) as file:
        file.write( b'\x00' * ( 1024 ** 3 ) )
    file_size = os.path.getsize( 'data.bin' )

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
    print(f"Time taken: {end - start} seconds")

#Call function และวัดเวลาที่ใช้
TimeTaken( WriteFile )
TimeTaken( lambda: Factorial( 994 ) )

#ลบ data.bin ออกจากไดเร็คทอรี่
os.remove('data.bin')
