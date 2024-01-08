from tkinter import Image, messagebox, END, Frame, Label
import ttkbootstrap
from ttkbootstrap.constants import *
from PIL import ImageTk, Image, ImageDraw, ImageFont
import time
from config import *


# ====================================================================================
class MainFrame(ttkbootstrap.Frame):
    def __init__(self, win, current_lan):
        super().__init__(win)
        self.win = win
        self.columnconfigure(0, weight=1)

        self.current_lan = current_lan
        self.start_test()

    # --------------------------------------------------------------
    def start_test(self):
        self.typing_word = TypingWord(self.win, self.current_lan)
        self.result_frm = ResultFrame(self, self.typing_word, self.start_test, self.finish_test, self.taggle_language)
        self.result_frm.grid(row=0, column=0, pady=(10,3), sticky=NSEW)
        
        self.new_words_frm = ttkbootstrap.Frame(self)#, border=True, borderwidth=2, relief=GROOVE)
        self.new_words_frm.grid(row=1, column=0, pady=(10,0), sticky=NSEW)
        self.showing_all_words = ShowingAllWords(self.new_words_frm, self.typing_word)
        self.showing_all_words.grid(row=0, column=0, sticky=NSEW)

        self.text_entry = TextEntry(self, self.typing_word, self.start_timer)
        self.text_entry.configure(width=500)
        self.text_entry.grid(row=2, column=0, sticky=NSEW)
        self.text_entry.bind('Key', self.start_timer)

        self.update_idletasks()
        self.grid(row=1, column=0, padx=int((self.win.winfo_screenwidth() - self.winfo_reqwidth())/2), pady=10, sticky=NSEW)
        self.result_frm.grid(row=0, column=0, padx=int((self.winfo_reqwidth() - self.result_frm.winfo_reqwidth())/2), sticky=NSEW)
        self.showing_all_words.grid(row=0, column=0, padx=int((self.winfo_reqwidth() - self.showing_all_words.winfo_reqwidth())/2), sticky=NSEW)

    def taggle_language(self, lan):   
        self.current_lan = lan
        self.start_test()
        
    def on_text_change(self, sv):
        self.typing_word.current_input.get()

    def start_timer(self, event):
        self.text_entry.ent.configure(state=NORMAL)
        self.result_frm.restart_btn.configure(state=NORMAL)
        self.result_frm.exit_btn.configure(state=NORMAL)
        if not self.typing_word.is_test_running:
            self.typing_word.start_time = time.time()
            self.typing_word.is_test_running = True
            self.after(60000, self.finish_test)
            self.update_timer()
            self.typing_word.current_input.trace('w', lambda name, index, mode, sv=self.typing_word.current_input: self.on_text_change(sv))
        if event.keysym == 'space':
            self.check_word()
            self.typing_word.current_input.set('')
            self.showing_all_words.load_photo()
        elif event.keysym == 'Return':
            response = messagebox.askokcancel(self.typing_word.lan_setting['msg4'], self.typing_word.lan_setting['msg5'])
            if response is True:
                print('pressed OK')
                self.result_frm.time_left.configure(text='Finished!')
                self.result_frm.restart_btn.configure(state=NORMAL, bootstyle=SUCCESS)
                self.finish_test()
            else: 
                pass
    
    def update_timer(self):
        if self.typing_word.time_left > 0 and self.typing_word.is_test_running:
            self.typing_word.time_left -= 1
            self.result_frm.time_left.configure(text=self.typing_word.time_left)
            self.after(1000, self.update_timer)
        else:
            if self.typing_word.time_left == 0:
                self.result_frm.time_left.configure(text='Time Up!')
                self.result_frm.restart_btn.configure(state=NORMAL, bootstyle=SUCCESS)
            self.finish_test()

    def check_word(self):
        typed_word = self.typing_word.current_input.get().strip()
        correct_word = self.typing_word.words_to_test[self.typing_word.current_word_index]

        self.typing_word.typed_words.append(typed_word)
        if typed_word == correct_word:
            self.typing_word.correct_words.append(correct_word)
            self.typing_word.correct_characters += typed_word 
        else:
            self.typing_word.incorrect_words.append(correct_word)
            self.typing_word.incorrect_characters += typed_word

        self.typing_word.current_word_index += 1
        if self.typing_word.current_word_index < len(self.typing_word.words_to_test):
            self.showing_all_words.current_word = self.typing_word.words_to_test[self.typing_word.current_word_index]
            self.showing_all_words.load_photo()
        else:
            self.finish_test()

    def save_record(self, time, wpm, cpm):
        for item in LANGUAGES:
            if item == self.current_lan:
                item['records'].append({'time':time, 'wpm':wpm, 'cpm':cpm})

    def finish_test(self):
        if self.typing_word.is_test_running and self.typing_word.current_word_index != 0:
            elapsed_time = 60 - self.typing_word.time_left
            wpm = int(self.typing_word.current_word_index / elapsed_time * 60)
            cpm = int(len(self.typing_word.correct_characters) / elapsed_time * 60)
            current_time = dt.now().strftime('%H:%m:%S')

            self.result_frm.corrected_wpm.configure(text=wpm)
            self.result_frm.corrected_cpm.configure(text=cpm)
            self.result_frm.score_lb.configure(text=f'{current_time}, {cpm} CPM ({wpm} WPM)')

            self.typing_word.is_test_running = False
            self.typing_word.current_input.set(self.typing_word.lan_setting['msg3'])
            self.text_entry.ent.configure(state=DISABLED)

            self.save_record(current_time, wpm, cpm)


class TypingWord():
    def __init__(self, win, lan):
        self.win = win
    
        self.lan_setting = lan
        self.words_to_test = self.lan_setting['words']
        self.current_word_index = 0

        self.current_input = ttkbootstrap.StringVar()

        self.typed_words = [] 
        self.correct_words = [] 
        self.incorrect_words = []
        self.wpm = 0

        self.typed_characters = ''
        self.correct_characters = ''
        self.incorrect_characters = ''
        self.cpm = 0
        
        self.time_left = 60
        
        self.start_time = None
        self.is_test_running = False


class ResultFrame(ttkbootstrap.Frame):
    def __init__(self, win, typing_word, start_test, finish_test, taggle_language): 
        super().__init__(win)
        self.columnconfigure((0,1,2), weight=1)
        self.rowconfigure((0,1,2), weight=1)
        self.cumulative_rows = 0
        self.typing_word = typing_word
    
        ttkbootstrap.Label(self, text=self.typing_word.lan_setting['msg1'], font=(self.typing_word.lan_setting['font'], self.typing_word.lan_setting['font_size'][0]), anchor=CENTER).grid(row=0, column=0, columnspan=3, sticky=NSEW)
        ttkbootstrap.Label(self, text=self.typing_word.lan_setting['msg2'], font=(self.typing_word.lan_setting['font'], self.typing_word.lan_setting['font_size'][1]), anchor=CENTER).grid(row=1, column=1, sticky=NSEW)
        
        self.score_frm1 = ttkbootstrap.Frame(self, border=True, borderwidth=2, relief=GROOVE)
        self.score_frm1.grid(row=2, column=0, columnspan=3, padx=250, pady=(0,10), sticky=NSEW)
        for item in LANGUAGES:
            if item == self.typing_word.lan_setting:
                if len(item['records']) == 0:
                    self.score_lb = ttkbootstrap.Label(self.score_frm1, text=f'{CURRENT_TIME},  ?  CPM ( ?  WPM)', font=(self.typing_word.lan_setting['font'], self.typing_word.lan_setting['font_size'][0]))
                else:
                    self.score_lb = ttkbootstrap.Label(self.score_frm1, text=f'{item['records'][-1]['time']}, {item['records'][-1]['cpm']} CPM ({item['records'][-1]['wpm']} WPM)', font=(self.typing_word.lan_setting['font'], self.typing_word.lan_setting['font_size'][0]))
        self.score_lb.grid(row=0, column=0, columnspan=9, padx=100, pady=4, sticky=NSEW)

        self.score_frm2 = ttkbootstrap.Frame(self)
        self.score_frm2.grid(row=3, column=0, columnspan=9, padx=100, pady=(30,0), sticky=NSEW)
        ttkbootstrap.Label(self.score_frm2, text=self.typing_word.lan_setting['msg6']).grid(row=0, column=0, padx=(30,0))
        self.corrected_cpm = ttkbootstrap.Label(self.score_frm2, text=' ? ', background='white', width=8, border=True, borderwidth=1, relief=GROOVE, anchor=CENTER)
        self.corrected_cpm.grid(row=0, column=1, sticky=NSEW)

        ttkbootstrap.Label(self.score_frm2, text=self.typing_word.lan_setting['msg7']).grid(row=0, column=2, padx=2)
        self.corrected_wpm = ttkbootstrap.Label(self.score_frm2, text=' ? ', background='white', width=8, border=True, borderwidth=1, relief=GROOVE, anchor=CENTER)
        self.corrected_wpm.grid(row=0, column=3, sticky=NSEW)

        ttkbootstrap.Label(self.score_frm2, text=self.typing_word.lan_setting['msg8']).grid(row=0, column=4, padx=2)
        self.time_left = ttkbootstrap.Label(self.score_frm2, text=self.typing_word.time_left, background='white', width=8, border=True, borderwidth=1, relief=GROOVE, anchor=CENTER)
        self.time_left.grid(row=0, column=5, sticky=NSEW)

        self.restart_btn = ttkbootstrap.Button(self.score_frm2, text=self.typing_word.lan_setting['msg9'], command=start_test, bootstyle='secondary-link', width=6, state=DISABLED)
        self.restart_btn.grid(row=0, column=6, padx=(20,2))
        self.exit_btn = ttkbootstrap.Button(self.score_frm2, text=self.typing_word.lan_setting['msg10'], command=finish_test, bootstyle='danger', width=4, state=DISABLED)
        self.exit_btn.grid(row=0, column=7, padx=2)
            
        self.other_lans = [item for item in LANGUAGES if item != self.typing_word.lan_setting]
        self.lan_btn1 = ttkbootstrap.Button(self.score_frm2, text=self.other_lans[0]['name'], command=lambda lan=self.other_lans[0]: taggle_language(lan), width=2, bootstyle='success-link') # 'success-outline'
        self.lan_btn1.grid(row=0, column=8, padx=2)
        self.lan_btn2 = ttkbootstrap.Button(self.score_frm2, text=self.other_lans[1]['name'], command=lambda lan=self.other_lans[1]: taggle_language(lan), width=2, bootstyle='info-link')
        self.lan_btn2.grid(row=0, column=9, padx=2)

class ShowingAllWords(Frame): 
    def __init__(self, win, typing_word, **kwargs): 
        super().__init__(win, **kwargs)
        self.columnconfigure((0,1,2), weight=1)
        self.rowconfigure((0,1,2), weight=1)
        self.cumulative_rows = 0
        self.typing_word = typing_word
        
        self.current_lan = self.typing_word.lan_setting
        self.current_word = self.typing_word.words_to_test[self.typing_word.current_word_index]
        self.user_input = self.typing_word.current_input.get().strip()

        self.d_font = ImageFont.truetype(font=self.current_lan['font'], size=self.current_lan['font_size'][2])
        self.other_lans = [item for item in LANGUAGES if item != self.typing_word.lan_setting]

        self.words_by_row = []
        row_w = 0
        row_words = []

        for word in self.current_lan['words']:
            txt = Image.new('RGBA', (80, 40))
            d_txt = ImageDraw.Draw(txt)
            _, _, w, h = d_txt.textbbox((0,0), text=word, font=self.d_font)
            
            if h >= self.current_lan['word_h']:
                self.current_lan['word_h'] = h  

            if row_w + w <= 550:
                row_words.append(word)
                row_w += w
            else:
                self.words_by_row.append({'words': row_words, 'width':row_w, 'photo': [], 'frm': Frame(self)})
                row_words = [word]
                row_w = 0
        if row_words:
            self.words_by_row.append({'words': row_words, 'width':row_w, 'photo': [], 'frm': Frame(self)})
        
        self.current_lan['max_row_w'] = max([item['width'] for item in self.words_by_row]) 
        self.load_photo()

    def load_photo(self):
        word_h = max([item['word_h'] for item in LANGUAGES])
        # row_w = max([item['max_row_w'] for item in LANGUAGES])

        for i in range (len(self.words_by_row)):
            padx = int((self.current_lan['max_row_w'] - self.words_by_row[i]['width'])/2) # self.current_lan['max_row_w']
            if self.current_word in self.words_by_row[i]['words']:
                if i < 2:
                    self.words_by_row[0]['frm'].grid(row=0, column=0, padx=padx, pady=(15,0))
                    self.words_by_row[1]['frm'].grid(row=1, column=0, padx=padx, pady=10)
                    self.words_by_row[2]['frm'].grid(row=2, column=0, padx=padx, pady=(0,15))
                else:
                    self.words_by_row[i-2]['frm'].grid_remove()
                    self.words_by_row[i-1]['frm'].grid(row=0, column=0, padx=padx, pady=(15,0))
                    self.words_by_row[i]['frm'].grid(row=1, column=0, padx=padx, pady=10)
                    self.words_by_row[i+1]['frm'].grid(row=2, column=0, padx=padx, pady=(0,15))
                 
            for col_no, word in enumerate(self.words_by_row[i]['words']):
                if word == self.current_word:
                    bg_fill = COLOR_GROUP[3]['rgba'] # light green
                    if word in self.typing_word.typed_words:
                        d_text_fill = COLOR_GROUP[4]['rgba'] # white
                    else:
                        d_text_fill = COLOR_GROUP[0]['rgba'] # black
                else:
                    bg_fill= COLOR_GROUP[4]['rgba'] # white
                    if word in self.typing_word.correct_words:  
                        d_text_fill = COLOR_GROUP[5]['rgba'] # Blue
                    elif word in self.typing_word.incorrect_words:  
                        d_text_fill = COLOR_GROUP[2]['rgba'] # Red
                    else:
                        d_text_fill = COLOR_GROUP[0]['rgba'] # Black

                txt = Image.new('RGBA', (80, word_h+10), bg_fill) # self.current_lan['word_h']
                d_txt = ImageDraw.Draw(txt)
                _, _, w, h = d_txt.textbbox((0,0), text=word , font=self.d_font)
                added_space = 16

                resized_txt = txt.resize((w+added_space, word_h+10))
                d_txt = ImageDraw.Draw(resized_txt)
                d_txt.text((int((w+added_space)/2), int(word_h+10)/2), text=word , font=self.d_font, fill=d_text_fill, anchor='mm') # https://pillow.readthedocs.io/en/stable/handbook/text-anchors.html

                txt_mask = Image.new('RGBA', (w+added_space, word_h+10), bg_fill)
                d_mask = ImageDraw.Draw(txt_mask)
                d_mask.rounded_rectangle((0, 0, w+added_space, word_h+10), radius=30, fill=bg_fill)

                txt_mask.paste(resized_txt, (0, 0, w+added_space, word_h+10), resized_txt)
                photo = ImageTk.PhotoImage(txt_mask)
                self.words_by_row[i]['photo'].append(photo)

                word_lb = Label(self.words_by_row[i]['frm'], image=photo)
                word_lb.grid(row=0, column=col_no)#, sticky=NSEW)  
    
class TextEntry(ttkbootstrap.Frame): # https://docs.python.org/3/library/tkinter.ttk.html#ttk-styling
    def __init__(self, win, typing_word, start_test):
        super().__init__(win)
        self.typing_word = typing_word

        self.ent = ttkbootstrap.Entry(self, textvariable=self.typing_word.current_input, foreground=COLOR_GROUP[2]['hex'], font=(typing_word.lan_setting['font'], typing_word.lan_setting['font_size'][2]), justify=CENTER) 
        self.ent.pack(fill=X)

        self.ent.insert(0, typing_word.lan_setting['msg3'])
        self.ent.bind('<FocusIn>', self.center_mouse_over_entry)
        self.ent.bind('<Key>', start_test)

    def center_mouse_over_entry(self, event):
        self.ent.delete(0, END)
        self.ent.focus_set()
        x_center = self.winfo_reqwidth() // 2
        y_center = self.winfo_reqheight() // 2
        self.ent.event_generate('<Motion>', warp=True, x=x_center, y=y_center)
    
    def on_text_change(self, name, index, mode, sv):
        print(sv.get())


