#Importing libraries
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox as msg

#Main class
class quizApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('400x560+550+80')
        self.root.title('Qiuz App')
        self.root.configure(bg='white')
        self.root.resizable(0, 0)
        self.root.focus_force

        #Image logo
        self.img = Image.open(r"images\quizlogo.jpg")
        self.img = self.img.resize((400,300))
        self.img = ImageTk.PhotoImage(self.img)
        self.image1 = Label(self.root, image=self.img, border=0).pack(pady=20)

        # Designer
        Label(self.root, text="designed by", fg="grey", bg='white').place(x=172, y=520)
        Label(self.root, text="KIRAN KILVA", font="Helvetica 10", bg='white').place(x=165, y=538)

        self.btn = Button(self.root, text="CONTINUE", padx=79, font="commissars 11 bold", bd=1, bg="#1E90FF", fg="white",
                    activebackground="#1E90FF", activeforeground="white", cursor="hand2", command=self.new_frame1)
        self.btn.place(x=80, y=450)

        #All variables
        self.check = IntVar()
        self.radio1 = IntVar()
        self.radio2 = IntVar()
        self.radio3 = IntVar()
        self.radio4 = IntVar()
        self.radio5 = IntVar()
        self.radio6 = IntVar()
        self.radio7 = IntVar()
        self.radio8 = IntVar()
        self.radio9 = IntVar()
        self.radio10 = IntVar()

        self.rule = ['RULES AND REGULATIONS',
                     '- Quiz is on General Knowledge consists of 10 Questions',
                     '- Correct answer will gives 1 point',
                     '- Wrong answer will gives 0 point',
                     '- Once you select Radio button that will be a final answer',
                     '- Hence think before you select',
                     'Final score is displayed when you finished all the questions.']

        #Questions
        self.questions = ['Who is known as Father Of Indian Space Pragramme?',
                          "Whose birthday is celebrated as 'Vishwa Manava Dina'?",
                          "The image of Hampi's stone chariot is printed on which of these Indian Face Values?",
                          "Who is called the 'Father of Plastic Surgery'?",
                          "When did Shivana Samudra Hydroelectric Centre was started?",
                          "Which is a Folk dance of Karnataka?",
                          "The ruins of Hampi were brought to light in 1800 by",
                          "When did Krishnadeva Raya died?",
                          "Hitler party which came into power in 1933 is known as",
                          "First China War was fought between"]
        
        #Options
        self.options = [['Rakesh Sharma', 'Abdul Kalam', 'Vikram Saaraabhai', 'None of the Above'],
                        ['Dr. B R Ambedkar', 'Kuvempu', 'Sir M Vishveshwarya', 'Dr. C V Raman'],
                        ['Rs. 10', 'Rs. 20', 'Rs. 50', 'Rs. 100'],
                        ['Vishwamitra', 'Shushruta', 'Chanakya', 'Kautilya'],
                        ['1900', '1901', '1902', '1903'],
                        ['Lavani', 'Bihu', 'Chhau', 'Nati'],
                        ['Alexander Greenlaw', 'Colonel Colin Mackenzie', 'Fernao Nuniz', 'J F Fleet'],
                        ['1527 AD', '1529 AD', '1533 AD', '1537 AD'],
                        ['Labour Party', 'Nazi Party', 'Ku-Klux-Klan', 'Democratic Party'],
                        ['China and Britain', 'China and France', 'China and Egypt', 'China and Greek']]

        #User answers
        self.user_ans = []
        
        #Correct answers
        self.ans = [3, 2, 3, 2, 3, 1, 2, 2, 2, 1]
        self.score = 0

    #frame1
    def new_frame1(self):
        frame1 = Frame(self.root, width=400, height=560, bg='white')
        frame1.place(x=0, y=0)

        #Rules 
        Label(frame1, text=self.rule[0], font=('Times New Roman',19,'bold'), bg='white', wraplength=370, justify=LEFT).place(x=25, y=85)
        Label(frame1, text=self.rule[1], font=('Times New Roman',12), bg='white', wraplength=370, justify=LEFT).place(x=27, y=160)
        Label(frame1, text=self.rule[2], font=('Times New Roman',12), bg='white', wraplength=370, justify=LEFT).place(x=27, y=190)
        Label(frame1, text=self.rule[3], font=('Times New Roman',12), bg='white', wraplength=370, justify=LEFT).place(x=27, y=220)
        Label(frame1, text=self.rule[4], font=('Times New Roman',12), bg='white', wraplength=370, justify=LEFT).place(x=27, y=250)
        Label(frame1, text=self.rule[5], font=('Times New Roman',12), bg='white', wraplength=370, justify=LEFT).place(x=27, y=280)
        Label(frame1, text=self.rule[6], font=('Times New Roman',12), bg='white', wraplength=370, justify=LEFT).place(x=27, y=310)

        self.check_btn = Checkbutton(frame1, text='I agree with this rules and regulations', onvalue=1, offvalue=0, variable=self.check,
                                font=('Times New Roman',10), height=2, width=40, bg='white', activebackground='white')
        self.check_btn.place(x=40, y=420)

        self.start_btn = Button(frame1, text="START", padx=79, font="commissars 11 bold", bd=1, bg="#1E90FF", fg="white",
                    activebackground="#1E90FF", activeforeground="white", cursor="hand2", command=self.new_frame2)
        self.start_btn.place(x=85, y=460)

    #frame2
    def new_frame2(self):
        if self.check.get() == 0:
            msg.showinfo('Quiz App', 'Please agree our Rules and Regulations!!')
        else:
            frame2 = Frame(self.root, width=400, height=560, bg='white')
            frame2.place(x=0, y=0)
            
            #Question1
            Label(frame2, text='QUESTION 1', font=('Times New Roman',13,'bold'), bg='white').place(x=20, y=20)
            Label(frame2, text=self.questions[0], font=('Times New Roman',12), bg='white', wraplength=370, justify=LEFT).place(x=22, y=50)
            r1 = Radiobutton(frame2, text=self.options[0][0], value=1, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio1)
            r1.place(x=25, y=80)
            r2 = Radiobutton(frame2, text=self.options[0][1], value=2, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio1)
            r2.place(x=25, y=110)
            r3 = Radiobutton(frame2, text=self.options[0][2], value=3, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio1)
            r3.place(x=25, y=140)
            r4 = Radiobutton(frame2, text=self.options[0][3], value=4, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio1)
            r4.place(x=25, y=170)

            #Question2
            Label(frame2, text='QUESTION 2', font=('Times New Roman',13,'bold'), bg='white').place(x=20, y=270)
            Label(frame2, text=self.questions[1], font=('Times New Roman',12), bg='white', wraplength=370, justify=LEFT).place(x=22, y=300)
            r5 = Radiobutton(frame2, text=self.options[1][0], value=1, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio2)
            r5.place(x=25, y=330)
            r6 = Radiobutton(frame2, text=self.options[1][1], value=2, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio2)
            r6.place(x=25, y=360)
            r7 = Radiobutton(frame2, text=self.options[1][2], value=3, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio2)
            r7.place(x=25, y=390)
            r8 = Radiobutton(frame2, text=self.options[1][3], value=4, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio2)
            r8.place(x=25, y=420)

            self.next1_btn = Button(frame2, text="NEXT", padx=69, font="commissars 11 bold", bd=1, bg="#1E90FF", fg="white",
                        activebackground="#1E90FF", activeforeground="white", cursor="hand2", command=self.new_frame3)
            self.next1_btn.place(x=110, y=500)


    #frame3
    def new_frame3(self):
        if (self.radio1.get() and self.radio2.get()) not in [1, 2, 3, 4]:
            msg.showwarning('Quiz App', 'Please answer all the questions!!')
        else:
            self.user_ans.append(self.radio1.get())
            self.user_ans.append(self.radio2.get())
            frame3 = Frame(self.root, width=400, height=560, bg='white')
            frame3.place(x=0, y=0)

            #Question3
            Label(frame3, text='QUESTION 3', font=('Times New Roman',13,'bold'), bg='white').place(x=20, y=20)
            Label(frame3, text=self.questions[2], font=('Times New Roman',12), bg='white', wraplength=370, justify=LEFT).place(x=22, y=50)
            r9 = Radiobutton(frame3, text=self.options[2][0], value=1, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio3)
            r9.place(x=25, y=100)
            r10 = Radiobutton(frame3, text=self.options[2][1], value=2, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio3)
            r10.place(x=25, y=130)
            r11 = Radiobutton(frame3, text=self.options[2][2], value=3, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio3)
            r11.place(x=25, y=160)
            r12 = Radiobutton(frame3, text=self.options[2][3], value=4, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio3)
            r12.place(x=25, y=190)

            #Question4
            Label(frame3, text='QUESTION 4', font=('Times New Roman',13,'bold'), bg='white').place(x=20, y=270)
            Label(frame3, text=self.questions[3], font=('Times New Roman',12), bg='white', wraplength=370, justify=LEFT).place(x=22, y=300)
            r13 = Radiobutton(frame3, text=self.options[3][0], value=1, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio4)
            r13.place(x=25, y=330)
            r14 = Radiobutton(frame3, text=self.options[3][1], value=2, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio4)
            r14.place(x=25, y=360)
            r15 = Radiobutton(frame3, text=self.options[3][2], value=3, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio4)
            r15.place(x=25, y=390)
            r16 = Radiobutton(frame3, text=self.options[3][3], value=4, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio4)
            r16.place(x=25, y=420)

            self.next2_btn = Button(frame3, text="NEXT", padx=69, font="commissars 11 bold", bd=1, bg="#1E90FF", fg="white",
                        activebackground="#1E90FF", activeforeground="white", cursor="hand2", command=self.new_frame4)
            self.next2_btn.place(x=110, y=500)

        
    #frame4
    def new_frame4(self):
        if (self.radio3.get() and self.radio4.get()) not in [1, 2, 3, 4]:
            msg.showwarning('Quiz App', 'Please answer all the questions!!')
        else:
            self.user_ans.append(self.radio3.get())
            self.user_ans.append(self.radio4.get())
            frame4 = Frame(self.root, width=400, height=560, bg='white')
            frame4.place(x=0, y=0)

            #Question5
            Label(frame4, text='QUESTION 5', font=('Times New Roman',13,'bold'), bg='white').place(x=20, y=20)
            Label(frame4, text=self.questions[4], font=('Times New Roman',12), bg='white', wraplength=370, justify=LEFT).place(x=22, y=50)
            r17 = Radiobutton(frame4, text=self.options[4][0], value=1, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio5)
            r17.place(x=25, y=100)
            r18 = Radiobutton(frame4, text=self.options[4][1], value=2, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio5)
            r18.place(x=25, y=130)
            r19 = Radiobutton(frame4, text=self.options[4][2], value=3, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio5)
            r19.place(x=25, y=160)
            r20 = Radiobutton(frame4, text=self.options[4][3], value=4, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio5)
            r20.place(x=25, y=190)

            #Question6
            Label(frame4, text='QUESTION 6', font=('Times New Roman',13,'bold'), bg='white').place(x=20, y=270)
            Label(frame4, text=self.questions[5], font=('Times New Roman',12), bg='white', wraplength=370, justify=LEFT).place(x=22, y=300)
            r21 = Radiobutton(frame4, text=self.options[5][0], value=1, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio6)
            r21.place(x=25, y=330)
            r22 = Radiobutton(frame4, text=self.options[5][1], value=2, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio6)
            r22.place(x=25, y=360)
            r23 = Radiobutton(frame4, text=self.options[5][2], value=3, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio6)
            r23.place(x=25, y=390)
            r24 = Radiobutton(frame4, text=self.options[5][3], value=4, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio6)
            r24.place(x=25, y=420)

            self.next3_btn = Button(frame4, text="NEXT", padx=69, font="commissars 11 bold", bd=1, bg="#1E90FF", fg="white",
                        activebackground="#1E90FF", activeforeground="white", cursor="hand2", command=self.new_frame5)
            self.next3_btn.place(x=110, y=500)


    #frame5
    def new_frame5(self):
        if (self.radio5.get() and self.radio6.get()) not in [1, 2, 3, 4]:
            msg.showwarning('Quiz App', 'Please answer all the questions!!')
        else:
            self.user_ans.append(self.radio5.get())
            self.user_ans.append(self.radio6.get())
            frame5 = Frame(self.root, width=400, height=560, bg='white')
            frame5.place(x=0, y=0)

            #Question7 
            Label(frame5, text='QUESTION 7', font=('Times New Roman',13,'bold'), bg='white').place(x=20, y=20)
            Label(frame5, text=self.questions[6], font=('Times New Roman',12), bg='white', wraplength=370, justify=LEFT).place(x=22, y=50)
            r25 = Radiobutton(frame5, text=self.options[6][0], value=1, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio7)
            r25.place(x=25, y=80)
            r26 = Radiobutton(frame5, text=self.options[6][1], value=2, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio7)
            r26.place(x=25, y=110)
            r27 = Radiobutton(frame5, text=self.options[6][2], value=3, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio7)
            r27.place(x=25, y=140)
            r28 = Radiobutton(frame5, text=self.options[6][3], value=4, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio7)
            r28.place(x=25, y=170)

            #Question8  
            Label(frame5, text='QUESTION 8', font=('Times New Roman',13,'bold'), bg='white').place(x=20, y=270)
            Label(frame5, text=self.questions[7], font=('Times New Roman',12), bg='white', wraplength=370, justify=LEFT).place(x=22, y=300)
            r29 = Radiobutton(frame5, text=self.options[7][0], value=1, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio8)
            r29.place(x=25, y=330)
            r30 = Radiobutton(frame5, text=self.options[7][1], value=2, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio8)
            r30.place(x=25, y=360)
            r31 = Radiobutton(frame5, text=self.options[7][2], value=3, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio8)
            r31.place(x=25, y=390)
            r32 = Radiobutton(frame5, text=self.options[7][3], value=4, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio8)
            r32.place(x=25, y=420)

            self.next4_btn = Button(frame5, text="NEXT", padx=69, font="commissars 11 bold", bd=1, bg="#1E90FF", fg="white",
                        activebackground="#1E90FF", activeforeground="white", cursor="hand2", command=self.new_frame6)
            self.next4_btn.place(x=110, y=500)


    #frame6
    def new_frame6(self):
        if (self.radio7.get() and self.radio8.get()) not in [1, 2, 3, 4]:
            msg.showwarning('Quiz App', 'Please answer all the questions!!')
        else:
            self.user_ans.append(self.radio7.get())
            self.user_ans.append(self.radio8.get())
            frame6 = Frame(self.root, width=400, height=560, bg='white')
            frame6.place(x=0, y=0)

            #Question9   
            Label(frame6, text='QUESTION 9', font=('Times New Roman',13,'bold'), bg='white').place(x=20, y=20)
            Label(frame6, text=self.questions[8], font=('Times New Roman',12), bg='white', wraplength=370, justify=LEFT).place(x=22, y=50)
            r33 = Radiobutton(frame6, text=self.options[8][0], value=1, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio9)
            r33.place(x=25, y=80)
            r34 = Radiobutton(frame6, text=self.options[8][1], value=2, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio9)
            r34.place(x=25, y=110)
            r35 = Radiobutton(frame6, text=self.options[8][2], value=3, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio9)
            r35.place(x=25, y=140)
            r36 = Radiobutton(frame6, text=self.options[8][3], value=4, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio9)
            r36.place(x=25, y=170)

            #Question10   
            Label(frame6, text='QUESTION 10', font=('Times New Roman',13,'bold'), bg='white').place(x=20, y=270)
            Label(frame6, text=self.questions[9], font=('Times New Roman',12), bg='white', wraplength=370, justify=LEFT).place(x=22, y=300)
            r37 = Radiobutton(frame6, text=self.options[9][0], value=1, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio10)
            r37.place(x=25, y=330)
            r38 = Radiobutton(frame6, text=self.options[9][1], value=2, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio10)
            r38.place(x=25, y=360)
            r39 = Radiobutton(frame6, text=self.options[9][2], value=3, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio10)
            r39.place(x=25, y=390)
            r40 = Radiobutton(frame6, text=self.options[9][3], value=4, bg='white', font=('Times New Roman',11), activebackground='white', variable=self.radio10)
            r40.place(x=25, y=420)

            self.next5_btn = Button(frame6, text="SUBMIT", padx=69, font="commissars 11 bold", bd=1, bg="#1E90FF", fg="white",
                        activebackground="#1E90FF", activeforeground="white", cursor="hand2", command=self.new_frame7)
            self.next5_btn.place(x=110, y=500)

            

    #frame7
    def submit_func(self):
        i = 0
        while i<len(self.ans) and i<len(self.user_ans):
            if self.ans[i] == self.user_ans[i]:
                self.score += 1
            i += 1

    def new_frame7(self):
        if (self.radio9.get() and self.radio10.get()) not in [1, 2, 3, 4]:
            msg.showwarning('Quiz App', 'Please answer all the questions!!')
        else:
            self.user_ans.append(self.radio9.get())
            self.user_ans.append(self.radio10.get())
            frame7 = Frame(self.root, width=400, height=560, bg='white')
            frame7.place(x=0, y=0)
            self.submit_func()

            #ResultImage logo
            self.img = Image.open(r"images\result.jpg")
            self.img = self.img.resize((350,300))
            self.img = ImageTk.PhotoImage(self.img)
            self.image1 = Label(frame7, image=self.img, border=0).place(x=30, y=0)

            Label(frame7, text='RESULT', font=('Helvetika',20,'bold underline'), bg='white').place(x=143, y=275)
            
            if self.score == 10:
                Label(frame7, text='Excellent!!', font=('comicsansms',17,'bold'), bg='white', justify=CENTER).place(x=145, y=320)
                Label(frame7, text='Your Score : '+str(self.score), font=('comicsansms',17,'bold'), bg='white', justify=CENTER).place(x=120, y=370)
                Label(frame7, text='Total Score : 10', font=('comicsansms',17,'bold'), bg='white', justify=CENTER).place(x=116, y=410)
                Label(frame7, text=str(round((self.score/10)*100, 2))+'%', font=('comicsansms',17,'bold'), bg='white', justify=CENTER).place(x=170, y=450)
            elif self.score>=7 and self.score<10:
                Label(frame7, text='Good!!', font=('comicsansms',17,'bold'), bg='white', justify=CENTER).place(x=163, y=320)
                Label(frame7, text='Your Score : '+str(self.score), font=('comicsansms',17,'bold'), bg='white', justify=CENTER).place(x=120, y=370)
                Label(frame7, text='Total Score : 10', font=('comicsansms',17,'bold'), bg='white', justify=CENTER).place(x=116, y=410)
                Label(frame7, text=str(round((self.score/10)*100, 2))+'%', font=('comicsansms',17,'bold'), bg='white', justify=CENTER).place(x=170, y=450)
            elif self.score == 5 or self.score == 6:
                Label(frame7, text='Average!!', font=('comicsansms',17,'bold'), bg='white', justify=CENTER).place(x=148, y=320)
                Label(frame7, text='Your Score : '+str(self.score), font=('Times New Roman',17,'bold'), bg='white', justify=CENTER).place(x=120, y=370)
                Label(frame7, text='Total Score : 10', font=('Times New Roman',17,'bold'), bg='white', justify=CENTER).place(x=116, y=410)
                Label(frame7, text=str(round((self.score/10)*100, 2))+'%', font=('comicsansms',17,'bold'), bg='white', justify=CENTER).place(x=170, y=450)
            else:
                Label(frame7, text='Poor!!, Better luck next time', font=('comicsansms',17,'bold'), bg='white', justify=CENTER).place(x=40, y=320)
                Label(frame7, text='Your Score : '+str(self.score), font=('comicsansms',17,'bold'), bg='white', justify=CENTER).place(x=120, y=370)
                Label(frame7, text='Total Score : 10', font=('comicsansms',17,'bold'), bg='white', justify=CENTER).place(x=116, y=410)
                Label(frame7, text=str(round((self.score/10)*100, 2))+'%', font=('comicsansms',17,'bold'), bg='white', justify=CENTER).place(x=170, y=450)


            self.next5_btn = Button(frame7, text="DONE", padx=69, font="commissars 11 bold", bd=1, bg="#1E90FF", fg="white",
                            activebackground="#1E90FF", activeforeground="white", cursor="hand2", command=self.done)
            self.next5_btn.place(x=110, y=510)

    def done(self):
        self.root.destroy()



root = Tk()
obj = quizApp(root)
root.mainloop()
