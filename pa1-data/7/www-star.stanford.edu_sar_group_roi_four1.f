c four1 this is the four1 routine from numerical recipes subroutine four1 data nn isign real 8 wr wi wpr wpi wtemp theta dimension data n 2 nn j 1 do 11 i 1 n 2 if j gt i then tempr data j tempi data j 1 data j data i data j 1 data i 1 data i tempr data i 1 tempi endif m n 2 1 if m ge 2 and j gt m then j jm m m 2 go to 1 endif j j m 11 continue mmax 2 2 if n gt mmax then istep 2 mmax theta 6.28318530717959 d0 isign mmax wpr 2 d0 dsin 0.5 d0 theta 2 wpi dsin theta wr 1 d0 wi 0 d0 do 13 m 1 mmax 2 do 12 i m n istep j i mmax tempr sngl wr data j sngl wi data j 1 tempi sngl wr data j 1 sngl wi data j data j data i tempr data j 1 data i 1 tempi data i data i tempr data i 1 data i 1 tempi 12 continue wtemp wr wr wr wpr wi wpi wr wi wi wpr wtemp wpi wi 13 continue mmax istep go to 2 endif return end