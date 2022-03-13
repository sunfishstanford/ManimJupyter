from manim import *

# manim -pql R1CS.py Formula
# manim -pql R1CS.py CalcWitness
# manim -pql R1CS.py R1CS1
# manim -pql R1CS.py R1CS3
# ffmpeg -i ./media/videos/R1CS/480p15/Formula.mp4 -loop 0 fig1.gif
# ffmpeg -i ./media/videos/R1CS/480p15/CalcWitness.mp4 -loop 0 fig2.gif
# ffmpeg -i ./media/videos/R1CS/480p15/CalcWitness.mp4 -vf reverse -loop 0 fig2reverse.gif
# ffmpeg -i ./media/videos/R1CS/480p15/R1CS1.mp4 -loop 0 fig3.gif
# ffmpeg -i ./media/videos/R1CS/480p15/R1CS3.mp4 -loop 0 fig4.gif

# https://superuser.com/questions/556029/how-do-i-convert-a-video-to-gif-using-ffmpeg-with-reasonable-quality

# fig 1
#

class Formula(Scene):
    def focus(self, src, dest):
        framebox1 = SurroundingRectangle(src, buff = .1)
        framebox2 = SurroundingRectangle(dest, buff = .1)
        self.play(Create(framebox1))
        self.play(ReplacementTransform(framebox1,framebox2))
        self.wait(duration=0.1)
        self.remove(framebox2)

    def initlayout(self, eq): # setup initial layout
        eqtprev = None
        eqt = []
        for i,x in enumerate(eq):
            a = MathTex(*x[:-1])
            eqt.append(a)
            if i==0:
                a.shift([0,1.5,0])
            if x[-1]=="disp":                
                if eqtprev is not None:
                    a.next_to(eqtprev,DOWN, buff=0.3)
                self.add(a)
                eqtprev=a
        return(eqt)
                
    def xf(self, eqt, idx): # transform                
        for i,x in enumerate(idx):
            src,dest,op = x
            if type(src)==tuple:
                a = eqt[src[0]][src[1]]
                b = eqt[dest[0]][dest[1]]

                aa = a.copy()
                aa.move_to(b.get_center())
                if op!='nofocus':
                    self.focus(a,b)
                if op=='rm':
                    self.remove(eqt[src[0]])
                self.play(Transform(b,aa))
                self.wait(duration=0.5)
            else:
                a = eqt[src]
                b = eqt[dest]
                aa = a.copy().move_to(b.get_center())
                eqt[dest] = aa
                self.remove(b)
                self.play(Indicate(aa))
                if op=='rm':
                    self.remove(a)
                self.wait(duration=0.5)
                
                                
    def construct(self):

        t1 = []
        t1.append(["sym_1=", "x * x", 'disp']) # eq 0
        t1.append(["y=",     "sym_1", "* x", 'disp']) # eq 1
        t1.append(["y =","x^3", 'nodisp']) # eq 2
        t1.append(["sym_2 =","y","+ x", 'disp']) # eq 3
        t1.append(["sym_2 = ","x^3+x", 'nodisp']) # eq 4
        t1.append(["out = ","sym_2","+5", 'disp']) # eq 5
        t1.append(["out = x^3+x+5", 'nodisp']) # eq 6
        eqt = self.initlayout(t1)
        self.xf(eqt,[[(0,1),(1,1),'rm'],
                    [2,1,''],
                    [(1,1),(3,1),'rm'],
                    [4,3,''],
                    [(3,1),(5,1),'rm'],
                    [6,5,'']
                   ])

        """
        Here, the meaning is:
        (0,1) = "x * x"
        (1,1) = "sym_1"

        'rm' in the first commmand = remove (0,1) as part of transforming 
        (1,1) into (0,1)

        2 = ["y =","x^3", 'nodisp']
        1 = "y=",     "sym_1", "* x", 'disp']
        '' in the second command = transform eq 1 into eq 2, and don't touch 
        eq 2 (in this case, because eq 2 was never displayed)
        
        Also, 'nofocus' in the command = don't run the focus box, and 
        don't remove (no 'rm')
        """
        self.wait(duration=2)



# fig 2
#

class CalcWitness(Scene):
    def focus(self, src, dest):
        framebox1 = SurroundingRectangle(src, buff = .1)
        framebox2 = SurroundingRectangle(dest, buff = .1)
        self.play(Create(framebox1))
        self.play(ReplacementTransform(framebox1,framebox2))
        self.wait(duration=0.1)
        self.remove(framebox2)

    def initlayout(self, eq): # setup initial layout
        eqt = []
        for x in eq:
            a = MathTex(*x[:-1])
            eqt.append(a)
        eqt[0].shift([0,2.5,0])
        eqt[1].shift([0,2,0])
        for i in range(len(eqt[0])):
            eqt[1][i].align_to(eqt[0][i],RIGHT)
        eqt[2].shift([0,0.5,0])
        self.add(eqt[0],eqt[1],eqt[2])
        eqtprev = eqt[2]
        for i in range(3,len(eq)):
            if eq[i][-1]=="disp":                
                a=eqt[i]
                a.next_to(eqtprev,DOWN, buff=0.3)
                self.add(a)
                eqtprev=a
        return(eqt)
                
    def xf(self, eqt, idx): # transform                
        for i,x in enumerate(idx):
            src,dest,op = x
            if type(src)==tuple:
                a = eqt[src[0]][src[1]]
                b = eqt[dest[0]][dest[1]]

                aa = a.copy()
                aa.move_to(b.get_center())
                if op!='nofocus':
                    self.focus(a,b)
                if op=='rm':
                    self.remove(eqt[src[0]])
                self.play(Transform(b,aa))
                self.wait(duration=0.5)
            else:
                a = eqt[src]
                b = eqt[dest]
                aa = a.copy().move_to(b.get_center())
                eqt[dest] = aa
                self.remove(b)
                self.play(Indicate(aa))
                if op=='rm':
                    self.remove(a)
                self.wait(duration=0.5)
                        
    def construct(self):
        t1 = []
        t1.append(['one', '\quad', 'x', '\quad', "out", "\quad", "sym_1", "\quad", "y", "\quad", "sym_2",'disp'])
        t1.append(["1","\quad","3","\quad","?","\quad","?","\quad","?",'\quad',"?",'disp']) # eq 1
        t1.append(["sym_1","=", "x", '*', 'x', 'disp']) # eq 2
        t1.append(['9','=3*3', 'nodisp']) # eq 3

        t1.append(["y","=","sym_1", "*","x", 'disp']) # eq 4
        t1.append(['27','=9*3', 'nodisp']) # eq 5

        t1.append(["sym_2","=","y","+","x",'disp']) # eq 6
        t1.append(["30","=27+3", 'nodisp']) # eq 7

        t1.append(["out", "=","sym_2","+5", 'disp']) # eq 8
        t1.append(["35","=30+5", 'nodisp']) # eq 9
        
        eqt = self.initlayout(t1)
        self.xf(eqt,[[(1,2),(2,2),''],
                    [(1,2),(2,4),''],
                    [(3,0),(2,0),'nofocus'],
                    [3,2,''],
                    [(2,0),(1,6),''],

                    [(1,6),(4,2),''],
                    [(1,2),(4,4),''],
                    [(5,0),(4,0),'nofocus'],
                    [5,4,''],
                    [(4,0),(1,8),''],

                    [(1,8),(6,2),''],
                    [(1,2),(6,4),''],
                    [(7,0),(6,0),'nofocus'],
                    [7,6,''],
                    [(6,0),(1,10),''],

                    [(1,10),(8,2),''],
                    [(9,0),(8,0),'nofocus'],
                    [9,8,''],
                    [(8,0),(1,4),''],

                    ])

        self.wait(duration=2)


# fig 3
#

class R1CS1(Scene):
    def focus(self, src, dest=None):
        framebox1 = SurroundingRectangle(src, buff = .1)
        self.play(Create(framebox1))
        if dest is not None:
            framebox2 = SurroundingRectangle(dest, buff = .1)
            self.play(ReplacementTransform(framebox1,framebox2))
            self.wait(duration=0.1)
            self.remove(framebox2)
        else:
            self.wait(duration=0.1)
            self.remove(framebox1)
            

    def initlayout(self, eq): # setup initial layout
        eqt = []
        for x in eq:
            a = MathTex(*x)
            eqt.append(a)
        eqt[0].shift([0,-2.5,0])
        eqt[1].move_to(eqt[0].get_center())
        self.add(eqt[0])
        for i in range(5):
            eqt[1][i].align_to(eqt[1][i+6],RIGHT)
        self.wait(duration=2)
        A = Group()
        B = Group()
        C = Group()
        for i in range(2,8):
            A.add(MathTex(*eq[i],font_size=20))
            B.add(MathTex(*eq[i],font_size=20))
            C.add(MathTex(*eq[i],font_size=20))
        A.arrange(direction=DOWN)
        B.arrange(direction=DOWN)
        C.arrange(direction=DOWN)
        A.shift([-4.5,1,0])
        B.shift([-0.5,1,0])
        C.shift([3.5,1,0])
        Aprod = Group()
        Avec = Group()
        Aprod.add(A[0][5])
        Avec.add(A[0][3])
        Bprod = Group()
        Bvec = Group()
        Bprod.add(B[0][5])
        Bvec.add(B[0][3])
        Cprod = Group()
        Cvec = Group()
        Cprod.add(C[0][5])
        Cvec.add(C[0][3])
        for i in range(1,len(A)):
            Aprod.add(A[i][5])
            Avec.add(A[i][3])
            Bprod.add(B[i][5])
            Bvec.add(B[i][3])
            Cprod.add(C[i][5])
            Cvec.add(C[i][3])
            for j in range(len(A[i])):
                A[i][j].align_to(A[0][j],RIGHT)
                B[i][j].align_to(B[0][j],RIGHT)
                C[i][j].align_to(C[0][j],RIGHT)
        f1 = SurroundingRectangle(Avec,buff=0.15,color=BLUE)
        f2 = SurroundingRectangle(Aprod,buff=0.15,color=GREEN)
        f3 = SurroundingRectangle(Bvec,buff=0.15,color=BLUE)
        f4 = SurroundingRectangle(Bprod,buff=0.15,color=GREEN)
        f5 = SurroundingRectangle(Cvec,buff=0.15,color=BLUE)
        f6 = SurroundingRectangle(Cprod,buff=0.15,color=GREEN)
        topeq = MathTex(*eq[1][:6],font_size=30)
        topeq.shift([0,-0.8,0])
        topeq[0].align_to(Aprod,RIGHT)
        topeq[2].align_to(Bprod,RIGHT)
        topeq[4].align_to(Cprod,RIGHT)
        ty = topeq[0].get_y()
        tx1 = 0.5*(topeq[0].get_x()+topeq[2].get_x())
        topeq[1].move_to([tx1,ty,0])
        tx2 = 0.5*(topeq[2].get_x()+topeq[4].get_x())
        topeq[3].move_to([tx2,ty,0])
        topeq[5].next_to(topeq[4],RIGHT,buff=1)
        label = MathTex(*eq[-1])
        label.next_to(f1,UP)
        label[0].align_to(A[0][1],RIGHT)
        label[1].align_to(A[0][3],RIGHT)
        label[2].align_to(B[0][1],RIGHT)
        label[3].align_to(B[0][3],RIGHT)
        label[4].align_to(C[0][1],RIGHT)
        label[5].align_to(C[0][3],RIGHT)

        self.play(Transform(eqt[0],eqt[1]))
        self.add(A,B,C,f1,f2,f3,f4,f5,f6,label)
        self.play(Create(topeq))
        return(topeq,Avec,Aprod,Bvec,Bprod,Cvec,Cprod)
                
    def xf(self, cmd): # transform  
        for x in cmd:
        # 3 types of commands:
        # 1. element 0 = tuple: plug the int into all object in tuple, no focus
        # 2. if not 1, then if element 1 = int: plug in the int into obj 1, add focus
        # 3. neither 1 nor 2: transfer from src to dest
            if type(x[0])==tuple:
                a = MathTex(x[1],font_size=20)
                for b in x[0]:
                    aa = a.copy()
                    aa.move_to(b.get_center())
                    self.play(Transform(b,aa))
                    self.wait(duration=0.1)                    
            elif type(x[1])==int:
                a = MathTex(x[1],font_size=20)
                b = x[0]
                aa = a.copy()
                aa.move_to(b.get_center())
                self.focus(b)
                self.play(Transform(b,aa))
                self.wait(duration=0.5)                    
            else:                
                a = x[0]
                b = x[1]
                aa = a.copy()
                aa.move_to(b.get_center())
                self.focus(a,b)
                self.play(Transform(b,aa))
                self.wait(duration=0.5)
                        
    def construct(self):
        t1 = []
        t1.append(['9','&=','3','*',r'3\\','sym_1','&=','x','*','x'])
        t1.append(['3','*','3','-','9',r'&=0\\','x','*','x','-','sym_1','&=0'])
        t1.append(['one','\quad 1','\quad * \quad','?','\quad = \quad','?'])
        t1.append(['x',' \quad 3','\quad * \quad','?','\quad = \quad','?'])
        t1.append(['out',' \quad 35','\quad * \quad','?','\quad = \quad','?'])
        t1.append(['sym_1',' \quad 9','\quad * \quad','?','\quad = \quad','?'])
        t1.append(['y',' \quad 27','\quad * \quad','?','\quad = \quad','?'])
        t1.append(['sym_2',' \quad 30','\quad * \quad','?','\quad = \quad','?'])
        t1.append(['s','a','s','b','s','c'])
        
        t,a,ap,b,bp,c,cp = self.initlayout(t1)
        self.wait(duration=3)
        self.xf([
            [t[0],ap[1]] , [a[1],1] , 
            [(a[0],a[2],a[3],a[4],a[5],ap[0],ap[2],ap[3],ap[4],ap[5]),0],
            [t[2],bp[1]] , [b[1],1] , 
            [(b[0],b[2],b[3],b[4],b[5],bp[0],bp[2],bp[3],bp[4],bp[5]),0],
            [t[4],cp[3]] , [c[3],1] , 
            [(c[0],c[1],c[2],c[4],c[5],cp[0],cp[1],cp[2],cp[4],cp[5]),0],
                    ])
        self.wait(duration=10)


# fig 4
#

class R1CS3(Scene):
    def focus(self, src, dest=None):
        framebox1 = SurroundingRectangle(src, buff = .1)
        self.play(Create(framebox1))
        if dest is not None:
            framebox2 = SurroundingRectangle(dest, buff = .1)
            self.play(ReplacementTransform(framebox1,framebox2))
            self.wait(duration=0.1)
            self.remove(framebox2)
        else:
            self.wait(duration=0.1)
            self.remove(framebox1)
            

    def initlayout(self, eq): # setup initial layout
        eqt = []
        for x in eq:
            a = MathTex(*x)
            eqt.append(a)
        eqt[0].shift([0,-2.5,0])
        eqt[1].move_to(eqt[0].get_center())
        eqt[2].move_to(eqt[0].get_center())
        self.add(eqt[0])
        for i in range(5):
            eqt[1][i].align_to(eqt[1][i+6],RIGHT)
        self.wait(duration=2)
        A = Group()
        B = Group()
        C = Group()
        for i in range(3,9):
            A.add(MathTex(*eq[i],font_size=20))
            B.add(MathTex(*eq[i],font_size=20))
            C.add(MathTex(*eq[i],font_size=20))
        A.arrange(direction=DOWN)
        B.arrange(direction=DOWN)
        C.arrange(direction=DOWN)
        A.shift([-4.5,1,0])
        B.shift([-0.5,1,0])
        C.shift([3.5,1,0])
        Aprod = Group()
        Avec = Group()
        Aprod.add(A[0][5])
        Avec.add(A[0][3])
        Bprod = Group()
        Bvec = Group()
        Bprod.add(B[0][5])
        Bvec.add(B[0][3])
        Cprod = Group()
        Cvec = Group()
        Cprod.add(C[0][5])
        Cvec.add(C[0][3])
        for i in range(1,len(A)):
            Aprod.add(A[i][5])
            Avec.add(A[i][3])
            Bprod.add(B[i][5])
            Bvec.add(B[i][3])
            Cprod.add(C[i][5])
            Cvec.add(C[i][3])
            for j in range(len(A[i])):
                A[i][j].align_to(A[0][j],RIGHT)
                B[i][j].align_to(B[0][j],RIGHT)
                C[i][j].align_to(C[0][j],RIGHT)
        f1 = SurroundingRectangle(Avec,buff=0.15,color=BLUE)
        f2 = SurroundingRectangle(Aprod,buff=0.15,color=GREEN)
        f3 = SurroundingRectangle(Bvec,buff=0.15,color=BLUE)
        f4 = SurroundingRectangle(Bprod,buff=0.15,color=GREEN)
        f5 = SurroundingRectangle(Cvec,buff=0.15,color=BLUE)
        f6 = SurroundingRectangle(Cprod,buff=0.15,color=GREEN)
        topeq = MathTex(*eq[2][:10],font_size=30)
        topeq.shift([0,-0.8,0])
        topeq[0].align_to(Aprod,RIGHT).shift([-1,0,0])
        topeq[1].next_to(topeq[0],RIGHT)
        topeq[2].next_to(topeq[1],RIGHT)
        topeq[3].next_to(topeq[2],RIGHT)
        topeq[4].next_to(topeq[3],RIGHT)

        topeq[6].align_to(Bprod,RIGHT) # 1
        topeq[8].align_to(Cprod,RIGHT) # 30
        ty = topeq[0].get_y()
        tx1 = 0.5*(topeq[2].get_x()+topeq[6].get_x())
        topeq[5].move_to([tx1,ty,0]) # *
        tx2 = 0.5*(topeq[6].get_x()+topeq[8].get_x())
        topeq[7].move_to([tx2,ty,0]) # -
        topeq[9].next_to(topeq[8],RIGHT,buff=1)
        label = MathTex(*eq[-1])
        label.next_to(f1,UP)
        label[0].align_to(A[0][1],RIGHT)
        label[1].align_to(A[0][3],RIGHT)
        label[2].align_to(B[0][1],RIGHT)
        label[3].align_to(B[0][3],RIGHT)
        label[4].align_to(C[0][1],RIGHT)
        label[5].align_to(C[0][3],RIGHT)

        self.play(Transform(eqt[0],eqt[1]))
        self.play(Transform(eqt[0],eqt[2]))
        self.add(A,B,C,f1,f2,f3,f4,f5,f6,label)
        self.play(Create(topeq))
        return(topeq,Avec,Aprod,Bvec,Bprod,Cvec,Cprod)
                
    def xf(self, cmd): # transform  
        for x in cmd:
        # 3 types of commands:
        # 1. element 0 = tuple: plug the int into all object in tuple, no focus
        # 2. if not 1, then if element 1 = int: plug in the int into obj 1, add focus
        # 3. neither 1 nor 2: transfer from src to dest
            if type(x[0])==tuple:
                a = MathTex(x[1],font_size=20)
                for b in x[0]:
                    aa = a.copy()
                    aa.move_to(b.get_center())
                    self.play(Transform(b,aa))
                    self.wait(duration=0.1)                    
            elif type(x[1])==int:
                a = MathTex(x[1],font_size=20)
                b = x[0]
                aa = a.copy()
                aa.move_to(b.get_center())
                self.focus(b)
                self.play(Transform(b,aa))
                self.wait(duration=0.5)                    
            else:                
                a = x[0]
                b = x[1]
                aa = a.copy()
                aa.move_to(b.get_center())
                self.focus(a,b)
                self.play(Transform(b,aa))
                self.wait(duration=0.5)
                        
    def construct(self):
        t1 = []
        t1.append(['30','&=','27','+',r'3\\','sym_2','&=','y','+','x'])
        t1.append(['27','+','3','-','30',r'&=0\\','y','+','x','-','sym_2','&=0'])
        t1.append(['(','27','+','3',')','*','1','-','30',r'&=0\\','y','+','x','-','sym_2','&=0'])
        t1.append(['one','\quad 1','\quad * \quad','?','\quad = \quad','?'])
        t1.append(['x',' \quad 3','\quad * \quad','?','\quad = \quad','?'])
        t1.append(['out',' \quad 35','\quad * \quad','?','\quad = \quad','?'])
        t1.append(['sym_1',' \quad 9','\quad * \quad','?','\quad = \quad','?'])
        t1.append(['y',' \quad 27','\quad * \quad','?','\quad = \quad','?'])
        t1.append(['sym_2',' \quad 30','\quad * \quad','?','\quad = \quad','?'])
        t1.append(['s','a','s','b','s','c'])
        
        t,a,ap,b,bp,c,cp = self.initlayout(t1)
        self.wait(duration=3)
        self.xf([
            [t[1],ap[4]], [t[3],ap[1]], [a[4],1] , [a[1],1],
            [(a[0], a[2],a[3],a[5],ap[0],ap[2],ap[3],ap[5]),0],
            [t[6],bp[0]] , [b[0],1] , 
            [(b[1],b[2],b[3],b[4],b[5],bp[1],bp[2],bp[3],bp[4],bp[5]),0],
            [t[8],cp[5]] , [c[5],1] , 
            [(c[0],c[1],c[2],c[3],c[4],cp[0],cp[1],cp[2],cp[3],cp[4]),0],
                    ])
        self.wait(duration=10)
