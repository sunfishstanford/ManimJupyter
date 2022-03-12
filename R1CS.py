from manim import *

# ffmpeg -i ./media/videos/R1CS/480p15/Formula.mp4 -loop 0 fig1.gif
# https://superuser.com/questions/556029/how-do-i-convert-a-video-to-gif-using-ffmpeg-with-reasonable-quality

class Formula(Scene):
    def substitute(self, src, srceq, dest,desteq, neweq, finaleq=None):
        framebox1 = SurroundingRectangle(src, buff = .1)
        framebox2 = SurroundingRectangle(dest, buff = .1)
        self.play(Create(framebox1))
        self.play(ReplacementTransform(framebox1,framebox2))
        self.wait()
        self.remove(framebox2)
        self.remove(srceq)
        self.add(src)
        neweq.align_to(desteq,LEFT).align_to(desteq,DOWN)
        self.play(TransformMatchingShapes(Group(src,desteq), neweq))
        if finaleq is not None:
            finaleq.align_to(desteq,LEFT).align_to(desteq,DOWN)
            self.play(TransformMatchingShapes(neweq,finaleq))        
        
    def construct(self):

        t1 = MathTex("sym_1=", "x * x")
        t2 = MathTex("y=", "sym_1", "* x")
        t2new = MathTex("y = x * x * x")
        t2final = MathTex("y=","x^3")
        t3 = MathTex("sym_2 =","y","+ x")
        t3new = MathTex("sym_2=","x^3+ x")
        t4 = MathTex("Out = ","sym_2","+5")
        t4new = MathTex("Out = x^3+x+5")
        t1.shift(UP)
        t2.next_to(t1,DOWN,buff=0.3)
        t3.next_to(t2,DOWN,buff=0.3)
        t4.next_to(t3,DOWN,buff=0.3)
        self.add(t1,t2,t3,t4)
        self.wait()
        
        self.substitute(t1[1], t1, t2[1], t2, t2new, t2final)
        self.wait()
#         src, srceq, dest, desteq, neweq, finaleq
#         src=t1[2]
#         srceq = t1
#         dest=t2[2]
#         desteq=t2
#         neweq=t2p
#         finaleq=t2pp

        self.substitute(t2final[1], t2final, t3[1], t3, t3new)
        self.wait()
        self.substitute(t3new[1], t3new, t4[1], t4, t4new)
    
        self.wait(duration=5)
#         self.play(Write(formula), run_time=30)


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

    def construct(self):

        vars = MathTex("one \quad", "x \quad", "out \quad", "sym_1 \quad", "y \quad", "sym_2")
        val=[]
        val.append(MathTex("1 \quad","3 \quad","? \quad","? \quad","? \quad","?"))
        val.append(MathTex("1 \quad","3 \quad","? \quad","9 \quad","? \quad","?"))
        val.append(MathTex("1 \quad","3 \quad","? \quad","9 \quad","27 \quad","?"))
        val.append(MathTex("1 \quad","3 \quad","? \quad","9 \quad","27 \quad","30"))
        val.append(MathTex("1 \quad","3 \quad","35 \quad","9 \quad","27 \quad","30"))
        vars.shift([0,2.7,0])
        self.add(vars)
        for i,x in enumerate(val):
            x.shift([0,2,0])
            for j in range(len(vars)):
                x[j].align_to(vars[j],LEFT)
        self.add(val[0])
        
        eqa, eqb, eqc = [],[],[]
        eqa.append(MathTex("sym_1 = x * x"))
        eqb.append(MathTex("sym_1 = 3 * 3"))
        eqc.append(MathTex("9=3*3"))
        
        eqa.append(MathTex("y = sym_1 * x"))
        eqb.append(MathTex("y = 9*3"))
        eqc.append(MathTex("27=9*3"))

        eqa.append(MathTex("sym_2 = y+ x"))
        eqb.append(MathTex("sym_2 = 27 + 3"))
        eqc.append(MathTex("30 = 27 + 3"))

        eqa.append(MathTex("out = sym_2 + 5"))
        eqb.append(MathTex("out = 30 + 5"))
        eqc.append(MathTex("35 = 30 + 5"))

        for i in range(1,len(eqa)):
            eqa[i].next_to(eqa[i-1],DOWN,buff=0.3)
        for i in range(len(eqa)):
            self.add(eqa[i])
            self.overlap(eqa[i],eqb[i])
            self.overlap(eqa[i],eqc[i])
     
        for i in range(len(eqa)-1):
            self.plugfly(val[i],eqa[i],eqb[i])
            self.calc(eqa[i],eqb[i],eqc[i])
            self.plugfade(eqc[i],val[i],val[i+1])
            
# need to hand tune the 4th equation
        i=3
        self.plugfade(val[i],eqa[i],eqb[i])
        self.calc(eqa[i],eqb[i],eqc[i])
        self.plugfade(eqc[i],val[i],val[i+1])
        
        self.wait(duration=5)
