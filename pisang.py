import random
 
 
def start():
    while True:
        bentuk_pisang = "("
        pisang_kosong = [bentuk_pisang] * 4

        buahnya = random.randint(1,4)
        pisang = pisang_kosong.copy ()
        pisang[buahnya-1] = "o"

        pisang_kosong = '  '.join (pisang_kosong)
        pisang = '  ' .join (pisang)

    

        print(f'saya ada tebakan untuk anda dimana dogan berada \n\n{pisang_kosong}\n')

        pilihan_user = int(input ("di nomor berapa dogan berada? [1/2/3/4]") )

        print(f"pilihan kamu adalah   {pilihan_user}")
        confirm_user = input(f"apakah kamu yakin jawabannya {pilihan_user}? [y/n] : ")
                
        if confirm_user == "n" :
            print ("program dihentikan ")
            exit() 

        elif  confirm_user == "y" :
            if pilihan_user == buahnya :
             print (f"\n dogannya ada di : \n {pisang} \n selamat kamu benar jawabannya adalah {buahnya}")
            
            else :
             print (f" \n dogannya ada di : \n{pisang} \n maaf kamu kalah jawbannya adalah {buahnya}")   
                
        else:
            print ("silahkan ulangi program")
            exit()
        play_again = input("\n\napakah kamu imgin bermain lagi ? \n ketik [y/n]")
        if play_again == "n" :
            break
        
    print ("program selesai")    

if __name__== '__main__':
    start()