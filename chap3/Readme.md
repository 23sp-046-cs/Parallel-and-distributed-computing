output 1 

![Chapter 3 Illustration](https://raw.githubusercontent.com/23sp-046-cs/Parallel-and-distributed-computing/7b8021ccc110e712a8984995fdf5602246746e68/chap3/1.jpg)


output 2

![Chapter 3 Image 2](https://raw.githubusercontent.com/23sp-046-cs/Parallel-and-distributed-computing/7b8021ccc110e712a8984995fdf5602246746e68/chap3/2.jpg)

output 3

![Chapter 3 Image 3](https://raw.githubusercontent.com/23sp-046-cs/Parallel-and-distributed-computing/7b8021ccc110e712a8984995fdf5602246746e68/chap3/3.jpg)


Conclusion 1 (Infinite Process and Termination):

Is program me ek process banaaya jata hai jo infinite loop chalata rehta hai. Kuch waqt baad main program us process ko terminate() aur join() karke clean tariqe se band kar deta hai. Ye code yeh demonstrate karta hai ke hum Python me long-running child processes ko control aur safely stop kar sakte hain.

Conclusion 2 (Shared Data with Manager Namespace):

Is code me multiprocessing.Manager() ka use karke ek shared variable banaya gaya hai jise multiple processes modify kar sakte hain. Worker process shared number ko barhata hai, aur change main program me reflect hota hai. Ye code yeh dikhata hai ke processes shared memory ke zariye safely data communicate aur update kar sakte hain.

Conclusion 3 (Basic Child Process Execution):

Ye program ek simple child process create karta hai jo apna PID print karta hai, aur parent process uske complete hone ka wait (join()) karta hai. Ye code demonstrate karta hai ke Python me process creation aur synchronization bohot asaan hai.


