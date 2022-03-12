from manim import *

# manim -pql R1CS.py Formula
# manim -pql R1CS.py CalcWitness
# ffmpeg -i ./media/videos/R1CS/480p15/Formula.mp4 -loop 0 fig1.gif
# ffmpeg -i ./media/videos/R1CS/480p15/CalcWitness.mp4 -loop 0 fig2.gif
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
        t1.append(["Out = ","sym_2","+5", 'disp']) # eq 5
        t1.append(["Out = x^3+x+5", 'nodisp']) # eq 6
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
    def plugfly(self, src, dest, destnew):
        self.play(TransformMatchingShapes(Group(src,dest),Group(src,destnew)),run_time=3)

    def plugfade(self, src, dest, destnew):
        self.play(ReplacementTransform(Group(src,dest),Group(src,destnew)),run_time=3)

    def calc(self, eq, eqnew, eqfinal):
        self.remove(eqnew[0])
        self.play(TransformMatchingShapes(Group(eq,eqnew),eqfinal))
#         self.play(TransformMatchingShapes(Group(eq[0],eqnew[1]),eqfinal))
        
    def overlap(self, first, second):
        second.align_to(first,LEFT).align_to(first,DOWN)

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

        t1.append(["Out", "=","sym_2","+5", 'disp']) # eq 8
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
