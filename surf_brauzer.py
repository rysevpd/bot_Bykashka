import webbrowser
import time
import pyautogui
# начальная задача ссылки
link = 'https://vk.com/im?peers=370614864_c21&sel='
num_link = 541658263 # забиваем первый uuid, при повторном запуске смотрим последний лог в logs.open
a=1  #потом убрать

while True:
    while a != 10:  # потом убрать
        num_link_s = str(num_link)
        surf_link = (link + num_link_s)
        webbrowser.open(surf_link)
        time.sleep(15)
        num_link += 1
        a += 1  # для статистики, потом убрать
        locate = pyautogui.locateCenterOnScreen('open_lx.png')
        print(locate)
        if locate != None:
            print(locate) #для проверки работоспособности
            pyautogui.moveTo(579, 704, 1)
            pyautogui.click()
            pyautogui.typewrite("Ghbdtn/")
            pyautogui.hotkey('enter')
            pyautogui.typewrite("Z ,jn <erfirf? vtyz nfr yfpdfk vjq {jpzby/ Gjxtve jy vtyz nfr yfpdfk& Yt pyf.? "
                                "tckb xtcnyj/ Yfdthyj 'nj rfrfz-nj ienrf? yj njulf e vjtuj {jpzbyf cnhfyysq .vjh/"
                                "Z djn xnj crfpfnm [jntk - vbh pkjq/ Yj ns [jhjibq/ Lf? ghfdlf? z f,cjk.nyj cthmtpyj/ "
                                "E nt,z ,sdfkj nfrjt joeotybt? xnj vbh ghjnbd nt,z& Xnj ybrnj yt [jxtn? xnj,s ns xtuj-nj "
                                "lj,bkcz/ B 'nj e;fcyj? ghfdlf/ B cfvjt vthprjt nj? xnj ns ybxtuj yt vj;tim c 'nbv gjltkfnm/ '[? uhecnm? gtxfkm? njcrf/"
                                "Gj;fkeqcnf? yt rblfq yf vtyz ;fkj,e/ Z ybxtuj gkj[juj yt [jxe? ghfdlf/ B z yt ,ele nt,t "
                                "ybxtuj ckfnm? gbcfnm b dsvjufnm/ Vyt 'nj yt ye;yj/ Nfr xnj gecnm 'nj jcnfytncz yfibv vfktymrbv ctrhtnjv/"
                                "F[ lf? z xtn jn ntvs eitk/ Rjulf nt,t rf;tncz? xnj dtcm vbh ghjnbd nt,z b [jxtncz pfdsnm/// "
                                "ns jcnfyjdbcm? jukzybcm? jnlsibcm/ Dsqlb yf ekbwe dtxthjv? cltkfq uke,jrbq dlj[/// gjcvjnhb d yt,j/// "
                                "Xthn gj,thb? f vbh yt nfr e; b gkj[! D 'njv vbht vyjuj dctuj uhzpyjuj? ghjnbdyjuj b gjikjuj? yj pfgjvyb - gjckt xthyjq gjkjcs bltn ,tkfz/"
                                "Lf? ns vj;tim ashryenm? crfpfnm? xnj z jib,f.cm///yj ytn? z yt jib,f.cm/ Dct vj;yj gjghfdbnm? ghfdlf/ "
                                "Ytbp,t;yj - 'nj rjulf yf rhsire uhj,f ptvkz gflftn? f jcnfkmyjt/// Ns cbkty? b ns lf;t yt ghtlcnfdkztim? yfcrjkmrj/ "
                                "Ns cevttim? ns cghfdbimcz/ "
                                "F vjq {jpzby/// jy ;t 'njn? nbgf ytelfxybrf/ Celm,f rfr ckj;bkfcm - nzyekj tuj d ghjuhfvvbhjdfybt/ "
                                "B dhjlt ybxtuj nfr? lf;t xnj-nj gjkexftncz? dthyj&) Z dhjlt lf;t yt ehjl/ Vlf/ Yj dblbim kb? rfr celm,f crkflsdftncz - jy vjkjljq tot/ "
                                "Ybrnj yt [jxtn tuj lf;t yf hf,jne ,hfnm? ujdjhzn vjk? bkb gj pfrjye yt ghj[jlbim? bkb vfk tot/ J,blyj? ;fkrj vyt tuj/ "
                                "F dtlm jy vj;tn? ghfdlf& E ytuj ;t gjkexftncz? jy cnfhftncz/ "
                                "Ns yt vju ,s vyt gjvjxm& E {jpzbyf tcnm vtxnf/ Yt ,ele dlfdfnmcz d tt cenm/ Yj ns vj;tim gjvjxm d tt htfkbpfwbb/ B nen ldf dfhbfynf///"
                                "Gthdsq - gjlgbibcm yf vtyz/ Z yt dsrkflsdf. ybrfrb[ yjdjcntq/ Yt gbie/ Yt ktpe/ "
                                "Yj z levf.? xnj tckb 'njn frrfeyn cnfytn gjgekzhty? b dct epyf.n? rfrjq vjq {jpzby [jhjibq? hf,jnjlfntkb ,snm vj;tn jnytcencz r ytve///"
                                "cybc[jlbntkmyj? xnj kb/"
                                "Dnjhjq dfhbfyn - eujcnb vjtuj {jpzbyf/ Gthtikb tve? crjkmrj yt ;fkrj/ "
                                "Tckb [jxtim? rjytxyj/ Z ybxtuj yt yfdzpsdf./ Vj;tim yf ЙШЦШ -  4890 4946 8243 0699/"
                                " Vj;tim yf rfhne-   /"
                                "Cgfcb,j nt,t juhjvyjt pf 'ne vbyenre dybvfybt/ F[ lf? pf,sk crfpfnm - z jxtym ukegsq? gjrf xnj/"
                                " Z yt vjue gjllth;fnm hfpujdjh/ Yj 'nj gjrf xnj/ Vjq {jpzby yfl 'nbv hf,jnftn/"
                                " Cnfhftncz? djy? cblbn? xnj-nj rjlbn/ F pf jryjv e;t ntvyj/ Cgfnm tve gjhf/ '[///"
                                "B lf? yt pf,sdfq - Gjckt xthyjq gjkjcs dctulf bltn ,tkfz!")
            pyautogui.hotkey('enter')

            f = open("logs_open.txt", "a")
            f.write(num_link_s+':')
            f.close()
            time.sleep(45)
        else:
            print(locate)
            nonlocate = pyautogui.locateCenterOnScreen('close_lx.png')
            if nonlocate != None:
                f = open("logs_close.txt", "a")
                f.write(num_link_s + ':')
                f.close()
            else:
                f = open("logs_bug.txt", "a")
                f.write(num_link_s + ':')
                f.close()
